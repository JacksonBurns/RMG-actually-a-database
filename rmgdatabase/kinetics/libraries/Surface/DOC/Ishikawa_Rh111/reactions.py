#!/usr/bin/env python
# encoding: utf-8

name = "Ishikawa_Rh111"
shortDesc = ""
longDesc = """
This library is built to import training reactions, based on:
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906
"""

entry(
    index=1,
    label="NO_X + X <=> N_X + O_X",
    kinetics=SurfaceArrhenius(
        A=(8.19e19, "cm^2/(mol*s)"),
        n=1.009,
        Ea=(76196, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""NO Dissociation""",
    longDesc="""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal="Rh",
    facet="111",
)

entry(
    index=2,
    label="NO_X + O_X <=> NO2_X + X",
    kinetics=SurfaceArrhenius(
        A=(6.52e19, "cm^2/(mol*s)"),
        n=1.015,
        Ea=(155285, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation""",
    longDesc="""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal="Rh",
    facet="111",
)

entry(
    index=3,
    label="N_X + N_X <=> N2 + X + X",
    kinetics=SurfaceArrhenius(
        A=(1.43e20, "cm^2/(mol*s)"),
        n=1.012,
        Ea=(171681, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""N2 Surface_Adsorption_Dissociative""",
    longDesc="""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal="Rh",
    facet="111",
)

entry(
    index=4,
    label="N2O_X + X <=> N2_X + O_X",
    kinetics=SurfaceArrhenius(
        A=(9.12e19, "cm^2/(mol*s)"),
        n=1.004,
        Ea=(63657, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation_Double_vdW""",
    longDesc="""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal="Rh",
    facet="111",
)

entry(
    index=5,
    label="CO_X + O_X <=> CO2_X + X",
    kinetics=SurfaceArrhenius(
        A=(1.73e20, "cm^2/(mol*s)"),
        n=1.001,
        Ea=(119598, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation_Double_vdW""",
    longDesc="""
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal="Rh",
    facet="111",
)
