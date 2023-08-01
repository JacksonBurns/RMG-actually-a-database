#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index=826,
    label="RnOOH;Y_rad_out",
    kinetics=ArrheniusEP(
        A=(1e10, "s^-1"),
        n=0,
        alpha=0,
        E0=(15, "kcal/mol"),
        Tmin=(300, "K"),
        Tmax=(1500, "K"),
    ),
    rank=0,
)
