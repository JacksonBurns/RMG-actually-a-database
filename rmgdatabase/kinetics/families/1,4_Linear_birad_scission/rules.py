#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=1,
    label="RJJ",
    kinetics=ArrheniusEP(
        A=(5e12, "s^-1"),
        n=0,
        alpha=0,
        E0=(0, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=10,
    shortDesc="""AG Vandeputte estimate (should be fast)""",
)