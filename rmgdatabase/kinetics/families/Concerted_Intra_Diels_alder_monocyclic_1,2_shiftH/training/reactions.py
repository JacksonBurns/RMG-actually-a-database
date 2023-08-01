#!/usr/bin/env python
# encoding: utf-8

name = "Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH/training"
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
        A=(2.65505e13, "s^-1"),
        n=-0.215087,
        Ea=(217.397, "kJ/mol"),
        T0=(1, "K"),
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc="""
Taken from entry: VIII <=> IX
""",
)
