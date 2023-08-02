import os

import peewee as pw
from tqdm import tqdm

from rmgdatabase.tree_str_to_pairs import sketchy_conversion

if os.path.exists("solvation.db"):
    os.remove("solvation.db")
db = pw.SqliteDatabase("solvation.db")

all_groups_fpaths = [os.path.join("groups", i) for i in os.listdir("groups")]

all_libraries_fpaths = [os.path.join("libraries", i) for i in os.listdir("libraries")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class SolvationGroups(BaseModel):
    rmgdb_index = pw.IntegerField()
    group_type = pw.TextField()
    label = pw.TextField()
    group = pw.TextField()

    abraham_S = pw.FloatField(null=True)
    abraham_B = pw.FloatField(null=True)
    abraham_E = pw.FloatField(null=True)
    abraham_L = pw.FloatField(null=True)
    abraham_A = pw.FloatField(null=True)

    data_count_gav_S = pw.IntegerField(null=True)
    data_count_gav_B = pw.IntegerField(null=True)
    data_count_gav_E = pw.IntegerField(null=True)
    data_count_gav_L = pw.IntegerField(null=True)
    data_count_gav_A = pw.IntegerField(null=True)

    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


class SolvationGroupsPairs(BaseModel):
    label = pw.ForeignKeyField(SolvationGroups)
    parent_to = pw.TextField(null=True)


class SolvationLibraries(BaseModel):
    rmgdb_index = pw.IntegerField()
    library_type = pw.TextField()
    label = pw.TextField()
    molecule = pw.TextField()

    abraham_S = pw.FloatField(null=True)
    abraham_B = pw.FloatField(null=True)
    abraham_E = pw.FloatField(null=True)
    abraham_L = pw.FloatField(null=True)
    abraham_A = pw.FloatField(null=True)
    abraham_V = pw.FloatField(null=True)

    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


db.connect()

db.create_tables([SolvationGroups, SolvationGroupsPairs, SolvationLibraries])

for fpath in tqdm(all_groups_fpaths):
    with open(fpath, "r") as file:
        file_data = iter(file.readlines())
        new_group = None
        while 1:
            line = next(file_data)
            if line.startswith("entry"):
                if new_group is not None:
                    new_group.save()
                new_group = SolvationGroups()
                new_group.group_type = fpath[7:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_group.rmgdb_index = idx
            elif line.startswith("    label"):
                new_group.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    group"):
                adj_list = ""
                while (line := next(file_data)) != '""",\n':
                    adj_list += line
                new_group.group = adj_list

            # abraham parameters
            elif line.startswith("        S"):
                if "." not in line:
                    new_group.data_count_gav_S = int(
                        line.split("=")[1].replace(",", "")
                    )
                else:
                    new_group.abraham_S = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        B"):
                if "." not in line:
                    new_group.data_count_gav_B = int(
                        line.split("=")[1].replace(",", "")
                    )
                else:
                    new_group.abraham_B = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        E"):
                if "." not in line:
                    new_group.data_count_gav_E = int(
                        line.split("=")[1].replace(",", "")
                    )
                else:
                    new_group.abraham_E = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        L"):
                if "." not in line:
                    new_group.data_count_gav_L = int(
                        line.split("=")[1].replace(",", "")
                    )
                else:
                    new_group.abraham_L = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        A"):
                if "." not in line:
                    new_group.data_count_gav_A = int(
                        line.split("=")[1].replace(",", "")
                    )
                else:
                    new_group.abraham_A = float(line.split("=")[1].replace(",", ""))

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
            new_pair = SolvationGroupsPairs(
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
                new_library = SolvationLibraries()
                new_library.library_type = fpath[10:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_library.rmgdb_index = idx
            elif line.startswith("    label"):
                new_library.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    molecule"):
                adj_list = ""
                while (line := next(file_data)) != '""",\n':
                    adj_list += line
                new_library.molecule = adj_list

            # abraham parameters
            elif line.startswith("        S"):
                new_library.abraham_S = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        B"):
                new_library.abraham_B = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        E"):
                new_library.abraham_E = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        L"):
                new_library.abraham_L = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        A"):
                new_library.abraham_A = float(line.split("=")[1].replace(",", ""))
            elif line.startswith("        V"):
                new_library.abraham_A = float(line.split("=")[1].replace(",", ""))

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
