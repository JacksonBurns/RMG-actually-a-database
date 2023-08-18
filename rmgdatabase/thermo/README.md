Directory Contents:
 - `thermo_files.tar.xz`: the original data files contained in RMG-database, tarballed and compressed with `tar -cJf thermo_files.tar.xz libraries groups depository`. Decompress and un-tar with `tar -xf thermo_files.tar.xz`.
 - `make_thermo_table.py`: reads through all the files from the uncompressed directories and flattens them into a database using `peewee`.
 - `thermo.db`: flattened, relational database-version of the original contents of this directory.

