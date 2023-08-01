#!/usr/bin/env python
# encoding: utf-8

name = "surfaceThermoNi111"
shortDesc = "Surface adsorbates on Ni(111)"
longDesc = """
A few surface species adsorbed on Ni(111),
largely estimated by Franklin Goldsmith
"""


entry(
    index=1,
    label="*",
    molecule="""
1 X u0 p0 c0
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
    #        H298 = (0,'kcal/mol'),
    #        S298 = (0,'cal/(mol*K)'),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[0.0, 0, 0, 0, 0, 0.0, 0.0], Tmin=(298, "K"), Tmax=(1000, "K")
            ),
            NASAPolynomial(
                coeffs=[0.0, 0, 0, 0, 0, 0.0, 0.0], Tmin=(1000, "K"), Tmax=(2000, "K")
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""library value for a vacant surface site""",
    longDesc="""Zeros, by definition.""",
    metal="Ni",
    facet="111",
)

entry(
    index=2,
    label="H*",
    molecule="""
1 H u0 p0 {2,S}
2 X u0 p0 {1,S}
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([1.50, 2.58, 3.40, 4.00, 4.73, 5.13, 5.57],'cal/(mol*K)'),
    #        H298 = (-11.26,'kcal/mol','+|-',0.1),
    #        S298 = (0.44,'cal/(mol*K)','+|-',0.1),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.01510910e00,
                    1.27747196e-02,
                    -1.36892852e-05,
                    6.67076880e-09,
                    -1.15946694e-12,
                    -5.53052906e03,
                    8.44686890e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    -1.84968995e-01,
                    6.05229805e-03,
                    -4.83715532e-06,
                    1.81340221e-09,
                    -2.61948776e-13,
                    -5.91533033e03,
                    -5.04191778e-01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""H atom adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=3,
    label="C*",
    molecule="""
1 C u0 p0 {2,Q}
2 X u0 p0 {1,Q}
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([4.04, 4.73, 5.12, 5.35, 5.60, 5.73, 5.85],'cal/(mol*K)'),
    #        H298 = (29.89,'kcal/mol','+|-',0.1),
    #        S298 = (2.62,'cal/(mol*K)','+|-',0.1),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -5.73265619e-01,
                    1.44803183e-02,
                    -2.45704673e-05,
                    1.93668551e-08,
                    -5.81642502e-12,
                    1.47661073e04,
                    1.20244250e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.71617577e00,
                    1.99967762e-05,
                    3.48031630e-07,
                    -2.47205634e-10,
                    5.00169813e-14,
                    1.41308872e04,
                    -1.44477318e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""C atom adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC.
    Unsure of adjacency list: Do we want a lone pair and triple bond?!""",
    metal="Ni",
    facet="111",
)

entry(
    index=4,
    label="O*",
    molecule="""
1 O u0 p2 {2,D}
2 X u0 p0 {1,D}
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([4.52, 5.06, 5.35, 5.52, 5.70, 5.79, 5.88],'cal/(mol*K)'),
    #        H298 = (-52.58,'kcal/mol','+|-',0.1),
    #        S298 = (3.61,'cal/(mol*K)','+|-',0.1),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.95855852e-01,
                    1.16923252e-02,
                    -2.02271203e-05,
                    1.61601691e-08,
                    -4.90070914e-12,
                    -2.69189243e04,
                    -2.01768707e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.90438370e00,
                    -2.74871763e-04,
                    5.38558858e-07,
                    -3.03946989e-10,
                    5.63969783e-14,
                    -2.74411389e04,
                    -1.48944150e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""O atom adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=5,
    label="H2*",
    molecule="""
1 H u0 p0 {2,S} {3,vdW}
2 H u0 p0 {1,S}
3 X u0 p0 {1,vdW}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.69073030e00,
                    1.56595045e-03,
                    -3.19654406e-06,
                    2.88277763e-09,
                    -8.73556269e-13,
                    -2.15972248e03,
                    -1.15931806e01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.49468701e00,
                    -1.73352628e-03,
                    1.97119900e-06,
                    -7.70127035e-10,
                    1.07125350e-13,
                    -2.31943201e03,
                    -1.54586471e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""H2 physisorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=6,
    label="CH*",
    molecule="""
1 C u0 p0 {2,S} {3,T}
2 H u0 p0 {1,S}
3 X u0 p0 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.44067538e-01,
                    7.15965809e-03,
                    -6.05381899e-06,
                    4.41670377e-09,
                    -1.57758787e-12,
                    2.48409325e03,
                    -2.97930741e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.70984781e-01,
                    6.44724983e-03,
                    -3.18677769e-06,
                    7.11925015e-10,
                    -5.43593812e-14,
                    2.47924869e03,
                    -3.03223839e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=7,
    label="CH2*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {4,D}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,D}
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([5.82, 7.37, 8.64, 9.69, 11.35, 12.64, 14.74],'cal/(mol*K)'),
    #        H298 = (4.11,'kcal/mol','+|-',0.1),
    #        S298 = (4.28,'cal/(mol*K)','+|-',0.1),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -7.19249342e-01,
                    1.65071735e-02,
                    -1.74998510e-05,
                    1.09676908e-08,
                    -2.88981251e-12,
                    1.68411050e03,
                    2.01831094e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.83780574e-01,
                    8.78623452e-03,
                    -4.38766259e-06,
                    1.09400822e-09,
                    -1.10409266e-13,
                    1.38336061e03,
                    -5.98458146e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH2 adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=8,
    label="CH3*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S}
""",
    #    thermo = ThermoData(
    #        Tdata = ([300,400,500,600,800,1000,1500],'K'),
    #        Cpdata = ([9.57,11.53,13.02,14.19,16.03,17.47,19.94],'cal/(mol*K)'),
    #        H298 = (-7.32,'kcal/mol','+|-',0.1),
    #        S298 = (8.06,'cal/(mol*K)','+|-',0.1),
    #    ),
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -5.52219087e-01,
                    2.64420133e-02,
                    -3.55617257e-05,
                    2.60043628e-08,
                    -7.52706787e-12,
                    -4.43346585e03,
                    6.92144274e-01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.62557353e00,
                    7.39511955e-03,
                    -2.43797398e-06,
                    1.86159414e-10,
                    3.64849549e-14,
                    -5.18722188e03,
                    -1.89668272e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""Methyl adsorbed on nickle""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=9,
    label="CH4*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S} {6,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 H u0 p0 {1,S}
6 X u0 p0 {1,vdW}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.32887778e00,
                    -5.00781929e-03,
                    2.79052442e-05,
                    -2.68118150e-08,
                    8.62124183e-12,
                    -9.68331332e03,
                    -5.81051526e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    -1.60598709e00,
                    1.64084653e-02,
                    -9.05813323e-06,
                    2.60602815e-09,
                    -3.14643586e-13,
                    -8.70274862e03,
                    1.77717514e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH4 physisorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)


entry(
    index=10,
    label="OH*",
    molecule="""
1 O u0 p2 {2,S} {3,S}
2 H u0 p0 {1,S}
3 X u0 p0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.58477686e00,
                    3.87867982e-03,
                    1.34107764e-06,
                    -3.93949585e-09,
                    1.68540254e-12,
                    -2.90977259e04,
                    -7.42452379e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.42377797e00,
                    5.57119676e-03,
                    -3.39293380e-06,
                    1.09513419e-09,
                    -1.46734126e-13,
                    -2.90972119e04,
                    -6.85806991e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""OH adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=11,
    label="H2O*",
    molecule="""
1 O u0 p2 {2,S} {3,S} {4,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,vdW}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.57850728e00,
                    5.24431866e-03,
                    -6.83196649e-06,
                    5.61222436e-09,
                    -1.73417281e-12,
                    -3.35165877e04,
                    -1.70841839e01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.76070198e00,
                    3.01863620e-05,
                    1.95429732e-06,
                    -1.04677380e-09,
                    1.70499154e-13,
                    -3.37366557e04,
                    -2.26859971e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""H2O physisorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=12,
    label="CO*",
    molecule="""
1 C u0 p0 {2,D} {3,D}
2 O u0 p2 {1,D} 
3 X u0 p0 {1,D} 
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.13851368e00,
                    7.37719433e-03,
                    -1.21673211e-05,
                    1.06231734e-08,
                    -3.55085256e-12,
                    -3.01011015e04,
                    -1.40684039e01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.39015575e00,
                    1.21423223e-03,
                    2.26543548e-08,
                    -2.74772156e-10,
                    6.84375847e-14,
                    -3.03339593e04,
                    -1.99186406e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CO adsorbed on nickel (?)""",
    longDesc="""Estimated via CFG-TiC
    Unsure of adjacency list.""",
    metal="Ni",
    facet="111",
)

entry(
    index=13,
    label="HCO*",
    molecule="""
1 C u0 p0 {2,D} {3,S} {4,S}
2 O u0 p2 {1,D}
3 H u0 p0 {1,S}
4 X u0 p0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.67902911e00,
                    1.39424587e-02,
                    -1.51013698e-05,
                    9.67718274e-09,
                    -2.69733533e-12,
                    -2.16030349e04,
                    -8.23427981e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.03186697e00,
                    8.02892147e-03,
                    -4.79702422e-06,
                    1.39761897e-09,
                    -1.61417712e-13,
                    -2.18711786e04,
                    -1.46921130e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""HCO di-sigma adsorbed on nickel. PREVIOUSLY WAS DI-SIGMA. I'VE CHANGED IT.""",
    longDesc="""Estimated via CFG-TiC
H--C--O
   || |
***********
""",
    metal="Ni",
    facet="111",
)

entry(
    index=14,
    label="COH*",
    molecule="""
1 C u0 p0 {2,S} {4,T}
2 O u0 p2 {1,S} {3,S}
3 H u0 p0 {2,S}
4 X u0 p0 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.57671035e00,
                    1.40109542e-02,
                    -1.49135569e-05,
                    9.39835302e-09,
                    -2.59115734e-12,
                    -2.39932633e04,
                    -7.86764175e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.90364615e00,
                    8.26442693e-03,
                    -4.98148751e-06,
                    1.46592732e-09,
                    -1.71209513e-13,
                    -2.42585084e04,
                    -1.42141420e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""COH adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=15,
    label="CH2O*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 {1,S} {6,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S}
6 X u0 p0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.25242157e-01,
                    1.54111015e-02,
                    -5.43318168e-06,
                    -2.53324638e-09,
                    1.74558573e-12,
                    -2.15271737e04,
                    -2.17550678e-01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    -4.92586490e-01,
                    1.77560911e-02,
                    -1.15522673e-05,
                    3.73955554e-09,
                    -4.85775848e-13,
                    -2.15145571e04,
                    8.10658192e-01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH2O di-sigma adsorbed on nickel.""",
    longDesc="""Estimated via CFG-TiC. Adjacency list changed by Richard to use two surface sites.""",
    metal="Ni",
    facet="111",
)

entry(
    index=16,
    label="CHOH*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {5,D}
2 O u0 p2 {1,S} {4,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 X u0 p0 {1,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.61466774e00,
                    1.97736658e-03,
                    1.13520606e-05,
                    -1.28686112e-08,
                    4.28854240e-12,
                    -2.08405084e04,
                    -1.83405542e01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.12897595e00,
                    1.31031973e-02,
                    -8.04327296e-06,
                    2.48752777e-09,
                    -3.12401921e-13,
                    -2.03714667e04,
                    -6.56664446e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CHOH adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=17,
    label="CH3O*",
    molecule="""
1 O u0 p2 {2,S} {6,S}
2 C u0 p0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 {2,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 X u0 p0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.53085334e-01,
                    2.34767303e-02,
                    -2.14198542e-05,
                    1.12397159e-08,
                    -2.54634600e-12,
                    -2.90522738e04,
                    -4.44446697e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.56333702e00,
                    1.57779773e-02,
                    -9.23295028e-06,
                    2.72123962e-09,
                    -3.26272331e-13,
                    -2.93898460e04,
                    -1.30594679e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH3O adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=18,
    label="CH2OH*",
    molecule="""
1 C u0 p0 {2,S} {3,S} {4,S} {6,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 O u0 p2 {1,S} {5,S}
5 H u0 p0 {4,S}
6 X u0 p0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.72324170e00,
                    2.46490814e-02,
                    -2.80859624e-05,
                    1.72678472e-08,
                    -4.26645223e-12,
                    -2.48262518e04,
                    -8.86801544e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.35800551e00,
                    9.63360342e-03,
                    -4.83501645e-06,
                    1.27341188e-09,
                    -1.42248592e-13,
                    -2.55298238e04,
                    -2.62856418e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH2OH adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=19,
    label="CH3OH*",
    molecule="""
1 O u0 p2 {2,S} {3,S} {7,vdW}
2 C u0 p0 {1,S} {4,S} {5,S} {6,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 H u0 p0 {2,S}
7 X u0 p0 {1,vdW}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.13156551e00,
                    2.38019419e-03,
                    2.17569785e-05,
                    -2.56954742e-08,
                    9.11028845e-12,
                    -3.25405443e04,
                    -1.86648447e01,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.37902838e00,
                    2.02943524e-02,
                    -1.24520299e-05,
                    3.99094219e-09,
                    -5.28740583e-13,
                    -3.18358817e04,
                    -1.03860539e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CH3OH physisorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)


entry(
    index=20,
    label="CO2*",
    molecule="""
1 C u0 p0 {2,D} {3,D} {4,vdW}
2 O u0 p2 {1,D}
3 O u0 p2 {1,D}
4 X u0 p0 {1,vdW}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.24139903e00,
                    1.23292022e-02,
                    -1.44097226e-05,
                    9.43642793e-09,
                    -2.60737252e-12,
                    -4.96482688e04,
                    1.76120609e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.71448250e00,
                    6.02066374e-03,
                    -3.73960975e-06,
                    1.12938233e-09,
                    -1.34984787e-13,
                    -4.99415034e04,
                    -5.29009370e00,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""CO2 physisorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)

entry(
    index=21,
    label="HOCO*",
    molecule="""
1 C u0 p0 {2,D} {3,S} {5,S}
2 O u0 p2 {1,D}
3 O u0 p2 {1,S} {4,S}
4 H u0 p0 {3,S}
5 X u0 p0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.00750147e-01,
                    3.22756606e-02,
                    -4.70618414e-05,
                    3.45557357e-08,
                    -1.00331658e-11,
                    -5.18553737e04,
                    -4.52637913e00,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.47849692e00,
                    7.14986800e-03,
                    -4.22981914e-06,
                    1.15767979e-09,
                    -1.19086295e-13,
                    -5.29808669e04,
                    -3.20736929e01,
                ],
                Tmin=(1000, "K"),
                Tmax=(2000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    shortDesc="""HOCO adsorbed on nickel""",
    longDesc="""Estimated via CFG-TiC""",
    metal="Ni",
    facet="111",
)
