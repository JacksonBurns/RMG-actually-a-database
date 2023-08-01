#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=1,
    label="XSYJ;YJ;S-RR",
    kinetics=ArrheniusEP(
        A=(2e12, "s^-1"),
        n=0,
        alpha=0,
        E0=(20, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
    shortDesc="""A. G. Vandeputte""",
)
