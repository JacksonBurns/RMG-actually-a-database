Directory Contents:
 - `surface_files.tar.xz`: the original data files contained in RMG-database, tarballed and compressed. Decompress and un-tar with `tar -xf surface_files.tar.xz`.
 - `make_surface_table.py`: reads through all the files from the uncompressed directories and flattens them into a database using `peewee`.
 - `surface.db`: flattened, relational database-version of the original contents of this directory.

Descriptions of Groups and Libraries from the file headers:
<details>
<summary> `libraries/metal.py` </summary>

name = "Metal Binding Energies"
shortDesc = ""
longDesc = """
Metal binding energies and surface site densities. 
The DFT calculations were performed by Katrin Blondal and Bjarne Kreitz (both Brown University) using Quantum Espresso with PAW PBE pseudopotentials. PBE was used as the xc-functional and a vdW-corr (DFT-D3) was applied. A 3x3 cell was used for the fcc(111) and hcp(0001) facets with 4 layers and a 1x3 cell with 12 layers for the (211) facets. Further the following settings were used: vaccum=10A (above and below), dftd3_version=4, dftd3_threebody=True, occupations='smearing', smearing='marzari-vanderbilt', degauss=0.005, mixing_mode='local-TF', tprnfor=True, nosym=True. 
Structures were optimized in a multistep procedure according to Blondal et al. (https://doi.org/10.1021/acs.iecr.9b01464) with (1) a (2,2,1) k-point grid ((2,1,1) for (211) facets) and 40 Ry cutoff and (2) (4,4,1) grid ((4,2,1) for (211) facets) and 50 Ry until forces were below 0.01 eV/A. The single point energy was computed on a (6,6,1) grid ((6,4,1) for (211) facets) and 60 Ry. Prior to the relaxation, the lattice constant of the bulk metal was determined through optimization with the calculator settings using a k-point grid of (21,21,21).
"""

</details>
