#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=5,
    label="H2O + X <=> H2OX",
    kinetics=StickingCoefficient(
        A=1.0e-1,
        n=0,
        Ea=(0, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=10,
    shortDesc="""Default""",
    longDesc="""R5
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
    metal="Ni",
)

entry(
    index=7,
    label="CO2 + X <=> CO2X",
    kinetics=StickingCoefficient(
        A=7.0e-6,
        n=0,
        Ea=(0, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=10,
    shortDesc="""Default""",
    longDesc="""R7
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
    metal="Ni",
)

entry(
    index=11,
    label="CH4 + X <=> CH4X",
    kinetics=StickingCoefficient(
        A=8.0e-3,
        n=0,
        Ea=(0, "J/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=10,
    shortDesc="""Default""",
    longDesc="""R11
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
    metal="Ni",
)
