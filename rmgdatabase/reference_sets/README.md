Directory Contents:
 - `reference_yml_files.tar.xz`: the original yaml data files contained in RMG-database, tarballed and compressed. Decompress and un-tar with `tar -xf reference_yml_files.tar.xz`.
 - `make_reference_sets_table.py`: reads through all the files from the uncompressed yaml directory and flattens them into a database using `peewee`.
 - `reference_sets.db`: flattened, relational database-version of the original contents of this directory.