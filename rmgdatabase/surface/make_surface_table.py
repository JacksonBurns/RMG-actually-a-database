import os

import peewee as pw
from tqdm import tqdm

if os.path.exists("surface.db"):
    os.remove("surface.db")
db = pw.SqliteDatabase("surface.db")

all_libraries_fpaths = [os.path.join("libraries", i) for i in os.listdir("libraries")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class MetalLibraries(BaseModel):
    rmgdb_index = pw.IntegerField()
    library_type = pw.TextField()
    label = pw.TextField()
    surface_site_density = pw.FloatField()
    surface_site_density_units = pw.TextField()
    binding_energy_H = pw.FloatField()
    binding_energy_H_units = pw.TextField()
    binding_energy_C = pw.FloatField()
    binding_energy_C_units = pw.TextField()
    binding_energy_N = pw.FloatField()
    binding_energy_N_units = pw.TextField()
    binding_energy_O = pw.FloatField()
    binding_energy_O_units = pw.TextField()
    facet = pw.TextField()
    metal = pw.TextField()
    short_desc = pw.TextField(null=True)
    long_desc = pw.TextField(null=True)


db.connect()

db.create_tables([MetalLibraries])

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
                new_library = MetalLibraries()
                new_library.library_type = fpath[10:-3]
            elif line.startswith("    index"):
                idx = int(line.split("=")[1].replace(",", ""))
                new_library.rmgdb_index = idx
            elif line.startswith("    label"):
                new_library.label = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    metal"):
                new_library.metal = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    facet"):
                new_library.facet = line.split("=")[1].replace('"', "").replace(",", "")
            elif line.startswith("    surfaceSiteDensity"):
                temp = line.split("=")[1].replace(")", "").replace("(", "").split(",")
                new_library.surface_site_density = float(temp[0])
                new_library.surface_site_density_units = temp[1].replace('"', "")
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
            elif line.startswith('        "H": '):
                temp = line.split(": ")[1].replace(")", "").replace("(", "").split(",")
                new_library.binding_energy_H = float(temp[0])
                new_library.binding_energy_H_units = temp[1].replace('"', "")
            elif line.startswith('        "C": '):
                temp = line.split(": ")[1].replace(")", "").replace("(", "").split(",")
                new_library.binding_energy_C = float(temp[0])
                new_library.binding_energy_C_units = temp[1].replace('"', "")
            elif line.startswith('        "N": '):
                temp = line.split(": ")[1].replace(")", "").replace("(", "").split(",")
                new_library.binding_energy_N = float(temp[0])
                new_library.binding_energy_N_units = temp[1].replace('"', "")
            elif line.startswith('        "O": '):
                temp = line.split(": ")[1].replace(")", "").replace("(", "").split(",")
                new_library.binding_energy_O = float(temp[0])
                new_library.binding_energy_O_units = temp[1].replace('"', "")
