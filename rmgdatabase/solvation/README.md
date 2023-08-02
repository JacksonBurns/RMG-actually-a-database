Directory Contents:
 - `solvation_files.tar.xz`: the original data files contained in RMG-database, tarballed and compressed. Decompress and un-tar with `tar -xf solvation_files.tar.xz`.
 - `make_solvation_table.py`: reads through all the files from the uncompressed directories and flattens them into a database using `peewee`.
 - `solvation.db`: flattened, relational database-version of the original contents of this directory.

Descriptions of Groups and Libraries from the file headers:

<details>
<summary> `libraries/solute.py` </summary>

name = "Solute Descriptors"
shortDesc = ""
longDesc = """
From Abarahm et al., J. Chem. Soc., Perkin Trans. 2, 1994, 1777-1791, DOI: 10.1039/P29940001777
or from in-house database received from Prof. Abraham
"""

</details>

<details>
<summary> `libraries/solvent.py` </summary>

name = "Solvent Descriptors"
shortDesc = ""
longDesc = """
Most of the Abraham (s_g, b_g, e_g, l_g, a_g, c_g) and Mintz solvent parameters (s_h, b_h, e_h, l_h, a_h, c_h) 
are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter, solvation free energy, 
and solvation enthalpy data (manuscript in preparation). Abraham solvent parameters are used for solvation 
free energy (dGsolv) calculations, and Mintz solvent parameters are used for solvation enthalpy (dHsolv) calculations.

The majority of the viscosity parameters (A, B, C, D, E) are obtained from:
    Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K., Rani, K. Y. (2007) Viscosity of Liquids.
    Springer, The Netherlands: Dordrecht.
The rest of the viscosity parameters are found from the DIPPR.

'alpha' and 'beta' are the SOLUTE parameters A and B that can be potentially used for intrinsic rate correction 
in H-abstraction rxns. But these parameters are currently not used in RMG.

'eps' is the dielectric constant of a solvent. It is currently not used in RMG.

'name_in_coolprop' represents the solvent's name used in the external package CoolProp. CoolProp is used for
fluid property calculation. If the solvent is not available in CoolProp, 'name_in_coolprop' is set to None.

'dataCount' stores the information on the number of data used to fit the Abraham and Mintz solvent parameters and 
their associated solvation free energy and solvation enthalpy mean absolute error (MAE).

Reference legend:
[Abraham2012] The hydrogen bond properties of water from 273 K to 573 K; equations for the prediction of gas-water partition coefficients Michael H. Abraham and William E. Acree Jr Phys. Chem. Chem. Phys., 2012,14, 7433–7440
[Abraham2016] Equations for the Partition of Neutral Molecules, Ionsand Ionic Species from Water to Water–MethanolMixtures Michael H. Abraham and William E. Acree Jr J Solution Chem (2016) 45:861–874
[Gagliardi2007] Static Dielectric Constants of Acetonitrile/Water Mixtures at Different Temperatures and Debye−Huckel A and a0B Parameters for Activity Coefficients Leonardo G. Gagliardi, Cecilia B. Castells, Clara Rafols, Marti Roses and, and Elisabeth Bosch, Journal of Chemical & Engineering Data 2007 52 (3), 1103-1107 DOI: 10.1021/je700055p
[JIRKAL2016] Application of Solvation Model to Prediction of the Solute Retention in Liquid Chromatography over a Wide Range of Mobile-Phase Compositions S. JIRKAL, M. MACHOVCOVA, AND J.G.K. SEVCIK DOI: 10.1556/1326.2016.28.1.06
[Mohsen-Nia2012] Measurement and modelling of static dielectric constants of aqueous solutions of methanol, ethanol and acetic acid at T = 293.15 K and 91.3 kPa M.Mohsen-Nia, H.Amiria https://doi.org/10.1016/j.jct.2012.08.009
"""

</details>


<details>
<summary> `groups/abraham.py` </summary>

name = "Abraham Solute Descriptors"
shortDesc = ""
longDesc = """

"""

</details>


<details>
<summary> `groups/group.py` </summary>

name = "group"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>


<details>
<summary> `groups/halogen.py` </summary>

name = "halogen"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>


<details>
<summary> `groups/longDistanceInteraction_cyclic.py` </summary>

name = "longDistanceInteraction_cyclic"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>


<details>
<summary> `groups/longDistanceInteraction_noncyclic.py` </summary>

name = "longDistanceInteraction_noncyclic"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>


<details>
<summary> `groups/nonacentered.py` </summary>

name = "Non Atom Centered Platts Groups"
shortDesc = ""
longDesc = """

"""

</details>


<details>
<summary> `groups/polycyclic.py` </summary>

name = "polycyclic"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>


<details>
<summary> `groups/radical.py` </summary>

name = "Radical Groups"
shortDesc = "Radical corrections to A"
longDesc = """
H-bonding parameter A should be modified for when we saturate 
radical molecules with hydrogens and look up the saturated
structure.
"""

</details>


<details>
<summary> `groups/ring.py` </summary>

name = "ring"
shortDesc = ""
longDesc = """ 
All groups are fitted by Yunsie Chung and Pierre Walker using experimental solute parameter data (manuscript in preparation)
unless written otherwise.
"""

</details>
