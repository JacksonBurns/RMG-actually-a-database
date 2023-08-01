#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=1,
    label="H2CCH3_X + Pt_5 + Pt_6 <=> H2CCH2_2X + H_X",
    degeneracy=3,
    kinetics=SurfaceArrhenius(
        A=(1.163e20, "m^4/(mol^2*s)"),
        n=0.644,
        Ea=(42144.629, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=8,
    shortDesc="""Deutschmann Ni""",
    longDesc="""
Calculated by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal="Pt",
)

entry(
    index=2,
    label="HCCH3_X + Pt_5 + Pt_6 <=> HCCH2_2X + H_X",
    degeneracy=3,
    kinetics=SurfaceArrhenius(
        A=(2.057e20, "m^4/(mol^2*s)"),
        n=0.598,
        Ea=(45301.1, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=8,
    shortDesc="""Default""",
    longDesc="""
Calculated by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal="Pt",
)

entry(
    index=3,
    label="H2CO_2X + H_X <=> H2COH_X + Pt_5 + Pt_6",
    degeneracy=1,
    kinetics=SurfaceArrhenius(
        A=(4.857e16, "m^2/(mol*s)"),
        n=0.063,
        Ea=(28353.5, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=8,
    shortDesc="""Default""",
    longDesc="""
Calculated by Katrín Blöndal at Brown University, using the vdW-DF-cx functional in Quantum ESPRESSO.
""",
    metal="Pt",
)
