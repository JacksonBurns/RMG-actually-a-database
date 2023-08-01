#!/usr/bin/env python
# encoding: utf-8

name = "Chernov"
shortDesc = (
    "Aromatic reactions only from 2014 Chernov et al. Combustion and Flame mechanism"
)
longDesc = """
Includes only reactions involving aromatic species from the mechanism in:
V. Chernov, et al., 
Soot Formation with C1 and C2 Fuels Using an Improved Chemical Mechanism for PAH growth
Combustion and Flame 161 (2014) 592-601
"""
entry(
    index=1,
    label="H2CCCH + C2H3 <=> C5H5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.6e40, "cm^3/(mol*s)"),
        n=-7.8,
        Ea=(119812, "J/mol"),
        T0=(1, "K"),
        comment="468",
    ),
    longDesc="""
468
""",
)

entry(
    index=2,
    label="H2CCCH + C2H2 <=> C5H5",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.87e55, "cm^3/(mol*s)"),
        n=-12.5,
        Ea=(17493.6, "J/mol"),
        T0=(1, "K"),
        comment="469",
    ),
    allow_max_rate_violation=True,
    longDesc="""
469
""",
)

entry(
    index=3,
    label="C5H5 + O2 <=> CH2CO + C2H2 + HCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e19, "cm^3/(mol*s)"),
        n=-2.48,
        Ea=(45563.3, "J/mol"),
        T0=(1, "K"),
        comment="470",
    ),
    longDesc="""
470
""",
)

entry(
    index=4,
    label="C5H6 + O2 <=> C5H5 + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(104762, "J/mol"),
        T0=(1, "K"),
        comment="471",
    ),
    longDesc="""
471
""",
)

entry(
    index=5,
    label="C5H5 + O <=> i-C4H5 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="472",
    ),
    longDesc="""
472
""",
)

entry(
    index=6,
    label="C5H6 + H <=> C5H5 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.8e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(9453.55, "J/mol"),
        T0=(1, "K"),
        comment="473",
    ),
    longDesc="""
473
""",
)

entry(
    index=7,
    label="C5H5 + H <=> C5H6",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.6e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="474\nC5H6+H = C3H5+C2H2 6.600E+14 0.0000 6200.00\n475",
    ),
    longDesc="""
474
C5H6+H = C3H5+C2H2 6.600E+14 0.0000 6200.00
475
""",
)

entry(
    index=8,
    label="C5H5 + OH <=> CH2O + C2H2 + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e15, "cm^3/(mol*s)"),
        n=0,
        Ea=(324264, "J/mol"),
        T0=(1, "K"),
        comment="476",
    ),
    longDesc="""
476
""",
)

entry(
    index=9,
    label="C5H6 + OH <=> C5H5 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.43e09, "cm^3/(mol*s)"),
        n=1.18,
        Ea=(-1870.76, "J/mol"),
        T0=(1, "K"),
        comment="477",
    ),
    longDesc="""
477
""",
)

entry(
    index=10,
    label="C5H6 + HO2 <=> C5H5 + H2O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(48781, "J/mol"),
        T0=(1, "K"),
        comment="478",
    ),
    longDesc="""
478
""",
)

entry(
    index=11,
    label="C5H6 + C2H3 <=> C5H5 + C2H4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="479",
    ),
    longDesc="""
479
""",
)

entry(
    index=12,
    label="C6H5O <=> C5H5 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.4e11, "s^-1"),
        n=0,
        Ea=(183750, "J/mol"),
        T0=(1, "K"),
        comment="480",
    ),
    longDesc="""
480
""",
)

entry(
    index=13,
    label="C6H5O + O <=> C5H5 + CO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.6e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="481",
    ),
    longDesc="""
481
""",
)

entry(
    index=14,
    label="C6H5O + H <=> C5H6 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="482",
    ),
    longDesc="""
482
""",
)

entry(
    index=15,
    label="C6H5O + H <=> C6H5OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="483",
    ),
    longDesc="""
483
""",
)

entry(
    index=16,
    label="C6H5OH <=> C5H6 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e12, "s^-1"),
        n=0,
        Ea=(254423, "J/mol"),
        T0=(1, "K"),
        comment="484",
    ),
    longDesc="""
484
""",
)

entry(
    index=17,
    label="C6H5OH + O <=> C6H5O + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.8e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(29932.1, "J/mol"),
        T0=(1, "K"),
        comment="485",
    ),
    longDesc="""
485
""",
)

entry(
    index=18,
    label="C6H5OH + H <=> C6H5O + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.58e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(24943.4, "J/mol"),
        T0=(1, "K"),
        comment="486",
    ),
    longDesc="""
486
""",
)

entry(
    index=19,
    label="C6H5OH + OH <=> C6H5O + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e10, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="487",
    ),
    longDesc="""
487
""",
)

entry(
    index=20,
    label="C6H5OH + C2H3 <=> C6H5O + C2H4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="488",
    ),
    longDesc="""
488
""",
)

entry(
    index=21,
    label="H2CCCH + H2CCCH <=> A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e36, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="489",
    ),
    longDesc="""
489
""",
)

entry(
    index=22,
    label="H2CCCH + H2CCCH <=> A1- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e35, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="490",
    ),
    longDesc="""
490
""",
)

entry(
    index=23,
    label="H2CCCCH + C2H3 <=> A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="491",
    ),
    longDesc="""
491
""",
)

entry(
    index=24,
    label="H2CCCCH + C2H3 <=> A1- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="492",
    ),
    longDesc="""
492
""",
)

entry(
    index=25,
    label="H2CCCH + C3H4 <=> A1 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.4e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(41572.4, "J/mol"),
        T0=(1, "K"),
        comment="493",
    ),
    longDesc="""
493
""",
)

entry(
    index=26,
    label="C2H3 + C4H4 <=> A1 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.9e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(10393.1, "J/mol"),
        T0=(1, "K"),
        comment="494",
    ),
    longDesc="""
494
""",
)

entry(
    index=27,
    label="H2CCCCH + C2H2 <=> A1-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61942.8, "J/mol"),
        T0=(1, "K"),
        comment="495",
    ),
    longDesc="""
495
""",
)

entry(
    index=28,
    label="C4H4 + C2H2 <=> A1- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e09, "cm^3/(mol*s)"),
        n=0,
        Ea=(124717, "J/mol"),
        T0=(1, "K"),
        comment="496",
    ),
    longDesc="""
496
""",
)

entry(
    index=29,
    label="i-C4H5 + C2H2 <=> A1 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(22449.1, "J/mol"),
        T0=(1, "K"),
        comment="497",
    ),
    longDesc="""
497
""",
)

entry(
    index=30,
    label="i-C4H5 + C2H3 <=> A1 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.8e-13, "cm^3/(mol*s)"),
        n=7.07,
        Ea=(-14966, "J/mol"),
        T0=(1, "K"),
        comment="498",
    ),
    longDesc="""
498
""",
)

entry(
    index=31,
    label="i-C4H5 + C2H <=> A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="499",
    ),
    longDesc="""
499
""",
)

entry(
    index=32,
    label="i-C4H5 + C2H <=> A1- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="500",
    ),
    longDesc="""
500
""",
)

entry(
    index=33,
    label="C5H6 + C2H3 <=> A1 + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.12e67, "cm^3/(mol*s)"),
        n=-16.08,
        Ea=(177265, "J/mol"),
        T0=(1, "K"),
        comment="501\nC5H5+CH3 = A1+2H 1.000E+18 0.0000 30000.00\n502",
    ),
    longDesc="""
501
C5H5+CH3 = A1+2H 1.000E+18 0.0000 30000.00
502
""",
)

entry(
    index=34,
    label="A1 <=> A1- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9e14, "s^-1"),
        n=0,
        Ea=(449480, "J/mol"),
        T0=(1, "K"),
        comment="503",
    ),
    longDesc="""
503
""",
)

entry(
    index=35,
    label="A1 <=> C4H4 + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9e14, "s^-1"),
        n=0,
        Ea=(449480, "J/mol"),
        T0=(1, "K"),
        comment="504",
    ),
    longDesc="""
504
""",
)

entry(
    index=36,
    label="A1 + O2 <=> A1- + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(261906, "J/mol"),
        T0=(1, "K"),
        comment="505",
    ),
    longDesc="""
505
""",
)

entry(
    index=37,
    label="A1 + O <=> A1- + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="506",
    ),
    longDesc="""
506
""",
)

entry(
    index=38,
    label="A1 + O <=> C6H5OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18957, "J/mol"),
        T0=(1, "K"),
        comment="507",
    ),
    longDesc="""
507
""",
)

entry(
    index=39,
    label="A1 + O <=> C6H5O + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18957, "J/mol"),
        T0=(1, "K"),
        comment="508",
    ),
    longDesc="""
508
""",
)

entry(
    index=40,
    label="A1 + H <=> A1- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.51e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(67014.6, "J/mol"),
        T0=(1, "K"),
        comment="509",
    ),
    longDesc="""
509
""",
)

entry(
    index=41,
    label="A1 + OH <=> C6H5OH + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(43900.4, "J/mol"),
        T0=(1, "K"),
        comment="510",
    ),
    longDesc="""
510
""",
)

entry(
    index=42,
    label="A1 + OH <=> A1- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.45e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18790.7, "J/mol"),
        T0=(1, "K"),
        comment="511",
    ),
    longDesc="""
511
""",
)

entry(
    index=43,
    label="A1 + CH3 <=> A1- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="512",
    ),
    longDesc="""
512
""",
)

entry(
    index=44,
    label="A1 + C2H <=> A1- + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="513",
    ),
    longDesc="""
513
""",
)

entry(
    index=45,
    label="A1 + C4H <=> A1- + C4H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="514",
    ),
    longDesc="""
514
""",
)

entry(
    index=46,
    label="A1 + C6H <=> A1- + C6H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="515",
    ),
    longDesc="""
515
""",
)

entry(
    index=47,
    label="A1 + C8H <=> A1- + C8H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="516",
    ),
    longDesc="""
516
""",
)

entry(
    index=48,
    label="A1- + O2 <=> C6H5O + O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(25359.1, "J/mol"),
        T0=(1, "K"),
        comment="517",
    ),
    longDesc="""
517
""",
)

entry(
    index=49,
    label="A1- + O <=> C5H5 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="518",
    ),
    longDesc="""
518
""",
)

entry(
    index=50,
    label="A1- + OH <=> C6H5O + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="519",
    ),
    longDesc="""
519
""",
)

entry(
    index=51,
    label="A1- + C6H5OH <=> C6H5O + A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.91e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(18291.8, "J/mol"),
        T0=(1, "K"),
        comment="520",
    ),
    longDesc="""
520
""",
)

entry(
    index=52,
    label="i-C4H5 + C3H4 <=> C7H8 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(15381.8, "J/mol"),
        T0=(1, "K"),
        comment="521",
    ),
    longDesc="""
521
""",
)

entry(
    index=53,
    label="i-C4H5 + H2CCCH <=> C7H7 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.5e35, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="522",
    ),
    longDesc="""
522
""",
)

entry(
    index=54,
    label="A1 + CH2 <=> C7H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.7e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="523",
    ),
    longDesc="""
523
""",
)

entry(
    index=55,
    label="A1 + CH2(S) <=> C7H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="524",
    ),
    longDesc="""
524
""",
)

entry(
    index=56,
    label="C7H8 <=> A1- + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.4e16, "s^-1"),
        n=0,
        Ea=(414892, "J/mol"),
        T0=(1, "K"),
        comment="525",
    ),
    longDesc="""
525
""",
)

entry(
    index=57,
    label="i-C4H5 + H2CCCH <=> C7H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e36, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="526",
    ),
    longDesc="""
526
""",
)

entry(
    index=58,
    label="C7H8 + O2 <=> C7H7 + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(172110, "J/mol"),
        T0=(1, "K"),
        comment="527",
    ),
    longDesc="""
527
""",
)

entry(
    index=59,
    label="C7H8 + O <=> C7H7 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.3e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="528",
    ),
    longDesc="""
528
""",
)

entry(
    index=60,
    label="C7H8 + H <=> A1 + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(21201.9, "J/mol"),
        T0=(1, "K"),
        comment="529",
    ),
    longDesc="""
529
""",
)

entry(
    index=61,
    label="C7H8 + H <=> C7H7 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(34089.3, "J/mol"),
        T0=(1, "K"),
        comment="530",
    ),
    longDesc="""
530
""",
)

entry(
    index=62,
    label="C7H8 + OH <=> C7H7 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.18e09, "cm^3/(mol*s)"),
        n=1,
        Ea=(3658.37, "J/mol"),
        T0=(1, "K"),
        comment="531",
    ),
    longDesc="""
531
""",
)

entry(
    index=63,
    label="C7H8 + HO2 <=> C7H7 + H2O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(62192.3, "J/mol"),
        T0=(1, "K"),
        comment="532",
    ),
    longDesc="""
532
""",
)

entry(
    index=64,
    label="C7H8 + CH3 <=> C7H7 + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.16e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(46477.9, "J/mol"),
        T0=(1, "K"),
        comment="533",
    ),
    longDesc="""
533
""",
)

entry(
    index=65,
    label="C7H8 + C2H3 <=> C7H7 + C2H4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(33923, "J/mol"),
        T0=(1, "K"),
        comment="534",
    ),
    longDesc="""
534
""",
)

entry(
    index=66,
    label="C7H8 + H2CCCH <=> C7H7 + C3H4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(63023.7, "J/mol"),
        T0=(1, "K"),
        comment="535",
    ),
    longDesc="""
535
""",
)

entry(
    index=67,
    label="C7H8 + C3H5 <=> C7H7 + C3H6",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62192.3, "J/mol"),
        T0=(1, "K"),
        comment="536",
    ),
    longDesc="""
536
""",
)

entry(
    index=68,
    label="C7H8 + C5H5 <=> C7H7 + C5H6",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(46394.8, "J/mol"),
        T0=(1, "K"),
        comment="537",
    ),
    longDesc="""
537
""",
)

entry(
    index=69,
    label="C7H8 + A1- <=> C7H7 + A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.94e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(46527.8, "J/mol"),
        T0=(1, "K"),
        comment="538",
    ),
    longDesc="""
538
""",
)

entry(
    index=70,
    label="A1- + CH3 <=> C7H7 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="539",
    ),
    longDesc="""
539
""",
)

entry(
    index=71,
    label="C7H7 <=> C4H4 + H2CCCH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e14, "s^-1"),
        n=0,
        Ea=(351702, "J/mol"),
        T0=(1, "K"),
        comment="540",
    ),
    longDesc="""
540
""",
)

entry(
    index=72,
    label="C7H7 + O <=> A1 + HCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="541\nC7H7 = C5H5+C2H2 6.100E+13 0.0000 35000.00\n542",
    ),
    longDesc="""
541
C7H7 = C5H5+C2H2 6.100E+13 0.0000 35000.00
542
""",
)

entry(
    index=73,
    label="C7H7 + O <=> A1- + CH2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="543",
    ),
    longDesc="""
543
""",
)

entry(
    index=74,
    label="C7H7 + H <=> C7H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.6e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="544",
    ),
    longDesc="""
544
""",
)

entry(
    index=75,
    label="C7H7 + HO2 <=> A1 + HCO + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="545",
    ),
    longDesc="""
545
""",
)

entry(
    index=76,
    label="C7H7 + HO2 <=> A1- + CH2O + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.17e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="546",
    ),
    longDesc="""
546
""",
)

entry(
    index=77,
    label="C7H7 + H + OH <=> A1 + CH2OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^6/(mol^2*s)"),
        n=0,
        Ea=(21551.1, "J/mol"),
        T0=(1, "K"),
        comment="547",
    ),
    longDesc="""
547
""",
)

entry(
    index=78,
    label="i-C4H5 + C4H2 <=> A1C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.16e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(7483.02, "J/mol"),
        T0=(1, "K"),
        comment="548",
    ),
    longDesc="""
548
""",
)

entry(
    index=79,
    label="A1C2H- + H <=> A1C2H",
    degeneracy=1,
    kinetics=Troe(
        arrheniusHigh=Arrhenius(
            A=(1e14, "cm^3/(mol*s)"), n=0, Ea=(0, "J/mol"), T0=(1, "K")
        ),
        arrheniusLow=Arrhenius(
            A=(6.6e75, "cm^6/(mol^2*s)"),
            n=-16.3,
            Ea=(58201.3, "J/mol"),
            T0=(1, "K"),
        ),
        alpha=1,
        T3=(0.1, "K"),
        T1=(584.9, "K"),
        T2=(6113, "K"),
        efficiencies={
            "C": 2,
            "O=C=O": 2,
            "CC": 3,
            "O": 6,
            "[H][H]": 2,
            "[C-]#[O+]": 1.5,
        },
        comment="549",
    ),
    longDesc="""
549
""",
)

entry(
    index=80,
    label="H2CCCCH + C4H2 <=> A1C2H-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.6e70, "cm^3/(mol*s)"),
        n=-17.77,
        Ea=(130205, "J/mol"),
        T0=(1, "K"),
        comment="550",
    ),
    longDesc="""
550
""",
)

entry(
    index=81,
    label="A1- + C4H2 <=> A1C2H + C2H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(91459.2, "J/mol"),
        T0=(1, "K"),
        comment="551",
    ),
    longDesc="""
551
""",
)

entry(
    index=82,
    label="A1- + C2H3 <=> A1C2H + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.9e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(26606.3, "J/mol"),
        T0=(1, "K"),
        comment="552",
    ),
    longDesc="""
552
""",
)

entry(
    index=83,
    label="A1- + C4H4 <=> A1C2H + C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.2e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(5656.83, "J/mol"),
        T0=(1, "K"),
        comment="553",
    ),
    longDesc="""
553
""",
)

entry(
    index=84,
    label="A1 + C2H <=> A1C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="554",
    ),
    longDesc="""
554
""",
)

entry(
    index=85,
    label="A1- + C2H <=> A1C2H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.24e14, "cm^3/(mol*s)"),
        n=-0.5,
        Ea=(2494.34, "J/mol"),
        T0=(1, "K"),
        comment="555",
    ),
    longDesc="""
555
""",
)

entry(
    index=86,
    label="A1C2H + O <=> A1C2H- + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(34089.3, "J/mol"),
        T0=(1, "K"),
        comment="556",
    ),
    longDesc="""
556
""",
)

entry(
    index=87,
    label="A1C2H + O <=> A1- + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e07, "cm^3/(mol*s)"),
        n=2,
        Ea=(7898.75, "J/mol"),
        T0=(1, "K"),
        comment="557",
    ),
    longDesc="""
557
""",
)

entry(
    index=88,
    label="A1C2H + O <=> C6H5O + C2H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18790.7, "J/mol"),
        T0=(1, "K"),
        comment="558",
    ),
    longDesc="""
558
""",
)

entry(
    index=89,
    label="A1C2H + H <=> A1C2H- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.7e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(40591.3, "J/mol"),
        T0=(1, "K"),
        comment="559",
    ),
    longDesc="""
559
""",
)

entry(
    index=90,
    label="A1C2H + H <=> A1- + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(40591.3, "J/mol"),
        T0=(1, "K"),
        comment="560",
    ),
    longDesc="""
560
""",
)

entry(
    index=91,
    label="A1C2H + H <=> n-C8H7",
    degeneracy=1,
    duplicate=True,
    kinetics=Arrhenius(
        A=(3e43, "cm^3/(mol*s)"),
        n=-9.22,
        Ea=(63289.8, "J/mol"),
        T0=(1, "K"),
        comment="561",
    ),
    longDesc="""
561
""",
)

entry(
    index=92,
    label="A1C2H + OH <=> A1C2H- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(19123.3, "J/mol"),
        T0=(1, "K"),
        comment="562",
    ),
    longDesc="""
562
""",
)

entry(
    index=93,
    label="A1C2H + OH <=> A1- + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(0.000218, "cm^3/(mol*s)"),
        n=4.5,
        Ea=(-4157.24, "J/mol"),
        T0=(1, "K"),
        comment="563",
    ),
    longDesc="""
563
""",
)

entry(
    index=94,
    label="A1C2H + OH <=> A1 + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2440, "cm^3/(mol*s)"),
        n=3.02,
        Ea=(46344.9, "J/mol"),
        T0=(1, "K"),
        comment="564",
    ),
    longDesc="""
564
""",
)

entry(
    index=95,
    label="A1C2H + C2H <=> A1C2H- + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="565",
    ),
    longDesc="""
565
""",
)

entry(
    index=96,
    label="C4H4 + C4H4 <=> A1C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.8e20, "cm^3/(mol*s)"),
        n=-1.9,
        Ea=(168202, "J/mol"),
        T0=(1, "K"),
        comment="566",
    ),
    longDesc="""
566
""",
)

entry(
    index=97,
    label="i-C4H5 + C4H4 <=> A1C2H3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.16e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(2494.34, "J/mol"),
        T0=(1, "K"),
        comment="567",
    ),
    longDesc="""
567
""",
)

entry(
    index=98,
    label="C5H5 + H2CCCH <=> A1C2H3* + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e35, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="568\nRxn 568 commented out because reverse rate coefficient is above Z",
    ),
    longDesc="""
568
Rxn 568 commented out because reverse rate coefficient is above Z
""",
)

entry(
    index=99,
    label="A1 + C2H3 <=> A1C2H3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.9e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(26606.3, "J/mol"),
        T0=(1, "K"),
        comment="569",
    ),
    longDesc="""
569
""",
)

entry(
    index=100,
    label="A1- + C2H3 <=> A1C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.06e26, "cm^3/(mol*s)"),
        n=-4,
        Ea=(22033.4, "J/mol"),
        T0=(1, "K"),
        comment="570",
    ),
    longDesc="""
570
""",
)

entry(
    index=101,
    label="A1- + C2H4 <=> A1C2H3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.51e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(25733.3, "J/mol"),
        T0=(1, "K"),
        comment="571",
    ),
    longDesc="""
571
""",
)

entry(
    index=102,
    label="A1- + C4H4 <=> A1C2H3 + C2H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(83144.7, "J/mol"),
        T0=(1, "K"),
        comment="572",
    ),
    longDesc="""
572
""",
)

entry(
    index=103,
    label="A1- + C4H6 <=> A1C2H3 + C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.2e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(7961.44, "J/mol"),
        T0=(1, "K"),
        comment="573",
    ),
    longDesc="""
573
""",
)

entry(
    index=104,
    label="C7H7 + CH2 <=> A1C2H3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.4e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="574",
    ),
    longDesc="""
574
""",
)

entry(
    index=105,
    label="A1C2H3 + H <=> n-C8H7 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.65e06, "cm^3/(mol*s)"),
        n=2.53,
        Ea=(50884.6, "J/mol"),
        T0=(1, "K"),
        comment="575",
    ),
    longDesc="""
575
""",
)

entry(
    index=106,
    label="A1C2H3 + H <=> A1C2H3* + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(303, "cm^3/(mol*s)"),
        n=3.3,
        Ea=(23862.5, "J/mol"),
        T0=(1, "K"),
        comment="576",
    ),
    longDesc="""
576
""",
)

entry(
    index=107,
    label="A1C2H3 + O <=> A1- + CH2HCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e08, "cm^3/(mol*s)"),
        n=1.45,
        Ea=(3741.51, "J/mol"),
        T0=(1, "K"),
        comment="577",
    ),
    longDesc="""
577
""",
)

entry(
    index=108,
    label="A1C2H3 + O <=> A1- + CH3 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.92e07, "cm^3/(mol*s)"),
        n=1.83,
        Ea=(914.592, "J/mol"),
        T0=(1, "K"),
        comment="578",
    ),
    longDesc="""
578
""",
)

entry(
    index=109,
    label="A1C2H3 + O <=> C2H3 + C6H5O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18832.3, "J/mol"),
        T0=(1, "K"),
        comment="579",
    ),
    longDesc="""
579
""",
)

entry(
    index=110,
    label="A1C2H3 + O <=> n-C8H7 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.55e06, "cm^3/(mol*s)"),
        n=1.91,
        Ea=(15631.2, "J/mol"),
        T0=(1, "K"),
        comment="580",
    ),
    longDesc="""
580
""",
)

entry(
    index=111,
    label="A1C2H3 + OH <=> n-C8H7 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.1e06, "cm^3/(mol*s)"),
        n=2,
        Ea=(14259.3, "J/mol"),
        T0=(1, "K"),
        comment="581",
    ),
    longDesc="""
581
""",
)

entry(
    index=112,
    label="A1C2H3 + OH => C6H5O + C2H4",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(44066.7, "J/mol"),
        T0=(1, "K"),
        comment="582",
    ),
    longDesc="""
582
""",
)

entry(
    index=113,
    label="A1C2H3 + OH <=> A1C2H3* + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.63e08, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6092.6, "J/mol"),
        T0=(1, "K"),
        comment="583",
    ),
    longDesc="""
583
""",
)

entry(
    index=114,
    label="A1C2H3 + OH <=> C7H7 + CH2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.4e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="584",
    ),
    longDesc="""
584
""",
)

entry(
    index=115,
    label="A1C2H3 + O2 <=> C6H5O + CH2HCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.88e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(31251.6, "J/mol"),
        T0=(1, "K"),
        comment="585",
    ),
    longDesc="""
585
""",
)

entry(
    index=116,
    label="A1C2H3* + O2 <=> C6H5O + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.88e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(31251.6, "J/mol"),
        T0=(1, "K"),
        comment="586",
    ),
    longDesc="""
586
""",
)

entry(
    index=117,
    label="A1C2H3* + H <=> A1C2H3",
    degeneracy=1,
    kinetics=Troe(
        arrheniusHigh=Arrhenius(
            A=(1e14, "cm^3/(mol*s)"), n=0, Ea=(0, "J/mol"), T0=(1, "K")
        ),
        arrheniusLow=Arrhenius(
            A=(6.6e75, "cm^6/(mol^2*s)"),
            n=-16.3,
            Ea=(58201.3, "J/mol"),
            T0=(1, "K"),
        ),
        alpha=1,
        T3=(0.1, "K"),
        T1=(584.9, "K"),
        T2=(6113, "K"),
        efficiencies={
            "C": 2,
            "O=C=O": 2,
            "CC": 3,
            "O": 6,
            "[H][H]": 2,
            "[C-]#[O+]": 1.5,
        },
        comment="587",
    ),
    longDesc="""
587
""",
)

entry(
    index=118,
    label="C5H5 + H2CCCH <=> n-C8H7 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.5e35, "cm^3/(mol*s)"),
        n=-7.18,
        Ea=(35203.5, "J/mol"),
        T0=(1, "K"),
        comment="588\nRxn 588 commented out because k>Z for T<1400 K",
    ),
    longDesc="""
588
Rxn 588 commented out because k>Z for T<1400 K
""",
)

entry(
    index=119,
    label="A1 + C2H <=> n-C8H7",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e38, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="589",
    ),
    longDesc="""
589
""",
)

entry(
    index=120,
    label="A1- + C2H2 <=> n-C8H7",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(48872.5, "J/mol"),
        T0=(1, "K"),
        comment="590",
    ),
    longDesc="""
590
""",
)

entry(
    index=121,
    label="A1- + C2H3 <=> n-C8H7 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.4, "cm^3/(mol*s)"),
        n=4.14,
        Ea=(96589.2, "J/mol"),
        T0=(1, "K"),
        comment="591",
    ),
    longDesc="""
591
""",
)

entry(
    index=122,
    label="n-C8H7 <=> A1C2H + H",
    degeneracy=1,
    duplicate=True,
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(
            A=(2e17, "cm^3/(mol*s)"), n=0, Ea=(166289, "J/mol"), T0=(1, "K")
        ),
        efficiencies={},
        comment="592",
    ),
    longDesc="""
592
""",
)

entry(
    index=123,
    label="n-C8H7 + H <=> A1C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.4e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(10060.5, "J/mol"),
        T0=(1, "K"),
        comment="593",
    ),
    longDesc="""
593
""",
)

entry(
    index=124,
    label="n-C8H7 + H <=> A1C2H + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="594",
    ),
    longDesc="""
594
""",
)

entry(
    index=125,
    label="n-C8H7 + OH <=> A1C2H + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="595",
    ),
    longDesc="""
595
""",
)

entry(
    index=126,
    label="C5H5 + C4H4 <=> INDENE + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(41821.8, "J/mol"),
        T0=(1, "K"),
        comment="596",
    ),
    longDesc="""
596
""",
)

entry(
    index=127,
    label="A1- + H2CCCH <=> INDENE",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.86e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(56954.1, "J/mol"),
        T0=(1, "K"),
        comment="597",
    ),
    longDesc="""
597
""",
)

entry(
    index=128,
    label="C4H6 + A1- <=> INDENE + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.42e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(1164.03, "J/mol"),
        T0=(1, "K"),
        comment="598",
    ),
    longDesc="""
598
""",
)

entry(
    index=129,
    label="i-C4H5 + A1 <=> INDENE + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.42e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(1164.03, "J/mol"),
        T0=(1, "K"),
        comment="599",
    ),
    longDesc="""
599
""",
)

entry(
    index=130,
    label="A1- + C3H4 <=> INDENE + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e16, "cm^3/(mol*s)"),
        n=0,
        Ea=(138020, "J/mol"),
        T0=(1, "K"),
        comment="600",
    ),
    longDesc="""
600
""",
)

entry(
    index=131,
    label="INDENE <=> INDENYL + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e15, "s^-1"),
        n=0,
        Ea=(322602, "J/mol"),
        T0=(1, "K"),
        comment="601",
    ),
    longDesc="""
601
""",
)

entry(
    index=132,
    label="INDENE + O <=> INDENYL + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="602",
    ),
    longDesc="""
602
""",
)

entry(
    index=133,
    label="INDENE + O <=> C7H7 + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(16628.9, "J/mol"),
        T0=(1, "K"),
        comment="603",
    ),
    longDesc="""
603
""",
)

entry(
    index=134,
    label="INDENE + H <=> INDENYL + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="604",
    ),
    longDesc="""
604
""",
)

entry(
    index=135,
    label="C7H7 + C2H2 <=> INDENE + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(41821.8, "J/mol"),
        T0=(1, "K"),
        comment="605",
    ),
    longDesc="""
605
""",
)

entry(
    index=136,
    label="INDENE + H <=> A1C2H + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(191233, "J/mol"),
        T0=(1, "K"),
        comment="606",
    ),
    longDesc="""
606
""",
)

entry(
    index=137,
    label="INDENE + H <=> A1 + H2CCCH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(203705, "J/mol"),
        T0=(1, "K"),
        comment="607",
    ),
    longDesc="""
607
""",
)

entry(
    index=138,
    label="INDENE + OH <=> C7H7 + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(41572.4, "J/mol"),
        T0=(1, "K"),
        comment="608",
    ),
    longDesc="""
608
""",
)

entry(
    index=139,
    label="INDENE + OH <=> INDENYL + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="609",
    ),
    longDesc="""
609
""",
)

entry(
    index=140,
    label="INDENE + CH3 <=> INDENYL + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(58201.3, "J/mol"),
        T0=(1, "K"),
        comment="610",
    ),
    longDesc="""
610
""",
)

entry(
    index=141,
    label="INDENE + H2CCCH <=> INDENYL + C3H4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.8e10, "cm^3/(mol*s)"),
        n=0,
        Ea=(23032.3, "J/mol"),
        T0=(1, "K"),
        comment="611",
    ),
    longDesc="""
611
""",
)

entry(
    index=142,
    label="INDENE + A1- <=> INDENYL + A1",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(24943.4, "J/mol"),
        T0=(1, "K"),
        comment="612",
    ),
    longDesc="""
612
""",
)

entry(
    index=143,
    label="INDENE + C7H7 <=> INDENYL + C7H8",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(29100.7, "J/mol"),
        T0=(1, "K"),
        comment="613",
    ),
    longDesc="""
613
""",
)

entry(
    index=144,
    label="C5H5 + C4H2 <=> INDENYL",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(41821.8, "J/mol"),
        T0=(1, "K"),
        comment="614",
    ),
    longDesc="""
614
""",
)

entry(
    index=145,
    label="INDENYL => C2H2 + C4H2 + H2CCCH",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e14, "s^-1"),
        n=0,
        Ea=(311793, "J/mol"),
        T0=(1, "K"),
        comment="615",
    ),
    longDesc="""
615
""",
)

entry(
    index=146,
    label="INDENYL + O <=> n-C8H7 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="616",
    ),
    longDesc="""
616
""",
)

entry(
    index=147,
    label="INDENYL + O <=> A1C2H3* + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="617",
    ),
    longDesc="""
617
""",
)

entry(
    index=148,
    label="INDENYL + HO2 => n-C8H7 + CO + OH",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="618",
    ),
    longDesc="""
618
""",
)

entry(
    index=149,
    label="INDENYL + HO2 => A1C2H + CO + H2O",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="619",
    ),
    longDesc="""
619
""",
)

entry(
    index=150,
    label="INDENYL + HO2 => A1C2H3* + CO + OH",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="620",
    ),
    longDesc="""
620
""",
)

entry(
    index=151,
    label="A1- + A1 <=> P2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e23, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(61942.8, "J/mol"),
        T0=(1, "K"),
        comment="621",
    ),
    longDesc="""
621
""",
)

entry(
    index=152,
    label="INDENYL + H2CCCH => P2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(58201.3, "J/mol"),
        T0=(1, "K"),
        comment="622",
    ),
    longDesc="""
622
""",
)

entry(
    index=153,
    label="INDENE + H2CCCH => P2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.55e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(215445, "J/mol"),
        T0=(1, "K"),
        comment="623",
    ),
    longDesc="""
623
""",
)

entry(
    index=154,
    label="A1- + A1- <=> P2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e19, "cm^3/(mol*s)"),
        n=-2.05,
        Ea=(12056, "J/mol"),
        T0=(1, "K"),
        comment="624",
    ),
    longDesc="""
624
""",
)

entry(
    index=155,
    label="A1- + A1- <=> P2- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(0.23, "cm^3/(mol*s)"),
        n=4.62,
        Ea=(120560, "J/mol"),
        T0=(1, "K"),
        comment="625",
    ),
    longDesc="""
625
""",
)

entry(
    index=156,
    label="P2 <=> P2- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e19, "s^-1"),
        n=-2.72,
        Ea=(476419, "J/mol"),
        T0=(1, "K"),
        comment="626",
    ),
    longDesc="""
626
""",
)

entry(
    index=157,
    label="P2 <=> INDENE + C3H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "s^-1"),
        n=0,
        Ea=(457296, "J/mol"),
        T0=(1, "K"),
        comment="627",
    ),
    longDesc="""
627
""",
)

entry(
    index=158,
    label="P2- + O2 <=> A2 + HCO + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="628",
    ),
    longDesc="""
628
""",
)

entry(
    index=159,
    label="P2 + H <=> P2- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="629",
    ),
    longDesc="""
629
""",
)

entry(
    index=160,
    label="P2 + OH <=> P2- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e08, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6402.14, "J/mol"),
        T0=(1, "K"),
        comment="630",
    ),
    longDesc="""
630
""",
)

entry(
    index=161,
    label="i-C4H5 + A1 => A2 + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(12500, "J/mol"),
        T0=(1, "K"),
        comment="631",
    ),
    longDesc="""
631
""",
)

entry(
    index=162,
    label="C4H6 + A1- => A2 + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(5e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(12500, "J/mol"),
        T0=(1, "K"),
        comment="632",
    ),
    longDesc="""
632
""",
)

entry(
    index=163,
    label="A1- + H2CCCCH <=> A2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.18e23, "cm^3/(mol*s)"),
        n=-3.2,
        Ea=(17709.8, "J/mol"),
        T0=(1, "K"),
        comment="633",
    ),
    longDesc="""
633
""",
)

entry(
    index=164,
    label="A1- + H2CCCCH <=> A2- + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e-10, "cm^3/(mol*s)"),
        n=7.1,
        Ea=(6536.75, "J/mol"),
        T0=(1, "K"),
        comment="634",
    ),
    longDesc="""
634
""",
)

entry(
    index=165,
    label="A1- + C4H4 <=> A2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="635",
    ),
    longDesc="""
635
""",
)

entry(
    index=166,
    label="C7H7 + H2CCCH => A2 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(582.013, "J/mol"),
        T0=(1, "K"),
        comment="636",
    ),
    longDesc="""
636
""",
)

entry(
    index=167,
    label="A1C2H- + C2H2 <=> A2-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(42403.8, "J/mol"),
        T0=(1, "K"),
        comment="637",
    ),
    longDesc="""
637
""",
)

entry(
    index=168,
    label="A1C2H3* + C2H2 <=> A2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(27437.8, "J/mol"),
        T0=(1, "K"),
        comment="638",
    ),
    longDesc="""
638
""",
)

entry(
    index=169,
    label="n-C8H7 + C2H2 <=> A2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(22449.1, "J/mol"),
        T0=(1, "K"),
        comment="639",
    ),
    longDesc="""
639
""",
)

entry(
    index=170,
    label="INDENYL + CH3 <=> A2 + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e18, "cm^3/(mol*s)"),
        n=0,
        Ea=(303478, "J/mol"),
        T0=(1, "K"),
        comment="640\nRxn 640 commented out because k>Z for T>2000 K",
    ),
    longDesc="""
640
Rxn 640 commented out because k>Z for T>2000 K
""",
)

entry(
    index=171,
    label="INDENE + CH2 => A2 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="641",
    ),
    longDesc="""
641
""",
)

entry(
    index=172,
    label="INDENE + CH2(S) <=> A2 + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="642",
    ),
    longDesc="""
642
""",
)

entry(
    index=173,
    label="A2 + O <=> CH2CO + A1C2H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(18832.3, "J/mol"),
        T0=(1, "K"),
        comment="643",
    ),
    longDesc="""
643
""",
)

entry(
    index=174,
    label="A2 + O => INDENYL + CO + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(3.6e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(183692, "J/mol"),
        T0=(1, "K"),
        comment="644",
    ),
    longDesc="""
644
""",
)

entry(
    index=175,
    label="A2 + O <=> n-C8H7 + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="645",
    ),
    longDesc="""
645
""",
)

entry(
    index=176,
    label="A2 + O <=> A1C2H3* + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="646",
    ),
    longDesc="""
646
""",
)

entry(
    index=177,
    label="A2 + O <=> A2- + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="647",
    ),
    longDesc="""
647
""",
)

entry(
    index=178,
    label="A2 + H <=> A2- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="648",
    ),
    longDesc="""
648
""",
)

entry(
    index=179,
    label="A2 + OH <=> A2- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(19123.3, "J/mol"),
        T0=(1, "K"),
        comment="649",
    ),
    longDesc="""
649
""",
)

entry(
    index=180,
    label="A2 + OH => A1C2H + CH2CO + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(44066.7, "J/mol"),
        T0=(1, "K"),
        comment="650",
    ),
    longDesc="""
650
""",
)

entry(
    index=181,
    label="A2 + CH3 <=> A2- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="651",
    ),
    longDesc="""
651
""",
)

entry(
    index=182,
    label="A2 + C2H <=> A2- + C2H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="652",
    ),
    longDesc="""
652
""",
)

entry(
    index=183,
    label="A2 + C2H <=> A2C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="653",
    ),
    longDesc="""
653
""",
)

entry(
    index=184,
    label="A2- + O2 => A1C2H + HCO + CO",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="654",
    ),
    longDesc="""
654
""",
)

entry(
    index=185,
    label="A2- + O => INDENYL + CO",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="655",
    ),
    longDesc="""
655
""",
)

entry(
    index=186,
    label="A2- + H <=> A2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7.8e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="656",
    ),
    longDesc="""
656
""",
)

entry(
    index=187,
    label="A2- + HO2 => INDENYL + CO + OH",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="657",
    ),
    longDesc="""
657
""",
)

entry(
    index=188,
    label="A2- + C2H2 <=> A2C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.3e24, "cm^3/(mol*s)"),
        n=-3.06,
        Ea=(93953.5, "J/mol"),
        T0=(1, "K"),
        comment="658",
    ),
    longDesc="""
658
""",
)

entry(
    index=189,
    label="A2C2H + H <=> A2C2H* + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="659",
    ),
    longDesc="""
659
""",
)

entry(
    index=190,
    label="A2C2H + OH <=> A2- + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(0.000218, "cm^3/(mol*s)"),
        n=4.5,
        Ea=(-4157.24, "J/mol"),
        T0=(1, "K"),
        comment="660",
    ),
    longDesc="""
660
""",
)

entry(
    index=191,
    label="A2C2H + OH <=> A2C2H* + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(19123.3, "J/mol"),
        T0=(1, "K"),
        comment="661",
    ),
    longDesc="""
661
""",
)

entry(
    index=192,
    label="INDENYL + H2CCCH => A2C2H + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(6e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="662",
    ),
    longDesc="""
662
""",
)

entry(
    index=193,
    label="A2 + CH2 <=> A2CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="663",
    ),
    longDesc="""
663
""",
)

entry(
    index=194,
    label="A2 + CH2(S) <=> A2CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(36334.2, "J/mol"),
        T0=(1, "K"),
        comment="664",
    ),
    longDesc="""
664
""",
)

entry(
    index=195,
    label="A2CH3 <=> A2- + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e16, "s^-1"),
        n=0,
        Ea=(405746, "J/mol"),
        T0=(1, "K"),
        comment="665",
    ),
    longDesc="""
665
""",
)

entry(
    index=196,
    label="A2CH3 <=> A2CH2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.81e15, "s^-1"),
        n=0,
        Ea=(371657, "J/mol"),
        T0=(1, "K"),
        comment="666",
    ),
    longDesc="""
666
""",
)

entry(
    index=197,
    label="A2CH3 + O2 <=> A2CH2 + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(173008, "J/mol"),
        T0=(1, "K"),
        comment="667",
    ),
    longDesc="""
667
""",
)

entry(
    index=198,
    label="A2CH3 + O <=> A2CH2 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(5379.46, "J/mol"),
        T0=(1, "K"),
        comment="668",
    ),
    longDesc="""
668
""",
)

entry(
    index=199,
    label="A2CH3 + H <=> A2CH2 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(398, "cm^3/(mol*s)"),
        n=3.44,
        Ea=(12970.6, "J/mol"),
        T0=(1, "K"),
        comment="669",
    ),
    longDesc="""
669
""",
)

entry(
    index=200,
    label="A2CH3 + H <=> A2 + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(21201.9, "J/mol"),
        T0=(1, "K"),
        comment="670",
    ),
    longDesc="""
670
""",
)

entry(
    index=201,
    label="A2CH3 + OH <=> A2CH2 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.19e08, "cm^3/(mol*s)"),
        n=1,
        Ea=(3658.37, "J/mol"),
        T0=(1, "K"),
        comment="671",
    ),
    longDesc="""
671
""",
)

entry(
    index=202,
    label="A2CH3 + HO2 <=> A2CH2 + H2O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(58201.3, "J/mol"),
        T0=(1, "K"),
        comment="672",
    ),
    longDesc="""
672
""",
)

entry(
    index=203,
    label="A2CH3 + CH3 <=> A2CH2 + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.58e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(45729.6, "J/mol"),
        T0=(1, "K"),
        comment="673",
    ),
    longDesc="""
673
""",
)

entry(
    index=204,
    label="A2CH2 + O <=> A2- + CH2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.65e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="674",
    ),
    longDesc="""
674
""",
)

entry(
    index=205,
    label="A2CH2 + HO2 <=> A2- + CH2O + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="675",
    ),
    longDesc="""
675
""",
)

entry(
    index=206,
    label="A2CH2 + CH2 <=> A2C2H + H2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.4e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="676",
    ),
    longDesc="""
676
""",
)

entry(
    index=207,
    label="A2CH2 + H2CCCH <=> A3 + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(58201.3, "J/mol"),
        T0=(1, "K"),
        comment="677",
    ),
    longDesc="""
677
""",
)

entry(
    index=208,
    label="A1C2H- + C4H4 <=> A2R5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(27437.8, "J/mol"),
        T0=(1, "K"),
        comment="678",
    ),
    longDesc="""
678
""",
)

entry(
    index=209,
    label="A1C2H3* + C4H2 <=> A2R5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(22449.1, "J/mol"),
        T0=(1, "K"),
        comment="679",
    ),
    longDesc="""
679
""",
)

entry(
    index=210,
    label="n-C8H7 + C4H2 <=> A2R5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(22449.1, "J/mol"),
        T0=(1, "K"),
        comment="680",
    ),
    longDesc="""
680
""",
)

entry(
    index=211,
    label="INDENYL + H2CCCH => A2R5 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(8.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(40643.6, "J/mol"),
        T0=(1, "K"),
        comment="681",
    ),
    longDesc="""
681
""",
)

entry(
    index=212,
    label="INDENE + H2CCCH => A2R5 + H + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.55e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(215445, "J/mol"),
        T0=(1, "K"),
        comment="682",
    ),
    longDesc="""
682
""",
)

entry(
    index=213,
    label="INDENYL + H2CCCH <=> A2R5 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9.5e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="683",
    ),
    longDesc="""
683
""",
)

entry(
    index=214,
    label="A2- + C2H2 <=> A2R5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.9e31, "cm^3/(mol*s)"),
        n=-5.26,
        Ea=(87302, "J/mol"),
        T0=(1, "K"),
        comment="684",
    ),
    longDesc="""
684
""",
)

entry(
    index=215,
    label="A2C2H* + H <=> A2R5",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="685",
    ),
    longDesc="""
685
""",
)

entry(
    index=216,
    label="A2C2H + H <=> A2R5 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.6e37, "cm^3/(mol*s)"),
        n=-7.03,
        Ea=(96032.2, "J/mol"),
        T0=(1, "K"),
        comment="686",
    ),
    longDesc="""
686
""",
)

entry(
    index=217,
    label="A2R5- + H <=> A2R5",
    degeneracy=1,
    kinetics=Troe(
        arrheniusHigh=Arrhenius(
            A=(1e14, "cm^3/(mol*s)"), n=0, Ea=(0, "J/mol"), T0=(1, "K")
        ),
        arrheniusLow=Arrhenius(
            A=(6.6e75, "cm^6/(mol^2*s)"),
            n=-16.3,
            Ea=(29.1007, "J/mol"),
            T0=(1, "K"),
        ),
        alpha=1,
        T3=(0.1, "K"),
        T1=(585, "K"),
        T2=(6113, "K"),
        efficiencies={
            "C": 3,
            "O=C=O": 1.5,
            "CC": 3,
            "O": 6.5,
            "[O][O]": 0.4,
            "[C-]#[O+]": 0.75,
            "[Ar]": 0.2,
        },
        comment="687",
    ),
    longDesc="""
687
""",
)

entry(
    index=218,
    label="A2R5 <=> A1C2H + C4H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e16, "s^-1"),
        n=0,
        Ea=(482239, "J/mol"),
        T0=(1, "K"),
        comment="688",
    ),
    longDesc="""
688
""",
)

entry(
    index=219,
    label="A2R5 + O <=> A2R5- + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="689",
    ),
    longDesc="""
689
""",
)

entry(
    index=220,
    label="A2R5 + O => A2- + HCCO",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="690",
    ),
    longDesc="""
690
""",
)

entry(
    index=221,
    label="A2R5 + H <=> A2R5- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="691",
    ),
    longDesc="""
691
""",
)

entry(
    index=222,
    label="A2R5 + OH <=> A2R5- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e08, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6027.99, "J/mol"),
        T0=(1, "K"),
        comment="692",
    ),
    longDesc="""
692
""",
)

entry(
    index=223,
    label="A2R5 + OH <=> A2- + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(41572.4, "J/mol"),
        T0=(1, "K"),
        comment="693",
    ),
    longDesc="""
693
""",
)

entry(
    index=224,
    label="A1C2H + A1- <=> A3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e23, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="694",
    ),
    longDesc="""
694
""",
)

entry(
    index=225,
    label="A1C2H- + A1 <=> A3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e23, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="695",
    ),
    longDesc="""
695
""",
)

entry(
    index=226,
    label="A2- + C4H4 <=> A3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="696",
    ),
    longDesc="""
696
""",
)

entry(
    index=227,
    label="A2- + C4H2 <=> A3-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="697",
    ),
    longDesc="""
697
""",
)

entry(
    index=228,
    label="P2- + C2H2 <=> A3 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.64e06, "cm^3/(mol*s)"),
        n=1.97,
        Ea=(30181.5, "J/mol"),
        T0=(1, "K"),
        comment="698",
    ),
    longDesc="""
698
""",
)

entry(
    index=229,
    label="A2C2H* + C2H2 <=> A3-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e62, "cm^3/(mol*s)"),
        n=-14.56,
        Ea=(137605, "J/mol"),
        T0=(1, "K"),
        comment="699",
    ),
    longDesc="""
699
""",
)

entry(
    index=230,
    label="A2R5- + C2H2 <=> A3-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="700",
    ),
    longDesc="""
700
""",
)

entry(
    index=231,
    label="A2R5 + C2H2 => A3",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(27650, "cm^3/(mol*s)"),
        n=2.45,
        Ea=(121682, "J/mol"),
        T0=(1, "K"),
        comment="701",
    ),
    longDesc="""
701
""",
)

entry(
    index=232,
    label="A2 + C4H2 => A3",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(27650, "cm^3/(mol*s)"),
        n=2.45,
        Ea=(121682, "J/mol"),
        T0=(1, "K"),
        comment="702",
    ),
    longDesc="""
702
""",
)

entry(
    index=233,
    label="A3 + O <=> A2C2H + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(22989.5, "J/mol"),
        T0=(1, "K"),
        comment="703",
    ),
    longDesc="""
703
""",
)

entry(
    index=234,
    label="A3 + O <=> A3- + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="704",
    ),
    longDesc="""
704
""",
)

entry(
    index=235,
    label="A3 + O => HCCO + P2-",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="705",
    ),
    longDesc="""
705
""",
)

entry(
    index=236,
    label="A3 + H <=> A3- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="706",
    ),
    longDesc="""
706
""",
)

entry(
    index=237,
    label="A3 + OH <=> A3- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.7e8, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6260.8, "J/mol"),
        T0=(1, "K"),
        comment="707\nRxn 707 commented out because k>Z for T>2000 K",
    ),
    longDesc="""
707
Rxn 707 commented out because k>Z for T>2000 K
""",
)

entry(
    index=238,
    label="A3 + OH => A2C2H + CH2CO + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(41572.4, "J/mol"),
        T0=(1, "K"),
        comment="708",
    ),
    longDesc="""
708
""",
)

entry(
    index=239,
    label="A3 + OH <=> CH2CO + P2-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(133032, "J/mol"),
        T0=(1, "K"),
        comment="709",
    ),
    longDesc="""
709
""",
)

entry(
    index=240,
    label="A3 + CH3 <=> A3- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="710",
    ),
    longDesc="""
710
""",
)

entry(
    index=241,
    label="A3 + C2H <=> A3C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="711",
    ),
    longDesc="""
711
""",
)

entry(
    index=242,
    label="A3C2H + H <=> A3C2H* + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(303, "cm^3/(mol*s)"),
        n=3.3,
        Ea=(23862.5, "J/mol"),
        T0=(1, "K"),
        comment="712",
    ),
    longDesc="""
712
""",
)

entry(
    index=243,
    label="A3C2H + OH <=> A3- + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(0.000218, "cm^3/(mol*s)"),
        n=4.5,
        Ea=(-4157.24, "J/mol"),
        T0=(1, "K"),
        comment="713",
    ),
    longDesc="""
713
""",
)

entry(
    index=244,
    label="A3- + O2 => CO + HCO + A2R5",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="714",
    ),
    longDesc="""
714
""",
)

entry(
    index=245,
    label="A3- + H <=> A3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="715",
    ),
    longDesc="""
715
""",
)

entry(
    index=246,
    label="A3- + C2H2 <=> A3C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e26, "cm^3/(mol*s)"),
        n=-3.44,
        Ea=(125549, "J/mol"),
        T0=(1, "K"),
        comment="716",
    ),
    longDesc="""
716
""",
)

entry(
    index=247,
    label="A3 + CH2 <=> A3CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(29898.8, "J/mol"),
        T0=(1, "K"),
        comment="717",
    ),
    longDesc="""
717
""",
)

entry(
    index=248,
    label="A3 + CH2(S) <=> A3CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(29898.8, "J/mol"),
        T0=(1, "K"),
        comment="718",
    ),
    longDesc="""
718
""",
)

entry(
    index=249,
    label="A3CH2 + H <=> A3- + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e16, "cm^3/(mol*s)"),
        n=0,
        Ea=(405746, "J/mol"),
        T0=(1, "K"),
        comment="719",
    ),
    longDesc="""
719
""",
)

entry(
    index=250,
    label="A3CH3 <=> A3CH2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.81e15, "s^-1"),
        n=0,
        Ea=(371657, "J/mol"),
        T0=(1, "K"),
        comment="720",
    ),
    longDesc="""
720
""",
)

entry(
    index=251,
    label="A3CH3 + O2 <=> A3CH2 + HO2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(173008, "J/mol"),
        T0=(1, "K"),
        comment="721",
    ),
    longDesc="""
721
""",
)

entry(
    index=252,
    label="A3CH3 + O <=> A3CH2 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(5342.05, "J/mol"),
        T0=(1, "K"),
        comment="722",
    ),
    longDesc="""
722
""",
)

entry(
    index=253,
    label="A3CH2 + O <=> A3- + CH2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.65e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="723",
    ),
    longDesc="""
723
""",
)

entry(
    index=254,
    label="A3CH3 + H <=> A3CH2 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(34920.8, "J/mol"),
        T0=(1, "K"),
        comment="724",
    ),
    longDesc="""
724
""",
)

entry(
    index=255,
    label="A3CH3 + H <=> A3 + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(21201.9, "J/mol"),
        T0=(1, "K"),
        comment="725",
    ),
    longDesc="""
725
""",
)

entry(
    index=256,
    label="A3CH3 + OH <=> A3CH2 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.26e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(10601, "J/mol"),
        T0=(1, "K"),
        comment="726",
    ),
    longDesc="""
726
""",
)

entry(
    index=257,
    label="A3CH3 + HO2 <=> A3CH2 + H2O2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(58201.3, "J/mol"),
        T0=(1, "K"),
        comment="727",
    ),
    longDesc="""
727
""",
)

entry(
    index=258,
    label="A3CH3 + CH3 <=> A3CH2 + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.58e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(45729.6, "J/mol"),
        T0=(1, "K"),
        comment="728",
    ),
    longDesc="""
728
""",
)

entry(
    index=259,
    label="A3CH2 + HO2 => A3- + CH2O + OH",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(8e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="729",
    ),
    longDesc="""
729
""",
)

entry(
    index=260,
    label="A3CH2 + CH2 <=> A4 + H2 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.4e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="730",
    ),
    longDesc="""
730
""",
)

entry(
    index=261,
    label="C4H2 + A2R5 => A4",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(500, "cm^3/(mol*s)"),
        n=2.2313,
        Ea=(-4732.35, "J/mol"),
        T0=(1, "K"),
        comment="731",
    ),
    longDesc="""
731
""",
)

entry(
    index=262,
    label="A1C2H + A1C2H- <=> A4 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="732",
    ),
    longDesc="""
732
""",
)

entry(
    index=263,
    label="n-C8H7 + A1C2H => A4 + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="733",
    ),
    longDesc="""
733
""",
)

entry(
    index=264,
    label="A1C2H3* + A1C2H => A4 + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="734",
    ),
    longDesc="""
734
""",
)

entry(
    index=265,
    label="INDENYL + C7H7 => A4 + H2 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(4.3e37, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="735",
    ),
    longDesc="""
735
""",
)

entry(
    index=266,
    label="INDENYL + INDENYL => A4 + C2H2 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(4.3e36, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="736",
    ),
    longDesc="""
736
""",
)

entry(
    index=267,
    label="A2 + C6H <=> A4-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="737",
    ),
    longDesc="""
737
""",
)

entry(
    index=268,
    label="A2 + A1- <=> A4 + H + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e11, "cm^3/(mol*s)"),
        n=0,
        Ea=(20786.2, "J/mol"),
        T0=(1, "K"),
        comment="738",
    ),
    longDesc="""
738
""",
)

entry(
    index=269,
    label="A2- + A1 <=> A4 + H + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(20786.2, "J/mol"),
        T0=(1, "K"),
        comment="739",
    ),
    longDesc="""
739
""",
)

entry(
    index=270,
    label="A2- + A1- => A4 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(4.3e37, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="740",
    ),
    longDesc="""
740
""",
)

entry(
    index=271,
    label="A2- + C6H2 <=> A4-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="741",
    ),
    longDesc="""
741
""",
)

entry(
    index=272,
    label="A2C2H* + C4H4 <=> A4 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="742",
    ),
    longDesc="""
742
""",
)

entry(
    index=273,
    label="A2R5- + C4H2 => A4-",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="743",
    ),
    longDesc="""
743
""",
)

entry(
    index=274,
    label="A2R5- + H2CCCCH <=> A4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.4e23, "cm^3/(mol*s)"),
        n=-3.2,
        Ea=(17709.8, "J/mol"),
        T0=(1, "K"),
        comment="744",
    ),
    longDesc="""
744
""",
)

entry(
    index=275,
    label="A3- + C2H2 <=> A4 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6.6e24, "cm^3/(mol*s)"),
        n=-3.36,
        Ea=(73998.8, "J/mol"),
        T0=(1, "K"),
        comment="745",
    ),
    longDesc="""
745
""",
)

entry(
    index=276,
    label="A3C2H + H <=> A4 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(9e38, "cm^3/(mol*s)"),
        n=-7.39,
        Ea=(86470.5, "J/mol"),
        T0=(1, "K"),
        comment="746",
    ),
    longDesc="""
746
""",
)

entry(
    index=277,
    label="A4 + O <=> A3- + HCCO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="747",
    ),
    longDesc="""
747
""",
)

entry(
    index=278,
    label="A4 + H <=> A4- + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="748",
    ),
    longDesc="""
748
""",
)

entry(
    index=279,
    label="A4 + OH <=> A4- + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.7e08, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6092.6, "J/mol"),
        T0=(1, "K"),
        comment="749",
    ),
    longDesc="""
749
""",
)

entry(
    index=280,
    label="A4 + OH <=> A3- + CH2CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="750",
    ),
    longDesc="""
750
""",
)

entry(
    index=281,
    label="A4 + CH3 <=> A4- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(303, "cm^3/(mol*s)"),
        n=3.3,
        Ea=(23862.5, "J/mol"),
        T0=(1, "K"),
        comment="751",
    ),
    longDesc="""
751
""",
)

entry(
    index=282,
    label="A4- + O2 <=> CO + CO + A3-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="752",
    ),
    longDesc="""
752
""",
)

entry(
    index=283,
    label="A4- + H <=> A4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="753",
    ),
    longDesc="""
753
""",
)

entry(
    index=284,
    label="A4- + C2H2 <=> A4C2H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.2e26, "cm^3/(mol*s)"),
        n=-3.44,
        Ea=(125549, "J/mol"),
        T0=(1, "K"),
        comment="754",
    ),
    longDesc="""
754
""",
)

entry(
    index=285,
    label="A4C2H + H <=> A4C2H* + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(66515.8, "J/mol"),
        T0=(1, "K"),
        comment="755",
    ),
    longDesc="""
755
""",
)

entry(
    index=286,
    label="A4C2H + H <=> BGHIF + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(4.6e37, "cm^3/(mol*s)"),
        n=-7.03,
        Ea=(96032.2, "J/mol"),
        T0=(1, "K"),
        comment="756",
    ),
    longDesc="""
756
""",
)

entry(
    index=287,
    label="A4C2H* + H <=> BGHIF",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="757",
    ),
    longDesc="""
757
""",
)

entry(
    index=288,
    label="P2 + C6H <=> C18H11",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="758",
    ),
    longDesc="""
758
""",
)

entry(
    index=289,
    label="P2- + C6H2 <=> BGHIF + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="759",
    ),
    longDesc="""
759
""",
)

entry(
    index=290,
    label="P2- + C6H2 <=> C18H11",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="760",
    ),
    longDesc="""
760
""",
)

entry(
    index=291,
    label="A3- + C4H4 <=> C18H12 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="761",
    ),
    longDesc="""
761
""",
)

entry(
    index=292,
    label="A3C2H* + C2H2 <=> BGHIF + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.6e16, "cm^3/(mol*s)"),
        n=-1.33,
        Ea=(27437.8, "J/mol"),
        T0=(1, "K"),
        comment="762",
    ),
    longDesc="""
762
""",
)

entry(
    index=293,
    label="A2R5 + C6H2 => BGHIF",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(241.3, "cm^3/(mol*s)"),
        n=2.2313,
        Ea=(-4730.93, "J/mol"),
        T0=(1, "K"),
        comment="763",
    ),
    longDesc="""
763
""",
)

entry(
    index=294,
    label="A1C2H- + A2 => BGHIF + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2.1e25, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="764",
    ),
    longDesc="""
764
""",
)

entry(
    index=295,
    label="A1C2H + A2- => BGHIF + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2.1e25, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="765",
    ),
    longDesc="""
765
""",
)

entry(
    index=296,
    label="INDENE + INDENYL => C18H12 + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="766",
    ),
    longDesc="""
766
""",
)

entry(
    index=297,
    label="INDENYL + INDENYL => BGHIF + H2 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(8.3e38, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="767",
    ),
    longDesc="""
767
""",
)

entry(
    index=298,
    label="A2 + C8H2 => BGHIF",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(241.3, "cm^3/(mol*s)"),
        n=2.2313,
        Ea=(-4731.77, "J/mol"),
        T0=(1, "K"),
        comment="768",
    ),
    longDesc="""
768
""",
)

entry(
    index=299,
    label="A2C2H + A1- <=> C18H12 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="769",
    ),
    longDesc="""
769
""",
)

entry(
    index=300,
    label="A2C2H* + A1 <=> C18H12 + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="770",
    ),
    longDesc="""
770
""",
)

entry(
    index=301,
    label="A2R5- + A1 => BGHIF + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.1e25, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="771",
    ),
    longDesc="""
771
""",
)

entry(
    index=302,
    label="A3C2H* + C4H4 <=> BAPYR + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="772",
    ),
    longDesc="""
772
""",
)

entry(
    index=303,
    label="A4- + C4H4 <=> BAPYR + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3.3e33, "cm^3/(mol*s)"),
        n=-5.7,
        Ea=(106010, "J/mol"),
        T0=(1, "K"),
        comment="773",
    ),
    longDesc="""
773
""",
)

entry(
    index=304,
    label="A4C2H* + C2H2 <=> BAPYR*S",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(7e37, "cm^3/(mol*s)"),
        n=-8.02,
        Ea=(68178.7, "J/mol"),
        T0=(1, "K"),
        comment="774",
    ),
    longDesc="""
774
""",
)

entry(
    index=305,
    label="BAPYR*S + H <=> BAPYR",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="775",
    ),
    longDesc="""
775
""",
)

entry(
    index=306,
    label="P2 + A1C2H- => BAPYR + H2 + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.1e24, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="776",
    ),
    longDesc="""
776
""",
)

entry(
    index=307,
    label="P2- + A1C2H3* => BAPYR + H2 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(8.3e38, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="777",
    ),
    longDesc="""
777
""",
)

entry(
    index=308,
    label="P2- + n-C8H7 => BAPYR + H2 + H2",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(8.3e38, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="778",
    ),
    longDesc="""
778
""",
)

entry(
    index=309,
    label="A2R5- + A1C2H- <=> BAPYR",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(8.3e38, "cm^3/(mol*s)"),
        n=-6.3,
        Ea=(187325, "J/mol"),
        T0=(1, "K"),
        comment="779",
    ),
    longDesc="""
779
""",
)

entry(
    index=310,
    label="A2R5 + A1C2H- <=> BAPYR + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e25, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="780",
    ),
    longDesc="""
780
""",
)

entry(
    index=311,
    label="A2R5- + A1C2H <=> BAPYR + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e25, "cm^3/(mol*s)"),
        n=-2.92,
        Ea=(66598.9, "J/mol"),
        T0=(1, "K"),
        comment="781",
    ),
    longDesc="""
781
""",
)

entry(
    index=312,
    label="C18H11 + O2 => HCO + CO + A4",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="782",
    ),
    longDesc="""
782
""",
)

entry(
    index=313,
    label="C18H11 + H <=> BGHIF + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e14, "cm^3/(mol*s)"),
        n=0,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="783",
    ),
    longDesc="""
783
""",
)

entry(
    index=314,
    label="C18H11 + C2H => BAPYR",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(5.24e14, "cm^3/(mol*s)"),
        n=-0.5,
        Ea=(2910.07, "J/mol"),
        T0=(1, "K"),
        comment="784",
    ),
    longDesc="""
784
""",
)

entry(
    index=315,
    label="C18H11 + C2H2 <=> BAPYR + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.1e24, "cm^3/(mol*s)"),
        n=-3.36,
        Ea=(73998.8, "J/mol"),
        T0=(1, "K"),
        comment="785",
    ),
    longDesc="""
785
""",
)

entry(
    index=316,
    label="C18H12 + O <=> C18H11 + OH",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="786",
    ),
    longDesc="""
786
""",
)

entry(
    index=317,
    label="C18H12 + H <=> C18H11 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(303, "cm^3/(mol*s)"),
        n=3.3,
        Ea=(23862.5, "J/mol"),
        T0=(1, "K"),
        comment="787",
    ),
    longDesc="""
787
""",
)

entry(
    index=318,
    label="C18H12 + OH <=> C18H11 + H2O",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.7e08, "cm^3/(mol*s)"),
        n=1.42,
        Ea=(6092.6, "J/mol"),
        T0=(1, "K"),
        comment="788",
    ),
    longDesc="""
788
""",
)

entry(
    index=319,
    label="BGHIF + O <=> HCCO + A4-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(61527.1, "J/mol"),
        T0=(1, "K"),
        comment="789",
    ),
    longDesc="""
789
""",
)

entry(
    index=320,
    label="BGHIF + OH <=> CH2CO + A4-",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(44066.7, "J/mol"),
        T0=(1, "K"),
        comment="790",
    ),
    longDesc="""
790
""",
)

entry(
    index=321,
    label="BAPYR*S + O2 => HCO + CO + BGHIF",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(30763.5, "J/mol"),
        T0=(1, "K"),
        comment="791",
    ),
    longDesc="""
791
""",
)

entry(
    index=322,
    label="C4H2 + A4 => BAPYR",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(600, "cm^3/(mol*s)"),
        n=2.2313,
        Ea=(-4732.35, "J/mol"),
        T0=(1, "K"),
        comment="792",
    ),
    longDesc="""
792
""",
)

entry(
    index=323,
    label="BAPYR + O <=> HCCO + C18H11",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(174604, "J/mol"),
        T0=(1, "K"),
        comment="793",
    ),
    longDesc="""
793
""",
)

entry(
    index=324,
    label="BAPYR + OH => CH2CO + C18H11",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(1.3e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(44066.7, "J/mol"),
        T0=(1, "K"),
        comment="794",
    ),
    longDesc="""
794
""",
)

entry(
    index=325,
    label="C5H5 + C5H5 <=> A2 + H + H",
    degeneracy=1,
    kinetics=MultiArrhenius(
        arrhenius=[
            Arrhenius(
                A=(3e16, "cm^3/(mol*s)"),
                n=0,
                Ea=(196429, "J/mol"),
                T0=(1, "K"),
                comment="795\n796\n797\n798\n799\n800\n801\n802\n803\n804\n805\n806\n807\n808\n809\n810",
            ),
            Arrhenius(
                A=(453000, "cm^3/(mol*s)"),
                n=1.83,
                Ea=(150001, "J/mol"),
                T0=(1, "K"),
                comment="811",
            ),
        ],
    ),
)

entry(
    index=326,
    label="C5H5 + H2CCCH <=> A1C2H3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(34704.6, "J/mol"),
        T0=(1, "K"),
        comment="812",
    ),
    longDesc="""
812
""",
)

entry(
    index=327,
    label="C5H5 + H2CCCCH <=> INDENE",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1e13, "cm^3/(mol*s)"),
        n=0,
        Ea=(34704.6, "J/mol"),
        T0=(1, "K"),
        comment="813",
    ),
    longDesc="""
813
""",
)

entry(
    index=328,
    label="C5H5 + C5H5 <=> INDENYL + CH3",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2.5e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(40000.9, "J/mol"),
        T0=(1, "K"),
        comment="814",
    ),
    longDesc="""
814
""",
)

entry(
    index=329,
    label="C5H6 + CH3 <=> C5H5 + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(0.1, "cm^3/(mol*s)"),
        n=4,
        Ea=(0, "J/mol"),
        T0=(1, "K"),
        comment="815",
    ),
    longDesc="""
815
""",
)

entry(
    index=330,
    label="n-C8H7 + A1C2H- => A4 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(3e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="816\nC5H5+C5H6 = INDENE+CH3 9.630E+13 1.6300 29972.00\n817",
    ),
    longDesc="""
816
C5H5+C5H6 = INDENE+CH3 9.630E+13 1.6300 29972.00
817
""",
)

entry(
    index=331,
    label="INDENYL + C5H5 => A3 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(3e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="818",
    ),
    longDesc="""
818
""",
)

entry(
    index=332,
    label="INDENYL + INDENYL => C18H12 + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="819",
    ),
    longDesc="""
819
""",
)

entry(
    index=333,
    label="A1C2H3* + A1C2H- <=> A4 + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="820",
    ),
    longDesc="""
820
""",
)

entry(
    index=334,
    label="A2C2H* + n-C8H7 <=> BAPYR + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="821",
    ),
    longDesc="""
821
""",
)

entry(
    index=335,
    label="A2C2H* + A1C2H3* <=> BAPYR + H + H",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="822",
    ),
    longDesc="""
822
""",
)

entry(
    index=336,
    label="A2R5- + A1- => BGHIF + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="823",
    ),
    longDesc="""
823
""",
)

entry(
    index=337,
    label="P2- + A1C2H- => BAPYR + H + H",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(6e17, "cm^3/(mol*s)"),
        n=0,
        Ea=(196429, "J/mol"),
        T0=(1, "K"),
        comment="824",
    ),
    longDesc="""
824
""",
)

entry(
    index=338,
    label="A1C2H3 + CH3 <=> A1C2H3* + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="825",
    ),
    longDesc="""
825
""",
)

entry(
    index=339,
    label="A2R5 + CH3 <=> A2R5- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="826",
    ),
    longDesc="""
826
""",
)

entry(
    index=340,
    label="P2 + CH3 <=> P2- + CH4",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(2e12, "cm^3/(mol*s)"),
        n=0,
        Ea=(62608, "J/mol"),
        T0=(1, "K"),
        comment="827",
    ),
    longDesc="""
827
""",
)

entry(
    index=341,
    label="A1 + O <=> C5H6 + CO",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(5.8e16, "cm^3/(mol*s)"),
        n=-0.77,
        Ea=(63564.1, "J/mol"),
        T0=(1, "K"),
        comment="828",
    ),
    longDesc="""
828
""",
)

entry(
    index=342,
    label="A2R5 + OH => A2 + HCCO",
    degeneracy=1,
    reversible=False,
    kinetics=Arrhenius(
        A=(176, "cm^3/(mol*s)"),
        n=3.25,
        Ea=(23240.6, "J/mol"),
        T0=(1, "K"),
        comment="829",
    ),
    longDesc="""
829
""",
)

entry(
    index=343,
    label="A1C2H3* + CH3 <=> INDENE + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(3e18, "cm^3/(mol*s)"),
        n=0,
        Ea=(303478, "J/mol"),
        T0=(1, "K"),
        comment="830",
    ),
    longDesc="""
830
""",
)

entry(
    index=344,
    label="C7H7 + CH3 <=> A1C2H3 + H2",
    degeneracy=1,
    kinetics=Arrhenius(
        A=(1.06e26, "cm^3/(mol*s)"),
        n=-4,
        Ea=(22033.4, "J/mol"),
        T0=(1, "K"),
        comment="831",
    ),
    longDesc="""
831
""",
)
