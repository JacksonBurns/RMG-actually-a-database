#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C8H6_H_abstraction"
shortDesc = ""
longDesc = """

"""
autoGenerated = False
entry(
    index=0,
    label="C6H5C2H(7) + H(1) <=> C6H4C2H(8) + H2(2)",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.42e08, "cm^3/(mol*s)"),
        n=1.77,
        Ea=(13.06, "kcal/mol"),
        T0=(1, "K"),
    ),
    longDesc="""
Originally from reaction library: First_to_Second_Aromatic_Ring/H_abstraction
""",
)

entry(
    index=1,
    label="C6H5C2H(7) + CH3(3) <=> C6H4C2H(8) + CH4(4)",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(5150, "cm^3/(mol*s)"),
        n=2.896,
        Ea=(15.31, "kcal/mol"),
        T0=(1, "K"),
    ),
    longDesc="""
Originally from reaction library: First_to_Second_Aromatic_Ring/H_abstraction
""",
)

entry(
    index=2,
    label="C6H5C2H(7) + OH(5) <=> C6H4C2H(8) + H2O(6)",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(23400, "cm^3/(mol*s)"),
        n=2.683,
        Ea=(0.73, "kcal/mol"),
        T0=(1, "K"),
    ),
    longDesc="""
Originally from reaction library: First_to_Second_Aromatic_Ring/H_abstraction
""",
)