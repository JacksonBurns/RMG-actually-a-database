# RMG-actually-a-database
# SWITCH THIS TO PARQUET
Fork of RMG-database that flattens all of the files into an actual relational database and exposes the data through an interface.

Broadly compatible with Python, individually packageable (installable with `pip` and `conda`), and standalone for other research applications.

TODO:

Convert...
 - [ ] kinetics
 - [x] quantum_corrections - was already _mostly_ compatible
 - [x] reference_sets - flattened
 - [x] solvation
 - [x] statmech
 - [x] surface
 - [ ] thermo
 - [x] transport - flattened

Rather than version controlling the acutal `db` file, we should dump the database into a git-able format (like `csv` or `sql`) and then version control that.
When distributing, we can make this into an actual database file.

Also, we will not include the `tar.xz` files in either the distribution or the version control.
They are here during only the transition period to (1) make debugging easier and (2) get an actual line diff.
If they are ever needed in the future, there is always version control.
