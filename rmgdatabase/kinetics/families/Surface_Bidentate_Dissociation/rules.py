#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/rules"
shortDesc = ""
longDesc = """
"""
entry(
    index=1,
    label="Combined",
    kinetics=SurfaceArrheniusBEP(
        A=(1.187e12, "1/s"),
        n=0.0,
        alpha=0.842,
        E0=(34.82, "kcal/mol"),
        Tmin=(200, "K"),
        Tmax=(3000, "K"),
    ),
    rank=0,
    shortDesc="""Default""",
    longDesc="""
A and n factors are averages of training reactions 1-3 and the reverse direction of training reactions 4-7, 
and alpha and E0 are BEP parameters from training reactions 1-3 and the reverse of training reactions 4-7.
""",
)
