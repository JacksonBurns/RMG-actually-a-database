#!/usr/bin/env python
# encoding: utf-8

name = "Offermans_Pt111"
shortDesc = ""
longDesc = """
This library is built to import training reactions, based on:
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067
"""

entry(
    index=1,
    label="N_X + N_X <=> N2 + X + X",
    kinetics=SurfaceArrhenius(
        A=(3.46e21, "cm^2/(mol*s)"),
        n=0,
        Ea=(4000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""N2 Surface_Adsorption_vdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K from p.62)= 8.6E12(1/s)/2.483E-9(mol/cm^2) = 3.46E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=2,
    label="NH3_X + X <=> NH2_X + H_X",
    kinetics=SurfaceArrhenius(
        A=(2.26e20, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(93000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation_vdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K)= 5.6E11(1/s)/2.483E-9(mol/cm^2) = 2.25E20 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=3,
    label="NH2_X + X <=> NH_X + H_X",
    kinetics=SurfaceArrhenius(
        A=(2.01e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(110000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.0E12(1/s)/2.483E-9(mol/cm^2) = 2.01E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=4,
    label="NH_X + X <=> N_X + H_X",
    kinetics=SurfaceArrhenius(
        A=(2.90e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(118000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Dissociation""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.2E12(1/s)/2.483E-9(mol/cm^2) = 2.90E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=5,
    label="NH3_X +O_X <=> NH2_X + OH_X",
    kinetics=SurfaceArrhenius(
        A=(4.83e20, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(42000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Abstraction_vdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.2E12(1/s)/2.483E-9(mol/cm^2) = 4.83E20 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=6,
    label="NH2_X +O_X <=> NH_X + OH_X",
    kinetics=SurfaceArrhenius(
        A=(2.46e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(87000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Abstraction""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 6.1E12(1/s)/2.483E-9(mol/cm^2) = 2.46E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=7,
    label="NH_X + O_X <=> N_X + OH_X",
    kinetics=SurfaceArrhenius(
        A=(3.06e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(84000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Abstraction""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.6E12(1/s)/2.483E-9(mol/cm^2) = 3.06E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=8,
    label="NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics=SurfaceArrhenius(
        A=(6.44e19, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(73000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Abstraction_Single_vdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.6E11(1/s)/2.483E-9(mol/cm^2) = 6.44E19 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=9,
    label="NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics=SurfaceArrhenius(
        A=(1.37e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(22000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_Abstraction_vdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 3.4E12(1/s)/2.483E-9(mol/cm^2) = 1.37E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=10,
    label="NH_X + OH_X <=> N_X + H2O_X",
    kinetics=SurfaceArrhenius(
        A=(2.05e20, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(35000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Surface_AbstractionvdW""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.1E11(1/s)/2.483E-9(mol/cm^2) = 2.05E20 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index=11,
    label="N_X + O_X <=> NO_X + X",
    kinetics=SurfaceArrhenius(
        A=(2.86e21, "cm^2/(mol*s)"),
        n=0.0,
        Ea=(1000, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    shortDesc="""Nitrogen/51""",
    longDesc="""
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.1E12(1/s)/2.483E-9(mol/cm^2) = 2.86E21 cm^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)
