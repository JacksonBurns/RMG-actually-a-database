#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=0,
    label="RHOO_rad;ROO_rad",
    kinetics=ArrheniusEP(
        A=(2e11, "cm^3/(mol*s)"),
        n=-0.55,
        alpha=0,
        E0=(-1600, "cal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
    longDesc="""

""",
)
