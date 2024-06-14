#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index=0,
    label="HCO + H <=> CO + H2",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(9.03e13, "cm^3/(mol*s)", "*|/", 2),
        n=0,
        Ea=(0, "cal/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(2500, "K"),
    ),
    rank=1,
    shortDesc="""Review and estimation based on experimental results""",
    longDesc="""
p. 519
R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe,
Evaluated Kinetic Data for Combustion Modelling
Journal of Physical and Chemical Reference Data, 1992, 21, 411,
doi: 10.1063/1.555918
""",
)

entry(
    index=1,
    label="HCO + O <=> CO + OH",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(3.01e13, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""FFCM-1""",
    longDesc="""
Taken from the FFCM-1 library
""",
)

entry(
    index=2,
    label="HCO + O2 <=> CO + HO2",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(5.12e13, "cm^3/(mol*s)"), n=0, Ea=(1690, "cal/mol"), T0=(1, "K")
    ),
    rank=1,
    shortDesc="""Review and estimation based on experimental results""",
    longDesc="""
p. 1147, rxn (15,3)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index=3,
    label="HCO + CH3 <=> CO + CH4",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "cal/mol"),
        T0=(1, "K"),
        Tmin=(1004, "K"),
        Tmax=(1006, "K"),
    ),
    rank=1,
    shortDesc="""Shock Tube""",
    longDesc="""
p. 4131, Table 1, rxn [16]
reported at 1005 K (value is anyway T-independent)
A.M. Held, K.C. Manthorne, P.D. Pacey, H.P. Reinholdt,
Canadian Journal of Chemistry, 1977, 55(23), 4128-4134
doi: 10.1139/v77-585
""",
)

entry(
    index=4,
    label="HCO + CH3O <=> CO + CH3OH",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(9.03e13, "cm^3/(mol*s)", "*|/", 3),
        n=0,
        Ea=(0, "cal/mol"),
        T0=(1, "K"),
    ),
    rank=1,
    shortDesc="""Review and estimation based on experimental results""",
    longDesc="""
p. 1246, rxn (24,15)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index=5,
    label="HCO + HCO_Y <=> CO + CH2O",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.8e13, "cm^3/(mol*s)", "+|-", 9e12),
        n=0,
        Ea=(0, "cal/mol"),
        T0=(1, "K"),
    ),
    rank=1,
    shortDesc="""Review and estimation based on experimental results""",
    longDesc="""
p. 1151, rxn (15,15 a)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index=6,
    label="HCO + C2H3 <=> CO + C2H4",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(9.033e13, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")
    ),
    rank=5,
    shortDesc="""JetSurF2.0""",
    longDesc="""
Taken from the JetSurF2.0 library
""",
)

entry(
    index=7,
    label="HCO + nC3H7 <=> CO + C3H8_n",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(6e13, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")),
    rank=5,
    shortDesc="""JetSurF2.0""",
    longDesc="""
Taken from the JetSurF2.0 library
""",
)

entry(
    index=8,
    label="HCO + iC3H7 <=> CO + C3H8_i",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1.2e14, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")),
    rank=5,
    shortDesc="""JetSurF2.0""",
    longDesc="""
Taken from the JetSurF2.0 library
""",
)

entry(
    index=9,
    label="HCO + NO <=> CO + HNO",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(7.1e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "cal/mol"),
        T0=(1, "K"),
        Tmin=(300, "K"),
        Tmax=(2500, "K"),
    ),
    rank=1,
    shortDesc="""Shock Tube""",
    longDesc="""
p. 4180, Table 2, rxn 1
J. Dammeier , M. Colberg, G. Friedrichs,
Phys. Chem. Chem. Phys., 2007, 9, 4177-4188
doi: 10.1039/B704197G

[Also available from: Z.F. Xu, C.-H. Hsu, M.C. Lin, J. Chem. Phys., 2005, 122, 234308, doi: 10.1063/1.1917834
calculations done at the G2M(CC5)//B3LYP/6-311G(d, p) level of theory
T ranges: 200-500 & 500-3000 K]
""",
)

entry(
    index=10,
    label="HCO + NO2 <=> CO + HONO",
    degeneracy=1.0,
    kinetics=Arrhenius(
        A=(1.24e23, "cm^3/(mol*s)"),
        n=-3.29,
        Ea=(2355, "cal/mol"),
        T0=(1, "K"),
        Tmin=(1140, "K"),
        Tmax=(1650, "K"),
    ),
    rank=1,
    shortDesc="""Shock Tube""",
    longDesc="""
p. 463, Table II, rxn 2
C-Y. Lin, H-T. Wang, M.C. Lin, C.F. Melius,
Int. J. Chem. Kin, 1990, 22(5), 455-482
doi: 10.1002/kin.550220504
""",
)

entry(
    index=11,
    label="CH2OH + HCO <=> CH3OH + CO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1e13, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")),
    rank=1,
    shortDesc="""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.10183""",
)

entry(
    index=12,
    label="C2H5 + HCO <=> C2H6 + CO",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(4.3e13, "cm^3/(mol*s)"), n=0, Ea=(0, "cal/mol"), T0=(1, "K")),
    rank=1,
    shortDesc="""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/j100296a057""",
)