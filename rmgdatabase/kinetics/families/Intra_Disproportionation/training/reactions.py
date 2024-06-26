#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/training"
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
        A=(1.949e11, "s^-1"), n=0.486, Ea=(5.464, "kcal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc="""
Taken from entry: W8 <=> W10
""",
)

entry(
    index=1,
    label="C10H10-3 <=> C10H10-4",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(7.437e08, "s^-1"), n=1.045, Ea=(15.153, "kcal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc="""
Taken from entry: W14 <=> W17
""",
)
