#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Diels_alder_monocyclic/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index=0,
    label="C6H6 <=> C6H6-2",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(3.18043e12, "s^-1"),
        n=-0.303917,
        Ea=(156.176, "kJ/mol"),
        T0=(1, "K"),
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc="""
Taken from entry: VIII <=> X
""",
)

entry(
    index=1,
    label="C6H6-3 <=> C6H6-4",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.012e13, "s^-1"), n=0.1, Ea=(41.203, "kcal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc="""
Taken from entry: IV <=> B
""",
)
