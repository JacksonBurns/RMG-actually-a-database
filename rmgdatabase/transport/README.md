Directory Contents:
 - `transport_files.tar.xz`: the original data files contained in RMG-database, tarballed and compressed. Decompress and un-tar with `tar -xf transport_files.tar.xz`.
 - `make_transport_table.py`: reads through all the files from the uncompressed directories and flattens them into a database using `peewee`.
 - `transport.db`: flattened, relational database-version of the original contents of this directory.

Descriptions of Groups and Libraries from the file headers:
<details>
<summary> `groups/nonring.py` </summary>

name = "Joback non-rings"
shortDesc = "Groups for atoms not in a ring to estimate critical point properties according to Joback 1984"
longDesc = """
Group definitions to estimate critical point properties via group additivity, from:

Joback, K. G. A unified approach to physical property estimation using multivariate statistical techniques,
PhD Thesis, Massachusetts Institute of Technology: Cambridge, MA, 1984.

Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.

`structureIndex` is 0 if linear, 1 if makes molecule nonlinear
"""

</details>

<details>
<summary> `groups/ring.py` </summary>
name = "Joback rings"
shortDesc = "Groups for atoms in a ring to estimate critical point properties according to Joback 1984"
longDesc = """
Group definitions to estimate critical point properties via group additivity, from:

Joback, K. G. A unified approach to physical property estimation using multivariate statistical techniques,
PhD Thesis, Massachusetts Institute of Technology: Cambridge, MA, 1984.

Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.
"""

</details>

`libraries/GRI-Mech.py`
_none_

<details>
<summary> `libraries/NIST_Fluorine.py` </summary>
name = "NIST_Fluorine"
shortDesc = "NIST Transport library for HFC combustion"
longDesc = """
Valeri I. Babushok, Michael J. Hegetschweiler, Gregory T. Linteris, Donald R. Burgess, Jr., Jeffrey A. Manion, Robert R. Burrell, Michael J. Hegetschweiler
Model for C1-C2 Hydrofluorocarbon (HFC) combustion of refrigerants.

This library is recommendend for C/H/O/F combustion models
"""

</details>

<details>

<summary> `libraries/NOx2018.py` </summary>
name = "NOx2018"
shortDesc = "NOx2018"
longDesc = """
P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002


 Hydrocarbon subset:

H. Hashemi, J.M. Christensen, S. Gersen, H. Levinsky, S.J. Klippenstein, P. Glarborg,
“High-Pressure Oxidation of Methane”, Combust. Flame 172 (2016) 349-364.

J. Gimenez-Lopez, C.T. Rasmussen, H. Hashemi, M.U. Alzueta, Y. Gao, P. Marshall, C.F. Goldsmith, P. Glarborg,
“Experimental and Kinetic Modeling Study of C2H2 Oxidation at High Pressure, Int. J. Chem. Kinet. 48 (2016) 724-738.

H. Hashemi, J.G. Jacobsen, C.T. Rasmussen, J.M. Christensen, P. Glarborg, S. Gersen, M. van Essen, H.B. Levinsky, S.J. Klippenstein, 
“High-Pressure Oxidation of Ethane”, Combust. Flame 182 (2017) 150-166.

 Nitrogen subset

P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002
"""

</details>

<details>
<summary> `libraries/OneDMinN2.py` </summary>
name = "OneDMinN2"
shortDesc = "OneDMinN2"
longDesc = """
A transport library of species calculated using the OneDMin software for N2 as a bath gas.

The citation for OneDMin is:
1. A. W. Jasper and J. A. Miller, "Lennard-Jones parameters for combustion and chemical kinetics modeling from
   full-dimensional intermolecular potentials," Combust. Flame, 161, 101 (2014).
2. A. W. Jasper and J. A. Miller, OneDMin, July 2014.

Listed below are pure-gas A+A Lennard-Jones parameters
LJ Parameters employed a DF-MP2/aug-cc-pVDZ potential energy surface.
Dipole Moment and Polarizability were computed at the B2PLYPD3/cc-pVTZ level

(1) Shape Index, indicating 0 (atom), 1 (linear molecule), or 2 (nonlinear molecule);
(2) Epsilon, the Lennard-Jones well depth, in K; and
(3) Sigma, the Lennard-Jones collision diameter, in Angstrom.
(4) Mu, total dipole moment, in Debye
(5) Alpha, mean static polarizability, in Angstrom^3
(6) Rotational Relacation Collision Number was *NOT* determined, and a default value of 1 is given here!
"""

</details>

`<details>
<summary> libraries/PrimaryTransportLibrary.py` </summary>
name = "primaryTransportLibrary"
shortDesc = ""
longDesc = """

"""

</details>

