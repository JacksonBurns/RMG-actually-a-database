#!/usr/bin/env python
# encoding: utf-8

name = "lone_electron_pair_bond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=0,
    label="N3sRRR;O_atom_singlet",
    kinetics=ArrheniusEP(
        A=(100000, "cm^3/(mol*s)"),
        n=0,
        alpha=0,
        E0=(100, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
)
