#!/usr/bin/env python
# encoding: utf-8

name = "Mebel_Naphthyl"
shortDesc = ""
longDesc = """
Reactions of naphthyl-1 and naphthyl-2+H=C10H8 from L. B. Harding, Y. Georgievskii, S. J. Klippenstein, Predictive theory for hydrogen-atom
hydrocarbon radical association kinetics, J. Phys. Chem. A. ,2005, 109, 4646-4656
Remaining reactions from A. M. Mebel, Y. Georgievskii, A. W. Jasper, S. J. Klippenstein, Temperature and pressure dependent rate coefficients 
for the HACA pathways from benzene to naphthalene, Proceedings of the Combust. Inst. (2016) 1-8
"""
entry(
    index=1,
    label="C6H4C2H + C2H2 <=> naphthyl-1",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(2.88e97, "cm^3/(mol*s)"),
                n=-24.74,
                Ea=(55080, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.49e82, "cm^3/(mol*s)"),
                n=-20.02,
                Ea=(51830, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.39e77, "cm^3/(mol*s)"),
                n=-18.2,
                Ea=(55590, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.05e63, "cm^3/(mol*s)"),
                n=-13.85,
                Ea=(50610, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=2,
    label="C6H4C2H + C2H2 <=> benzofulvenyl",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(2.71e35, "cm^3/(mol*s)"),
                n=-7.778,
                Ea=(10640, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.81e42, "cm^3/(mol*s)"),
                n=-9.437,
                Ea=(16890, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(3.07e51, "cm^3/(mol*s)"),
                n=-11.5,
                Ea=(26120, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.72e31, "cm^3/(mol*s)"),
                n=-5.453,
                Ea=(16910, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=3,
    label="C6H4C2H + C2H2 <=> naphthyl-2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(8.87e104, "cm^3/(mol*s)"),
                n=-26.75,
                Ea=(62780, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.18e104, "cm^3/(mol*s)"),
                n=-25.7,
                Ea=(76820, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.01e98, "cm^3/(mol*s)"),
                n=-23.65,
                Ea=(85700, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(9.45e78, "cm^3/(mol*s)"),
                n=-17.82,
                Ea=(83270, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=4,
    label="C6H4C2H + C2H2 <=> C6H4(C2H)2 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(1.47e34, "cm^3/(mol*s)"),
                n=-5.51,
                Ea=(38260, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.76e40, "cm^3/(mol*s)"),
                n=-7.036,
                Ea=(48210, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.82e28, "cm^3/(mol*s)"),
                n=-3.775,
                Ea=(42120, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.5e17, "cm^3/(mol*s)"),
                n=-0.635,
                Ea=(35600, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=5,
    label="C6H4C2H + C2H2 <=> naphthyne-12 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(8.5e53, "cm^3/(mol*s)"),
                n=-11.31,
                Ea=(44760, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(3.87e64, "cm^3/(mol*s)"),
                n=-13.98,
                Ea=(62560, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(9.6e62, "cm^3/(mol*s)"),
                n=-13.32,
                Ea=(70290, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.08e52, "cm^3/(mol*s)"),
                n=-10.12,
                Ea=(71290, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=6,
    label="C6H4C2H + C2H2 <=> naphthyne-23 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(6.38e60, "cm^3/(mol*s)"),
                n=-13.28,
                Ea=(51290, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(9.25e72, "cm^3/(mol*s)"),
                n=-16.3,
                Ea=(72450, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.23e83, "cm^3/(mol*s)"),
                n=-18.74,
                Ea=(94140, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.42e74, "cm^3/(mol*s)"),
                n=-15.94,
                Ea=(103210, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=7,
    label="C6H4(C2H)2 + H <=> naphthyl-1",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(1.39e99, "cm^3/(mol*s)"),
                n=-24.84,
                Ea=(58630, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.01e86, "cm^3/(mol*s)"),
                n=-20.6,
                Ea=(56700, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.02e80, "cm^3/(mol*s)"),
                n=-18.53,
                Ea=(59600, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.14e64, "cm^3/(mol*s)"),
                n=-13.83,
                Ea=(53190, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=8,
    label="C6H4(C2H)2 + H <=> benzofulvenyl",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(3.33e39, "cm^3/(mol*s)"),
                n=-8.608,
                Ea=(14700, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(5.3e46, "cm^3/(mol*s)"),
                n=-10.19,
                Ea=(21350, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(7.37e53, "cm^3/(mol*s)"),
                n=-11.84,
                Ea=(29570, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.45e37, "cm^3/(mol*s)"),
                n=-6.855,
                Ea=(23570, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=9,
    label="C6H4(C2H)2 + H <=> naphthyl-2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(3.71e109, "cm^3/(mol*s)"),
                n=-27.64,
                Ea=(69300, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6e108, "cm^3/(mol*s)"),
                n=-26.63,
                Ea=(83590, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.64e102, "cm^3/(mol*s)"),
                n=-24.46,
                Ea=(92100, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.35e82, "cm^3/(mol*s)"),
                n=-18.42,
                Ea=(88860, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=10,
    label="C6H4(C2H)2 + H <=> naphthyne-12 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(4.94e59, "cm^3/(mol*s)"),
                n=-12.55,
                Ea=(52170, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(7.29e69, "cm^3/(mol*s)"),
                n=-15.09,
                Ea=(69850, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.08e67, "cm^3/(mol*s)"),
                n=-14.29,
                Ea=(77310, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.16e55, "cm^3/(mol*s)"),
                n=-10.81,
                Ea=(77390, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=11,
    label="C6H4(C2H)2 + H <=> naphthyne-23 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(5.06e67, "cm^3/(mol*s)"),
                n=-14.83,
                Ea=(59750, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.32e79, "cm^3/(mol*s)"),
                n=-17.63,
                Ea=(80720, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.08e88, "cm^3/(mol*s)"),
                n=-19.94,
                Ea=(102250, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.59e79, "cm^3/(mol*s)"),
                n=-16.97,
                Ea=(110840, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=12,
    label="naphthyne-12 + H <=> naphthyl-1",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(2.92e83, "cm^3/(mol*s)"),
                n=-19.93,
                Ea=(44880, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.27e67, "cm^3/(mol*s)"),
                n=-15.15,
                Ea=(38580, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(3.22e49, "cm^3/(mol*s)"),
                n=-9.959,
                Ea=(26820, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(5.33e34, "cm^3/(mol*s)"),
                n=-5.755,
                Ea=(16810, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=13,
    label="naphthyne-12 + H <=> benzofulvenyl",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(3.82e50, "cm^3/(mol*s)"),
                n=-10.99,
                Ea=(25200, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(3.81e61, "cm^3/(mol*s)"),
                n=-13.54,
                Ea=(41180, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.58e69, "cm^3/(mol*s)"),
                n=-15.3,
                Ea=(55910, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.84e45, "cm^3/(mol*s)"),
                n=-8.142,
                Ea=(48480, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=14,
    label="naphthyne-12 + H <=> naphthyl-2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(4.76e85, "cm^3/(mol*s)"),
                n=-20.55,
                Ea=(46410, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.9e72, "cm^3/(mol*s)"),
                n=-16.43,
                Ea=(42280, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.25e49, "cm^3/(mol*s)"),
                n=-9.89,
                Ea=(27060, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.01e25, "cm^3/(mol*s)"),
                n=-3.125,
                Ea=(9500, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=15,
    label="naphthyne-12 + H <=> naphthyne-23 + H",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(5.37e63, "cm^3/(mol*s)"),
                n=-13.24,
                Ea=(57380, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.8e58, "cm^3/(mol*s)"),
                n=-11.59,
                Ea=(62910, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.15e48, "cm^3/(mol*s)"),
                n=-8.496,
                Ea=(62020, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.73e30, "cm^3/(mol*s)"),
                n=-3.493,
                Ea=(54590, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=16,
    label="naphthyne-23 + H <=> naphthyl-1",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(1.16e103, "cm^3/(mol*s)"),
                n=-25.18,
                Ea=(63330, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.12e103, "cm^3/(mol*s)"),
                n=-24.5,
                Ea=(77920, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(1.19e98, "cm^3/(mol*s)"),
                n=-22.7,
                Ea=(85620, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.74e67, "cm^3/(mol*s)"),
                n=-14.05,
                Ea=(68970, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=17,
    label="naphthyne-23 + H <=> benzofulvenyl",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(8.39e82, "cm^3/(mol*s)"),
                n=-19.82,
                Ea=(51820, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.41e86, "cm^3/(mol*s)"),
                n=-20.17,
                Ea=(68230, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(9.14e99, "cm^3/(mol*s)"),
                n=-23.28,
                Ea=(93130, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.12e56, "cm^3/(mol*s)"),
                n=-10.77,
                Ea=(74870, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=18,
    label="naphthyne-23 + H <=> naphthyl-2",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.0395, 1, 10, 100], "atm"),
        arrhenius=[
            Arrhenius(
                A=(1.25e86, "cm^3/(mol*s)"),
                n=-20.69,
                Ea=(43640, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(6.32e78, "cm^3/(mol*s)"),
                n=-18.22,
                Ea=(44420, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(2.62e56, "cm^3/(mol*s)"),
                n=-11.76,
                Ea=(30610, "cal/mol"),
                T0=(1, "K"),
            ),
            Arrhenius(
                A=(4.86e26, "cm^3/(mol*s)"),
                n=-3.385,
                Ea=(9000, "cal/mol"),
                T0=(1, "K"),
            ),
        ],
    ),
)

entry(
    index=19,
    label="naphthyl-1 + H <=> C10H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.87e13, "cm^3/(mol*s)"), n=0.13, Ea=(0, "cal/mol"), T0=(1, "K")
    ),
)

entry(
    index=20,
    label="naphthyl-2 + H <=> C10H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.26e13, "cm^3/(mol*s)"), n=0.17, Ea=(0, "cal/mol"), T0=(1, "K")
    ),
)
