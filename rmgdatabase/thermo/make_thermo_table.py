import os
import pickle as pkl

import peewee as pw
from tqdm import tqdm

from rmgdatabase.tree_str_to_pairs import sketchy_conversion

if os.path.exists("thermo.db"):
    os.remove("thermo.db")
db = pw.SqliteDatabase("thermo.db")

all_groups_fpaths = [os.path.join("groups", i) for i in os.listdir("groups")]

all_libraries_fpaths = [os.path.join("libraries", i) for i in os.listdir("libraries")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class ThermoGroups(BaseModel):
    rmgdb_index = pw.IntegerField()
    group_type = pw.TextField()
    label = pw.TextField()
    group = pw.TextField()
    metal = pw.TextField(null=True)
    facet = pw.TextField(null=True)
    rank = pw.IntegerField(null=True)

    thermo_type = pw.TextField(null=True)
    thermo = pw.BlobField(null=True)

    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


class ThermoGroupsPairs(BaseModel):
    label = pw.ForeignKeyField(ThermoGroups)
    parent_to = pw.TextField(null=True)


class ThermoLibraries(BaseModel):
    rmgdb_index = pw.IntegerField()
    library_type = pw.TextField()
    label = pw.TextField()
    molecule = pw.TextField()

    thermo_type = pw.TextField(null=True)
    thermo = pw.BlobField(null=True)

    reference = pw.TextField(null=True)
    reference_type = pw.TextField(null=True)

    rank = pw.IntegerField(null=True)
    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


# lord forgive me
class entry:
    def __init__(
        self,
        index,
        label,
        group,
        thermo,
        longDesc=None,
        shortDesc=None,
        metal=None,
        facet=None,
        rank=None,
    ):
        self.index = index
        self.label = label
        self.group = group
        self.thermo = thermo
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.metal = metal
        self.facet = facet
        self.rank = rank


class ThermoData:
    def __init__(self, Tdata, Cpdata, H298, S298, Cp0=None, CpInf=None):
        self.Tdata = Tdata
        self.CPdata = Cpdata
        self.H298 = H298
        self.S298 = S298
        self.Cp0 = Cp0
        self.CpInf = CpInf


# TODO: NASA, ThermoData, etc. should not be pickled and saved as BLOBs, but instead put into another table
# and FK'd back to the ThermoLibrariesTable


class NASA:
    def __init__(
        self, polynomials, Tmin, Tmax, E0=None, Cp0=None, CpInf=None, comment=None
    ):
        self.polynomials = polynomials
        self.Tmin = Tmin
        self.Tmax = Tmax
        self.E0 = E0
        self.Cp0 = Cp0
        self.CpInf = CpInf
        self.comment = comment


class NASAPolynomial:
    def __init__(self, coeffs, Tmin, Tmax):
        self.coeffs = coeffs
        self.Tmin = Tmin
        self.Tmax = Tmax


class Wilhoit:
    def __init__(self, Cp0, CpInf, a0, a1, a2, a3, H0, S0, B):
        self.Cp0 = Cp0
        self.CpInf = CpInf
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.H0 = H0
        self.S0 = S0
        self.B = B


db.connect()

db.create_tables([ThermoGroups, ThermoGroupsPairs, ThermoLibraries])

print("Flattening groups...", flush=True)
for fpath in tqdm(all_groups_fpaths):
    with open(fpath, "r") as file:
        file_data = iter(file.readlines())
        new_group = None
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
                try:
                    exec(entry_str)
                except:
                    print(entry_str)
                    raise

                new_group = ThermoGroups()
                new_group.rmgdb_index = entry_row.index
                new_group.group_type = fpath[7:-3]
                new_group.label = entry_row.label
                new_group.group = entry_row.group
                if (val := entry_row.metal) is not None:
                    new_group.metal = val
                if (val := entry_row.facet) is not None:
                    new_group.facet = val

                new_group.thermo_type = str(type(entry_row.thermo))
                new_group.thermo = pkl.dumps(entry_row.thermo)
                new_group.rank = entry_row.rank

                if (desc := entry_row.shortDesc) is not None:
                    new_group.short_desc = desc
                new_group.long_desc = entry_row.longDesc
                new_group.save()
            elif line.startswith("tree"):
                break

        # now deal with the tree relationship
        next(file_data)
        tree_str = ""
        while '"""' not in (line := next(file_data)):
            tree_str += line
        all_pairs = sketchy_conversion(tree_str)
        for pair in tqdm(all_pairs):
            if pair[0] is None:
                continue  # head nodes
            new_pair = ThermoGroupsPairs(
                label=pair[0],
                parent_to=pair[1],
            )
            new_pair.save()

del entry


# redefine entry for the libraries
class entry:
    def __init__(
        self,
        index,
        label,
        molecule,
        thermo,
        shortDesc=None,
        longDesc=None,
        reference=None,
        referenceType=None,
        metal=None,
        facet=None,
        rank=None,
    ):
        self.index = index
        self.label = label
        self.molecule = molecule
        self.thermo = thermo
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.reference = reference
        self.referenceType = referenceType
        self.metal = metal
        self.facet = facet
        self.rank = rank


class Reference:
    def __init__(self, authors, title, year, url):
        self.self_str = " ".join(authors) + " " + title + " " + year + " " + url


print("Flattening libraries...", flush=True)
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
                if "deleted duplicate" in entry_str:
                    entry_str += '""",\n)\n'
                try:
                    exec(entry_str)
                except:
                    print(entry_str)
                    raise

                new_library = ThermoLibraries()
                new_library.rmgdb_index = entry_row.index
                new_library.library_type = fpath[10:-3]
                new_library.label = entry_row.label
                new_library.molecule = entry_row.molecule

                new_library.thermo_type = str(type(entry_row.thermo))
                new_library.thermo = pkl.dumps(entry_row.thermo)

                new_library.short_desc = entry_row.shortDesc
                new_library.long_desc = entry_row.longDesc
                new_library.rank = entry_row.rank
                if type(entry_row.reference) is Reference:
                    new_library.reference = entry_row.reference.self_str
                else:
                    new_library.reference = entry_row.reference
                new_library.reference_type = entry_row.referenceType
                new_library.metal = entry_row.metal
                new_library.facet = entry_row.facet
                new_library.save()
