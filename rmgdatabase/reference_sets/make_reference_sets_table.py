import os
import peewee as pw

import yaml
from tqdm import tqdm

db = pw.SqliteDatabase("reference_sets.db")

all_yaml_fpaths = [os.path.join("main", i) for i in os.listdir("main")]


class BaseModel(pw.Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class ReferenceSets(BaseModel):
    inchi_key = pw.PrimaryKeyField()
    RMG_version = pw.TextField()
    adjacency_list = pw.TextField()
    charge = pw.IntegerField()
    created_timestamp = pw.DateTimeField()
    formula = pw.TextField()
    inchi = pw.TextField()
    label = pw.TextField()
    index = pw.IntegerField()
    multiplicity = pw.IntegerField()
    smiles = pw.TextField()
    symmetry_number = pw.FloatField()


class ReferenceData(BaseModel):
    inchi_key = pw.ForeignKeyField(ReferenceSets, backref="reference_data")
    source = pw.TextField()
    quantity = pw.TextField()
    units = pw.TextField()
    value = pw.FloatField()
    # optional fields
    uncertainty_type = pw.TextField(null=True)
    uncertainty_value = pw.FloatField(null=True)


class CalculatedData(BaseModel):
    inchi_key = pw.ForeignKeyField(ReferenceSets, backref="calculated_data")
    level_of_theory = pw.TextField()
    quantity = pw.TextField()
    units = pw.TextField()
    value = pw.FloatField()


def _coords_dict_to_xyz_file_str(coord_dict, inchi):
    atomic_number_array = coord_dict["isotopes"]
    xyz_array = coord_dict["coords"]["object"]
    chemical_symbols = coord_dict["symbols"]
    xyz_str = str(len(atomic_number_array)) + f"\n{inchi}\n"  # 'header' lines
    for atomic_number, atomic_coordinates, atomic_symbol in zip(
        atomic_number_array, xyz_array, chemical_symbols
    ):
        line_to_file = " "
        line_to_file += atomic_symbol
        # prepend a space for one-letter abbreviations
        if len(atomic_symbol) == 1:
            line_to_file = " " + line_to_file
        line_to_file += "        {:10.5f}        {:10.5f}        {:10.5f}\n".format(
            *atomic_coordinates,
        )
        xyz_str += line_to_file
    return xyz_str


db.connect()

db.create_tables([ReferenceSets, ReferenceData, CalculatedData])

for yaml_fpath in tqdm(all_yaml_fpaths):
    with open(yaml_fpath, "r") as file:
        data = yaml.safe_load(file)
    # iterate separately
    calcd_data = data.pop("calculated_data")
    ref_data = data.pop("reference_data")

    # remove unused fields
    data.pop("class")
    data.pop("default_xyz_chemistry")

    # renamed fields
    mw = data.pop("molecular_weight")["value"]
    ts = data.pop("datetime")
    molecule_entry = ReferenceSets(**data)
    molecule_entry.save()
    for source, value in ref_data.items():
        if "thermo_data" in value.keys():  # H298
            ref_data_entry = ReferenceData(
                inchi_key=data["inchi_key"],
                source=source,
                quantity="H298",
                value=value["thermo_data"]["H298"]["value"],
                units=value["thermo_data"]["H298"]["units"],
                uncertainty_type=value["thermo_data"]["H298"].get(
                    "uncertainty_type", None
                ),
                uncertainty_value=value["thermo_data"]["H298"].get("uncertainty", None),
            )
            ref_data_entry.save()
        else:
            # CCBDB
            for quantity, sub_value in value.items():
                if type(sub_value) is str:
                    continue  # skip class names
                # coordinates
                if "xyz_dict" in quantity:
                    ref_data_entry = ReferenceData(
                        inchi_key=data["inchi_key"],
                        source=source,
                        quantity="xyz_file",
                        value=_coords_dict_to_xyz_file_str(
                            sub_value, data["inchi_key"]
                        ),
                        units="coords",
                        uncertainty_type=None,
                        uncertainty_units=None,
                    )
                    ref_data_entry.save()
                    continue

                # atomization energy and zpe
                ref_data_entry = ReferenceData(
                    inchi_key=data["inchi_key"],
                    source=source,
                    quantity=quantity,
                    value=sub_value["value"],
                    units=sub_value["units"],
                    uncertainty_type=sub_value.get("uncertainty_type", None),
                    uncertainty_value=sub_value.get("uncertainty", None),
                )
                ref_data_entry.save()

    for level_of_theory, value in calcd_data.items():
        for quantity, sub_value in value.items():
            if type(sub_value) is str:
                continue  # skip class names
            if quantity == "thermo_data":  # H298
                calcd_data_entry = CalculatedData(
                    inchi_key=data["inchi_key"],
                    level_of_theory=level_of_theory,
                    quantity="H298",
                    value=sub_value["H298"]["value"],
                    units=sub_value["H298"]["units"],
                )
                calcd_data_entry.save()
            else:
                # coordinates
                calcd_data_entry = CalculatedData(
                    inchi_key=data["inchi_key"],
                    level_of_theory=level_of_theory,
                    quantity="xyz_file",
                    value=_coords_dict_to_xyz_file_str(sub_value, data["inchi_key"]),
                    units="coords",
                )
                calcd_data_entry.save()
