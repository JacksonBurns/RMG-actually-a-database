#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_cyclization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=1,
    label="XSYJ;YJ;Cs;S",
    kinetics=ArrheniusEP(
        A=(1e12, "s^-1"),
        n=0,
        alpha=0,
        E0=(50, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""Aaron Vandeputte CBS-QB3 HO""",
)
