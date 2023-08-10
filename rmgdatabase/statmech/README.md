Directory Contents:
 - `statmech_files.tar.xz`: the original data files contained in RMG-database, tarballed and compressed. Decompress and un-tar with `tar -xf statmech_files.tar.xz`.
 - `make_statmech_table.py`: reads through all the files from the uncompressed directories and flattens them into a database using `peewee`.
 - `statmech.db`: flattened, relational database-version of the original contents of this directory.

The only file header contents from `libraries/halogens_G4.py`:
name = "halogens_G4"
shortDesc = "G4 (B3LYP/GTBas3)"
longDesc = """
Small halogenated species calculated with G4 method (B3LYP/GTBas3) using Gaussian 16
"""