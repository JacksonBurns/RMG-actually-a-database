#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=24,
    label="CH2X_1 + HOX_3 <=> CH3X_4 + OX_5",
    degeneracy=1,
    kinetics=SurfaceArrhenius(
        A=(1.39e17, "m^2/(mol*s)"),
        n=0.101,
        Ea=(19000.0, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=3,
    shortDesc="""Deutschmann Ni""",
    longDesc="""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R24
""",
    metal="Ni",
)

entry(
    index=26,
    label="CHX_1 + HOX_3 <=> CH2X_4 + OX_5",
    degeneracy=1,
    kinetics=SurfaceArrhenius(
        A=(4.40e18, "m^2/(mol*s)"),
        n=0.101,
        Ea=(42400.0, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=3,
    shortDesc="""Default""",
    longDesc="""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R26
""",
    metal="Ni",
)

# Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R28.
# entry(
#    index = 27,
#    label = "OX_5 + CHX_4 <=> HOX_3 + CX_1 ",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(2.47E17, 'm^2/(mol*s)'),
#        n = 0.312,
#        Ea=(57700.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    #rank = 3,
#    shortDesc = u"""Default""",
#    longDesc = u"""
# "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
# Delgado et al
# Catalysts, 2015, 5, 871-904. Reaction R27
# """,
#    metal = "Ni",
# )

entry(
    index=28,
    label="HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy=1,
    kinetics=SurfaceArrhenius(
        A=(2.43e17, "m^2/(mol*s)"),
        n=-0.312,
        Ea=(118900.0, "J/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=3,
    shortDesc="""Default""",
    longDesc="""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
    metal="Ni",
)

entry(
    index=39,
    label="O* + HCO* <=> OH* + CO*",
    degeneracy=1,
    kinetics=SurfaceArrhenius(
        A=(3.298e17, "m^2/(mol*s)"),
        n=0.0,
        Ea=(0.0, "kcal/mol"),
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    rank=1,
    shortDesc="""Default""",
    longDesc="""
Reaction 39 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.298e17 m^2/(mol*s)
""",
    metal="Cu",
)
