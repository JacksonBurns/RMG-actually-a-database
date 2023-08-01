#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Cyclic_birad_scission/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index=0,
    label="C10H10 <=> C10H10-2",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(3.208e11, "s^-1"), n=0.001, Ea=(25.838, "kcal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc="""
Taken from entry: W4 <=> W8
""",
)

entry(
    index=1,
    label="C10H10-3 <=> C10H10-4",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(5.623e09, "s^-1"), n=0.522, Ea=(43.633, "kcal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc="""
Taken from entry: W2 <=> W14
""",
)
