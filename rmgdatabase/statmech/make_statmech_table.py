import ast
import os

import peewee as pw
from tqdm import tqdm

from rmgdatabase.tree_str_to_pairs import sketchy_conversion

if os.path.exists("statmech.db"):
    os.remove("statmech.db")
db = pw.SqliteDatabase("statmech.db")

all_groups_fpaths = [os.path.join("groups", i) for i in os.listdir("groups")]

all_libraries_fpaths = [os.path.join("libraries", i) for i in os.listdir("libraries")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class StatmechGroups(BaseModel):
    rmgdb_index = pw.IntegerField()
    group_type = pw.TextField()
    label = pw.TextField()
    group = pw.TextField()

    frequencies = pw.TextField(null=True)
    symmetry = pw.IntegerField(null=True)

    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


class StatmechGroupsPairs(BaseModel):
    label = pw.ForeignKeyField(StatmechGroups)
    parent_to = pw.TextField(null=True)


class StatmechLibraries(BaseModel):
    rmgdb_index = pw.IntegerField()
    library_type = pw.TextField()
    label = pw.TextField()
    molecule = pw.TextField()

    E0 = pw.FloatField(null=True)
    E0_units = pw.TextField(null=True)
    mass = pw.FloatField(null=True)
    mass_units = pw.TextField(null=True)

    # all on the same line
    intertia_moment_1 = pw.FloatField(null=True)
    intertia_moment_2 = pw.FloatField(null=True)
    intertia_moment_3 = pw.FloatField(null=True)
    inertia_units = pw.TextField(null=True)
    symmetry = pw.IntegerField(null=True)
    frequencies = pw.BlobField(null=True)  # bytes-like object, compressed list
    frequencies_units = pw.TextField(null=True)
    spin_multiplicity = pw.IntegerField(null=True)
    optical_isomers = pw.IntegerField(null=True)

    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


db.connect()

db.create_tables([StatmechGroups, StatmechGroupsPairs, StatmechLibraries])

for fpath in tqdm(all_groups_fpaths):
    with open(fpath, "r") as file:
        file_data = iter(file.readlines())
        new_group = None
        while 1:
            line = next(file_data)
            if line.startswith("entry"):
                if new_group is not None:
                    new_group.save()
                new_group = StatmechGroups()
                new_group.group_type = fpath[7:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_group.rmgdb_index = idx
            elif line.startswith("    label"):
                new_group.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    group"):
                if '"""' in line:
                    adj_list = ""
                    while (line := next(file_data)) != '""",\n':
                        adj_list += line
                    new_group.group = adj_list
                else:  # single line group
                    new_group.group = (
                        line.split("=")[1].replace('"', "").replace(",", "")
                    )

            elif line.startswith("        symmetry"):
                new_group.symmetry = int(line.split("=")[1].replace(",", ""))

            elif line.startswith("        frequencies"):
                frequencies_str = "(\n"
                while (line := next(file_data)) != "        ],\n":
                    frequencies_str += line
                frequencies_str += ")"
                new_group.frequencies = (
                    frequencies_str  # ast.literal_eval(frequencies_str)
                )

            elif line.startswith("    shortDesc"):
                new_group.short_desc = (
                    line.split("=")[1].replace('"', "").replace(",", "")
                )
            elif line.startswith("    longDesc"):
                # can be multiline
                comment = ""
                if line == '    longDesc="""\n':
                    while (line := next(file_data)) != '""",\n':
                        comment += line
                else:
                    comment = line.split("=")[1].replace('"', "").replace(",", "")
                new_group.long_desc = comment
            elif line.startswith("tree"):
                break

        # now deal with the tree relationship
        next(file_data)
        tree_str = ""
        while (line := next(file_data)) != '"""\n':
            tree_str += line
        all_pairs = sketchy_conversion(tree_str)
        for pair in tqdm(all_pairs):
            if pair[0] is None:
                continue  # head nodes
            new_pair = StatmechGroupsPairs(
                label=pair[0],
                parent_to=pair[1],
            )
            new_pair.save()


# lord forgive me
class entry:
    def __init__(self, index, label, molecule, statmech, shortDesc, longDesc):
        self.index = index
        self.label = label
        self.molecule = molecule
        self.statmech = statmech
        self.shortDesc = shortDesc
        self.longDesc = longDesc


class Conformer:
    def __init__(self, E0, modes, spin_multiplicity=None, optical_isomers=None):
        self.E0 = E0
        self.modes = modes
        self.spin_multiplicity = spin_multiplicity
        self.optical_isomers = 0


class IdealGasTranslation:
    def __init__(self, mass):
        self.mass = mass


class LinearRotor:
    def __init__(self, inertia, symmetry):
        self.inertia = inertia
        self.symmetry = symmetry


class NonlinearRotor:
    def __init__(self, inertia, symmetry):
        self.inertia = inertia
        self.symmetry = symmetry


class HarmonicOscillator:
    def __init__(self, frequencies):
        self.frequencies = frequencies


for fpath in tqdm(all_libraries_fpaths):
    with open(fpath, "r") as file:
        file_data = iter(file.readlines())
        new_library = None
        while 1:
            try:
                line = next(file_data)
            except StopIteration:
                break
            if line.startswith("entry"):
                entry_row = None
                entry_str = "entry_row = " + line
                while (line := next(file_data)) != ")\n":
                    entry_str += line
                entry_str += line
                exec(entry_str)

                new_library = StatmechLibraries()
                new_library.rmgdb_index = entry_row.index
                new_library.library_type = fpath[10:-3]
                new_library.label = entry_row.label
                new_library.molecule = entry_row.molecule

                new_library.E0 = entry_row.statmech.E0[0]
                new_library.E0_units = entry_row.statmech.E0[1]
                new_library.mass = entry_row.statmech.modes[0].mass[0]
                new_library.mass_units = entry_row.statmech.modes[0].mass[1]

                # all on the same line
                if type(entry_row.statmech.modes[1]) is LinearRotor:
                    new_library.intertia_moment_1 = entry_row.statmech.modes[1].inertia[
                        0
                    ]
                else:
                    new_library.intertia_moment_1 = entry_row.statmech.modes[1].inertia[
                        0
                    ][0]
                    new_library.intertia_moment_2 = entry_row.statmech.modes[1].inertia[
                        0
                    ][1]
                    new_library.intertia_moment_3 = entry_row.statmech.modes[1].inertia[
                        0
                    ][2]

                new_library.inertia_units = entry_row.statmech.modes[1].inertia[1]
                new_library.symmetry = entry_row.statmech.modes[1].symmetry
                new_library.frequencies = str(
                    entry_row.statmech.modes[2].frequencies[0]
                )
                new_library.frequencies_units = entry_row.statmech.modes[2].frequencies[
                    1
                ]

                if (val := entry_row.statmech.spin_multiplicity) is not None:
                    new_library.spin_multiplicity = val
                if (val := entry_row.statmech.optical_isomers) is not None:
                    new_library.optical_isomers = val

                new_library.short_desc = entry_row.shortDesc
                new_library.long_desc = entry_row.longDesc
                new_library.save()
