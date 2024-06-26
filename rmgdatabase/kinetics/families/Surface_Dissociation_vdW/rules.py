#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/rules"
shortDesc = ""
longDesc = """
"""

entry(
    index=1,
    label="Combined;VacantSite",
    kinetics=SurfaceArrheniusBEP(
        A=(4.879e15, "m^2/(mol*s)"),
        n=0,
        alpha=0.6,
        E0=(10.8384576, "kcal/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
    longDesc="""
Reaction 30 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
E0 is Ea

A factor from paper / surface site density of Cu
1.436e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.879e15 m^2/(mol*s)
""",
)
