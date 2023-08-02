import os

import peewee as pw
from tqdm import tqdm

from rmgdatabase.tree_str_to_pairs import sketchy_conversion

db = pw.SqliteDatabase("transport.db")

all_groups_fpaths = [os.path.join("groups", i) for i in os.listdir("groups")]

all_libraries_fpaths = [os.path.join("libraries", i) for i in os.listdir("libraries")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class TransportGroups(BaseModel):
    rmgdb_index = pw.IntegerField()
    group_type = pw.TextField()
    label = pw.TextField()
    group = pw.TextField()
    is_head_node = pw.BooleanField(default=False)
    contribution_Tc = pw.FloatField(null=True)
    contribution_Pc = pw.FloatField(null=True)
    contribution_Vc = pw.FloatField(null=True)
    contribution_Tb = pw.FloatField(null=True)
    contribution_is_linear = pw.BooleanField(null=True)
    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


class TransportGroupsPairs(BaseModel):
    label = pw.ForeignKeyField(TransportGroups)
    parent_to = pw.TextField(null=True)


class TransportLibraries(BaseModel):
    rmgdb_index = pw.IntegerField()
    library_type = pw.TextField()
    label = pw.TextField()
    molecule = pw.TextField()
    shape_index = pw.IntegerField()
    epsilon = pw.FloatField()
    epsilon_units = pw.TextField()
    dipole_moment = pw.FloatField()
    dipole_moment_units = pw.TextField()
    sigma = pw.FloatField()
    sigma_units = pw.TextField()
    polarizability = pw.FloatField()
    polarizability_units = pw.TextField()
    rot_relax_col_num = pw.FloatField()
    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


db.connect()

db.create_tables([TransportGroups, TransportLibraries, TransportGroupsPairs])

for fpath in tqdm(all_groups_fpaths):
    with open(fpath, "r") as file:
        file_data = iter(file.readlines())
        new_group = None
        while 1:
            line = next(file_data)
            if line.startswith("entry"):
                if new_group is not None:
                    new_group.save()
                new_group = TransportGroups()
                new_group.group_type = fpath[7:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_group.rmgdb_index = idx
                if idx == 0:
                    new_group.is_head_node = True
            elif line.startswith("    label"):
                new_group.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    group"):
                adj_list = ""
                while (line := next(file_data)) != '""",\n':
                    adj_list += line
                new_group.group = adj_list
            elif line.startswith("        Tc"):
                new_group.contribution_Tc = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        Pc"):
                new_group.contribution_Pc = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        Vc"):
                new_group.contribution_Vc = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        Tb"):
                new_group.contribution_Tb = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        structureIndex"):
                new_group.contribution_is_linear = (
                    int(line.split("=")[1].replace(",", "")) == 0
                )
            elif line.startswith("    shortDesc"):
                new_group.short_desc = (
                    line.split("=")[1].replace('"', "").replace(",", "")
                )
            elif line.startswith("    longDesc"):
                new_group.long_desc = (
                    line.split("=")[1].replace('"', "").replace(",", "")
                )
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
            new_pair = TransportGroupsPairs(
                label=pair[0],
                parent_to=pair[1],
            )
            new_pair.save()


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
                if new_library is not None:
                    new_library.save()
                new_library = TransportLibraries()
                new_library.library_type = fpath[10:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_library.rmgdb_index = idx
            elif line.startswith("    label"):
                new_library.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    molecule"):
                adj_list = ""
                while (line := next(file_data)) not in {'    """,\n', '""",\n'}:
                    adj_list += line
                new_library.molecule = adj_list
            elif line.startswith("        shapeIndex"):
                new_library.shape_index = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        epsilon"):
                temp = line.split("=")[1].replace(")", "").replace("(", "").split(",")
                new_library.epsilon = float(temp[0])
                new_library.epsilon_units = temp[1].replace('"', "")
            elif line.startswith("        sigma"):
                temp = line.split("=")[1].replace(")", "").replace("(", "").split(",")
                new_library.sigma = float(temp[0])
                new_library.sigma_units = temp[1].replace('"', "")
            elif line.startswith("        dipoleMoment"):
                temp = line.split("=")[1].replace(")", "").replace("(", "").split(",")
                new_library.dipole_moment = float(temp[0])
                new_library.dipole_moment_units = temp[1].replace('"', "")
            elif line.startswith("        polarizability"):
                temp = line.split("=")[1].replace(")", "").replace("(", "").split(",")
                new_library.polarizability = float(temp[0])
                new_library.polarizability_units = temp[1].replace('"', "")
            elif line.startswith("        rotrelaxcollnum"):
                new_library.rot_relax_col_num = float(
                    line.split("=")[1].replace(",", "")
                )
            elif line.startswith("    shortDesc"):
                new_library.short_desc = (
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
                new_library.long_desc = comment
