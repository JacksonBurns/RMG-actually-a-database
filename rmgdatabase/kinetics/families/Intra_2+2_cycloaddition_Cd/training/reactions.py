#!/usr/bin/env python
# encoding: utf-8

name = "Intra_2+2_cycloaddition_Cd/training"
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
        A=(4.99998e11, "s^-1"),
        n=0.0559095,
        Ea=(122.413, "kJ/mol"),
        T0=(1, "K"),
    ),
    rank=5,
    shortDesc="""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc="""
Taken from entry: II <=> III
""",
)

entry(
    index=1,
    label="C4H6_BD <=> C4H6_CB",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.70652e13, "s^-1"), n=-0.361171, Ea=(187.676, "kJ/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc="""
Calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)
