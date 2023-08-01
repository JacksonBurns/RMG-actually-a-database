#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_CSm/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index=1,
    label="H + CS <=> CHS",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(20.92, "kJ/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
    longDesc="""
Converted to training reaction from rate rule: CSm;Y_rad
""",
)

entry(
    index=2,
    label="H + CS <=> CHS",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.18e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(11.3386, "kJ/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=11,
    shortDesc="""Guessed from CO+H_rad""",
    longDesc="""
Converted to training reaction from rate rule: CSm;H_rad
""",
)

entry(
    index=3,
    label="CH3 + CS <=> C2H3S",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=2.11,
        Ea=(10.2926, "kJ/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=5,
    shortDesc="""CAC CBS-QB3 calc (using methyl group), HO Approx""",
    longDesc="""
Converted to training reaction from rate rule: CSm;C_methyl
""",
)

entry(
    index=4,
    label="C2H5 + CS <=> C3H5S",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(2.01e10, "cm^3/(mol*s)"),
        n=2.22,
        Ea=(1.63176, "kJ/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=5,
    shortDesc="""CAC CBS-QB3 calc (using ethyl group), HO approx""",
    longDesc="""
Converted to training reaction from rate rule: CSm;CH2CH3
""",
)
