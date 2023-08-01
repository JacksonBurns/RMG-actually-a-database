#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/rules"
shortDesc = ""
longDesc = """
Surface adsorption of a single radical forming a single bond to the surface site
"""
entry(
    index=1,
    label="Adsorbate;VacantSite",
    kinetics=StickingCoefficientBEP(
        A=0.1,
        n=0,
        alpha=0,
        E0=(0, "kcal/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
    longDesc="""Made up""",
)
