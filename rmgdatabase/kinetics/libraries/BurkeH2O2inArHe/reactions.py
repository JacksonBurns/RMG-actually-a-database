#!/usr/bin/env python
# encoding: utf-8

name = "BurkeH2O2inArHe"
shortDesc = "Library for H2 combustion by Burke et al."
longDesc = """
Comprehensive H2/O2 kinetic model for high-pressure combustion
M.P. Burke, M. Chaos, Y. Ju, F.L. Dryer, S.J. Klippenstein
International Journal of Chemical Kinetics
Volume 44, Issue 7, pages 444-474, July 2012
DOI: 10.1002/kin.20603

In this version of the library, the reaction H+O2(+M)=HO2(+M)
takes the form reccomended by the authors for the case of
Ar or He as the main bath gas.
"""
entry(
    index=1,
    label="H + O2 <=> O + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.04e14, "cm^3/(mol*s)"), n=0, Ea=(15286, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Hong et al., Proc. Comb. Inst. 33:309-316 (2011)""",
)

entry(
    index=2,
    label="O + H2 <=> H + OH",
    degeneracy=1,
    duplicate=True,
    kinetics=MultiArrhenius(
        arrhenius=[
            Arrhenius(
                A=(3.818e12, "cm^3/(mol*s)"), n=0, Ea=(7948, "cal/mol"), T0=(1, "K")
            ),
            Arrhenius(
                A=(8.792e14, "cm^3/(mol*s)"), n=0, Ea=(19170, "cal/mol"), T0=(1, "K")
            ),
        ],
    ),
    shortDesc="""Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)""",
)

entry(
    index=3,
    label="H2 + OH <=> H2O + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.16e08, "cm^3/(mol*s)"), n=1.51, Ea=(3430, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)""",
)

entry(
    index=4,
    label="OH + OH <=> O + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(33400, "cm^3/(mol*s)"), n=2.42, Ea=(-1930, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)""",
)

entry(
    index=5,
    label="H2 <=> H + H",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(4.577e19, "cm^3/(mol*s)"), n=-1.40, Ea=(104380, "cal/mol"), T0=(1, "K")
        ),
        efficiencies={
            "[H][H]": 2.5,
            "O": 12,
            "[C-]#[O+]": 1.9,
            "O=C=O": 3.8,
            "[Ar]": 0,
            "[He]": 0,
        },
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=6,
    label="H2 + Ar <=> H + H + Ar",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.84e18, "cm^3/(mol*s)"), n=-1.10, Ea=(104380, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=7,
    label="H2 + He <=> H + H + He",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.84e18, "cm^3/(mol*s)"), n=-1.10, Ea=(104380, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=8,
    label="O + O <=> O2",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.165e15, "cm^6/(mol^2*s)"), n=-0.50, Ea=(0, "cal/mol"), T0=(1, "K")
        ),
        efficiencies={
            "[H][H]": 2.5,
            "O": 12,
            "[C-]#[O+]": 1.9,
            "O=C=O": 3.8,
            "[Ar]": 0,
            "[He]": 0,
        },
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=9,
    label="O + O + Ar <=> O2 + Ar",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.886e13, "cm^6/(mol^2*s)"), n=0, Ea=(-1788, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=10,
    label="O + O + He <=> O2 + He",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.886e13, "cm^6/(mol^2*s)"), n=0, Ea=(-1788, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=11,
    label="O + H <=> OH",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(4.714e18, "cm^6/(mol^2*s)"), n=-1, Ea=(0, "cal/mol"), T0=(1, "K")
        ),
        efficiencies={
            "[H][H]": 2.5,
            "O": 12,
            "[C-]#[O+]": 1.9,
            "O=C=O": 3.8,
            "[Ar]": 0.75,
            "[He]": 0.75,
        },
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=12,
    label="H2O <=> H + OH",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.064e27, "cm^3/(mol*s)"), n=-3.322, Ea=(120790, "cal/mol"), T0=(1, "K")
        ),
        efficiencies={
            "[H][H]": 3,
            "O": 0,
            "[C-]#[O+]": 1.9,
            "O=C=O": 3.8,
            "[O][O]": 1.5,
            "[He]": 1.1,
            "N#N": 2,
        },
    ),
    shortDesc="""Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)""",
    longDesc="""
Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)
Rate constant is for Ar with efficiencies from Michael et al., J. Phys. Chem. A, 106 (2002)
Efficiencies for CO and CO2 taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
""",
)

entry(
    index=13,
    label="H2O + H2O <=> H + OH + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.006e26, "cm^3/(mol*s)"), n=-2.44, Ea=(120180, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)""",
)

entry(
    index=14,
    label="H + O2 <=> HO2",
    degeneracy=1,
    kinetics=Troe(
        arrheniusHigh=Arrhenius(
            A=(4.65084e12, "cm^3/(mol*s)"), n=0.44, Ea=(0, "cal/mol"), T0=(1, "K")
        ),
        arrheniusLow=Arrhenius(
            A=(9.042e19, "cm^6/(mol^2*s)"), n=-1.50, Ea=(492.2, "cal/mol"), T0=(1, "K")
        ),
        alpha=0.5,
        T3=(1e-30, "K"),
        T1=(1e30, "K"),
        efficiencies={
            "[H][H]": 3,
            "[O][O]": 1.1,
            "[C-]#[O+]": 2.7,
            "O=C=O": 5.4,
            "O": 21,
            "[He]": 1.2,
            "N#N": 1.5,
        },
    ),
    shortDesc="""MAIN BATH GAS IS Ar or He""",
    longDesc="""
High-pressure limit from Troe, Proc. Comb. Inst. 28:1463-1469 (2000)
Low-pressure limit from Michael et al., J. Phys. Chem. A 106:5297-5313
Centering factors from Fernandes et al., Phys. Chem. Chem. Phys. 10:4313-4321 (2008)
""",
)

entry(
    index=15,
    label="HO2 + H <=> H2 + O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.75e06, "cm^3/(mol*s)"), n=2.09, Ea=(-1451, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Michael et al., Proc. Comb. Inst. 28:1471 (2000)""",
    longDesc="""
Scaled by 0.75
Originally: 3.659E+06 2.09 -1.451E+03
""",
)

entry(
    index=16,
    label="HO2 + H <=> OH + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.079e13, "cm^3/(mol*s)"), n=0, Ea=(295, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)""",
)

entry(
    index=17,
    label="HO2 + O <=> O2 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.85e10, "cm^3/(mol*s)"), n=1, Ea=(-723.93, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)""",
    longDesc="""
Scaled by 0.60
Originally: 4.750E+10 1.00 -7.2393E+02
""",
)

entry(
    index=18,
    label="HO2 + OH <=> H2O + O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.89e13, "cm^3/(mol*s)"), n=0, Ea=(-497, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Keyser, J. Phys. Chem. 92:1193 (1988)""",
)

entry(
    index=19,
    label="HO2 + HO2 <=> H2O2 + O2",
    degeneracy=1,
    duplicate=True,
    kinetics=MultiArrhenius(
        arrhenius=[
            Arrhenius(
                A=(4.2e14, "cm^3/(mol*s)"), n=0, Ea=(11982, "cal/mol"), T0=(1, "K")
            ),
            Arrhenius(
                A=(1.3e11, "cm^3/(mol*s)"), n=0, Ea=(-1629.3, "cal/mol"), T0=(1, "K")
            ),
        ],
    ),
    shortDesc="""Hippler et al., J. Chem. Phys. 93:1755 (1990)""",
)

entry(
    index=20,
    label="H2O2 <=> OH + OH",
    degeneracy=1,
    kinetics=Troe(
        arrheniusHigh=Arrhenius(
            A=(2e12, "s^-1"), n=0.9, Ea=(48749, "cal/mol"), T0=(1, "K")
        ),
        arrheniusLow=Arrhenius(
            A=(2.49e24, "cm^3/(mol*s)"), n=-2.3, Ea=(48749, "cal/mol"), T0=(1, "K")
        ),
        alpha=0.43,
        T3=(1e-30, "K"),
        T1=(1e30, "K"),
        efficiencies={
            "[H][H]": 3.7,
            "O": 7.5,
            "[O][O]": 1.2,
            "N#N": 1.5,
            "[C-]#[O+]": 2.8,
            "OO": 7.7,
            "O=C=O": 1.6,
            "[He]": 0.65,
        },
    ),
    shortDesc="""Troe, Combust. Flame, 158:594-601 (2011)""",
    longDesc="""
Rate constant is for Ar
Efficiencies for H2 and CO taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
""",
)

entry(
    index=21,
    label="H2O2 + H <=> H2O + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.41e13, "cm^3/(mol*s)"), n=0, Ea=(3970, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=22,
    label="H2O2 + H <=> HO2 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.82e13, "cm^3/(mol*s)"), n=0, Ea=(7950, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=23,
    label="H2O2 + O <=> OH + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.55e06, "cm^3/(mol*s)"), n=2, Ea=(3970, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index=24,
    label="H2O2 + OH <=> HO2 + H2O",
    degeneracy=1,
    duplicate=True,
    kinetics=MultiArrhenius(
        arrhenius=[
            Arrhenius(
                A=(1.74e12, "cm^3/(mol*s)"), n=0, Ea=(318, "cal/mol"), T0=(1, "K")
            ),
            Arrhenius(
                A=(7.59e13, "cm^3/(mol*s)"), n=0, Ea=(7270, "cal/mol"), T0=(1, "K")
            ),
        ],
    ),
    shortDesc="""Hong et al., J. Phys. Chem. A, 114:5718 (2010)""",
)

entry(
    index=25,
    label="HO2 + H <=> H2O + O",
    degeneracy=1,
    duplicate=False,
    kinetics=Arrhenius(
        A=(2.90e08, "cm^3/(mol*s)"), n=1.55, Ea=(-160.1, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Mousavipour et al., Bull. Chem. Soc. Jpn., 80:1901 (2007)""",
    longDesc="""Reaction X1 in Burke at el. (Table III)
    Also available from Karkach et al., J. Chem. Phys., 110:11918 (1999):
    kinetics = Arrhenius(A=(5.90E+12, 'cm^3/(mol*s)'), n=0.81, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
    """,
)

entry(
    index=26,
    label="HO2 + H <=> H2O2",
    degeneracy=1,
    duplicate=False,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.0e14, "cm^6/(mol^2*s)"), n=1.25, Ea=(-270, "cal/mol"), T0=(1, "K")
        )
    ),
    shortDesc="""Mousavipour et al., Bull. Chem. Soc. Jpn., 80:1901 (2007)""",
    longDesc="""Reaction X2 in Burke at el. (Table III),
    p. 1909 in Mousavipour et al.
    Declared 'negligible' by Burke at el.
    The original rate Arrhenius(A=(7.20E+09, 'cm^6/(mol^2*s)'), n=1.25, Ea=(-270, 'cal/mol'), T0 = (1, 'K')) was
    multiplied by the inverse of ~1.2E-05 mol cm^-3 which is the density of an ideal gas at 1000 K,
    so that a ThirdBody kinetics format could be written here""",
)

entry(
    index=27,
    label="OH + OH <=> H2 + O2",
    degeneracy=1,
    duplicate=False,
    kinetics=Arrhenius(
        A=(2.00e11, "cm^3/(mol*s)"), n=0.51, Ea=(5.050e04, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Karkach et al., J. Chem. Phys., 110:11918 (1999)""",
    longDesc="""Reaction X3 in Burke at el. (Table III)""",
)

entry(
    index=28,
    label="H2O + O <=> H2 + O2",
    degeneracy=1,
    duplicate=False,
    kinetics=Arrhenius(
        A=(1.07e10, "cm^3/(mol*s)"), n=0.97, Ea=(6.870e04, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Karkach et al., J. Chem. Phys., 110:11918 (1999)""",
    longDesc="""Reaction X4 in Burke at el. (Table III)""",
)

entry(
    index=29,
    label="H2O2 + O <=> H2O + O2",
    degeneracy=1,
    duplicate=False,
    kinetics=Arrhenius(
        A=(8.43e11, "cm^3/(mol*s)"), n=0.00, Ea=(3.970e03, "cal/mol"), T0=(1, "K")
    ),
    shortDesc="""Baulch et al., J. Phys. Chem. Ref. Data, 34:757 (2005)""",
    longDesc="""
    Reaction X5 in Burke at el. (Table III),
    Upper limit""",
)

entry(
    index=30,
    label="OH + O <=> HO2",
    degeneracy=1,
    duplicate=False,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(1.00e15, "cm^6/(mol^2*s)"), n=0.00, Ea=(0.00, "cal/mol"), T0=(1, "K")
        )
    ),
    shortDesc="""Germann et al., J. Phys. Chem. A, 101:6358 (1997)""",
    longDesc="""Reaction X6 in Burke at el. (Table III)
    Also available from Westbrook et al., Prog. Energy Combust. Sci. 10:1 (1984):
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.00E+17, 'cm^6/(mol^2*s)'), n=0.00, Ea=(0.00, 'cal/mol'), T0 = (1, 'K')))
    """,
)
