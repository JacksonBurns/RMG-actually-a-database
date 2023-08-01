#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=3000,
    label="R_R;YJ",
    kinetics=ArrheniusEP(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        alpha=0,
        E0=(0.5, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
)
