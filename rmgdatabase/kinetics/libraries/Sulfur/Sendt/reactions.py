#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Sendt"
shortDesc = "small sulfur molecule reactions"
longDesc = """
Created by Caleb for small sulfur molecule reactions by the work of Sendt et al.
"""
entry(
    index=1,
    label="H2S + H <=> SH + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.49e07, "cm^3/(mol*s)"),
        n=1.94,
        Ea=(0.9, "kcal/mol"),
        T0=(1, "K"),
    ),
    longDesc="""
Reactions from Sendt et al. Proc. Comb. Inst. 2002
Not including reactions 1, 19, 20, 21
""",
)

entry(
    index=2,
    label="H2S + S <=> SH + SH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(8.32e13, "cm^3/(mol*s)"), n=0, Ea=(7.38, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=3,
    label="S + H2 <=> SH + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.35e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(19.29, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=4,
    label="S + SH <=> S2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.7e13, "cm^3/(mol*s)"), n=0, Ea=(0, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=5,
    label="H + HSS <=> SH + SH",
    degeneracy=1,
    kinetics=Arrhenius(A=(3e14, "cm^3/(mol*s)"), n=0, Ea=(0, "kcal/mol"), T0=(1, "K")),
    longDesc="""
	Using adjusted singlet surface calculation for this one (see paper)
	""",
)

# entry(
#    index = 5,
#    label = "H + HSS <=> SH + SH",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1.1e+13, 'cm^3/(mol*s)'),
#        n = 0.353,
#        Ea = (0.21, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc =
# 	u"""
# 	Using unadjusted singlet surface calculation for this one (see paper)
# 	""",
# )

entry(
    index=6,
    label="SH + HSS <=> H2S + S2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6270, "cm^3/(mol*s)"), n=3.05, Ea=(-1.1, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=7,
    label="H + HSS <=> H2 + S2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.23e08, "cm^3/(mol*s)"),
        n=1.653,
        Ea=(-1.1, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=8,
    label="H + HSS <=> H2S + S",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.41e13, "cm^3/(mol*s)"), n=0, Ea=(6.33, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=9,
    label="S + HSS <=> S2 + SH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.17e06, "cm^3/(mol*s)"),
        n=2.2,
        Ea=(-0.6, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=10,
    label="HSS + HSS <=> H2S2 + S2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.56, "cm^3/(mol*s)"), n=3.37, Ea=(-1.67, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=11,
    label="H2S2 + H <=> HSS + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.99e07, "cm^3/(mol*s)"),
        n=1.933,
        Ea=(-1.41, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=12,
    label="H2S2 + H <=> H2S + SH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.66e08, "cm^3/(mol*s)"),
        n=1.724,
        Ea=(0.47, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=13,
    label="H2S2 + SH <=> H2S + HSS",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6400, "cm^3/(mol*s)"), n=2.98, Ea=(-1.48, "kcal/mol"), T0=(1, "K")
    ),
)

entry(
    index=14,
    label="H2S2 + S <=> HSS + SH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.85e06, "cm^3/(mol*s)"),
        n=2.31,
        Ea=(1.2, "kcal/mol"),
        T0=(1, "K"),
    ),
)

entry(
    index=15,
    label="H + S2 <=> HSS",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(1.15e25, "cm^6/(mol^2*s)"),
            n=-2.84,
            Ea=(1.66, "kcal/mol"),
            T0=(1, "K"),
        ),
        efficiencies={"S": 1.1, "[He]": 1.39, "N#N": 1, "[Ar]": 0.88},
    ),
    longDesc="""
Pressure dependent reactions from Sendt et al. Proc. Comb. Inst. 2002
Not including reactions 1, 19, 20, 21
""",
)

entry(
    index=16,
    label="H2S2 <=> SH + SH",
    degeneracy=1,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.93e14, "cm^3/(mol*s)"),
            n=1,
            Ea=(57.03, "kcal/mol"),
            T0=(1, "K"),
        ),
        efficiencies={"S": 1.1, "[He]": 1.39, "N#N": 1, "[Ar]": 0.88},
    ),
    longDesc="""
A-factor could also be 2.31E14
""",
)
