#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["XSYJ"], products=["SY", "XJ"], ownReverse=False)

reverse = "Ring_OpeningS"
reversible = True

recipe(
    actions=[
        ["BREAK_BOND", "*1", 1, "*2"],
        ["FORM_BOND", "*1", 1, "*3"],
        ["GAIN_RADICAL", "*2", "1"],
        ["LOSE_RADICAL", "*3", "1"],
    ]
)

boundaryAtoms = ["*1", "*3"]

entry(
    index=0,
    label="XSYJ",
    group="OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics=None,
)

entry(
    index=1,
    label="YJ",
    group="""
1 *3 R!H u1
""",
    kinetics=None,
)

entry(
    index=2,
    label="S-RR",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 R   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=3,
    label="XSR3J",
    group="""
1 *4 R!H u0 {2,S} {3,[S,D]}
2 *1 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,[S,D]}
4 *2 R   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=4,
    label="XSR3J_S",
    group="""
1 *4 R!H u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *2 R   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=5,
    label="XSR3J_S_Cs",
    group="""
1 *4 Cs  u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *2 R   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=6,
    label="XSR3J_S_Ss",
    group="""
1 *4 S2s u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *2 R   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=7,
    label="XSR3J_D",
    group="""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *1 S2s u0 p2 c0 {2,S} {4,S}
4 *2 R   u0 {3,S}
""",
    kinetics=None,
)

entry(
    index=8,
    label="XSR4J",
    group="""
1 *4 R!H u0 {2,[S,D]} {3,S}
2 *5 R!H u0 {1,[S,D]} {4,[S,D]}
3 *1 S2s u0 p2 c0 {1,S} {5,S}
4 *3 R!H u1 {2,[S,D]}
5 *2 R   u0 {3,S}
""",
    kinetics=None,
)

entry(
    index=9,
    label="XSR4J_SS",
    group="""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 S2s u0 p2 c0 {3,S} {5,S}
5 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=10,
    label="XSR4J_SD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 S2s u0 p2 c0 {3,S} {5,S}
5 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=11,
    label="XSR4J_DS",
    group="""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 S2s u0 p2 c0 {3,S} {5,S}
5 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=12,
    label="XSR4J_DD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 S2s u0 p2 c0 {3,S} {5,S}
5 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=13,
    label="XSR5J",
    group="""
1 *6 R!H u0 {2,[S,D]} {3,[S,D]}
2 *4 R!H u0 {1,[S,D]} {4,S}
3 *5 R!H u0 {1,[S,D]} {5,[S,D]}
4 *1 S2s u0 p2 c0 {2,S} {6,S}
5 *3 R!H u1 {3,[S,D]}
6 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=14,
    label="XSR5J_SSS",
    group="""
1 *6 R!H u0 {2,S} {3,S}
2 *4 R!H u0 {1,S} {4,S}
3 *5 R!H u0 {1,S} {5,S}
4 *1 S2s u0 p2 c0 {2,S} {6,S}
5 *3 R!H u1 {3,S}
6 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=15,
    label="XSR5J_SSS_CsRCs",
    group="""
1 *6 R!H u0 {2,S} {3,S}
2 *4 Cs  u0 {1,S} {4,S}
3 *5 Cs  u0 {1,S} {5,S}
4 *1 S2s u0 p2 c0 {2,S} {6,S}
5 *3 R!H u1 {3,S}
6 *2 R   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=16,
    label="XSR5J_SSD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=17,
    label="XSR5J_SDS",
    group="""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=18,
    label="XSR5J_DSS",
    group="""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=19,
    label="XSR5J_DDS",
    group="""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=20,
    label="XSR5J_DSD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=21,
    label="XSR5J_SDD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=22,
    label="XSR5J_DDD",
    group="""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 S2s u0 p2 c0 {4,S} {6,S}
6 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=23,
    label="XSR6J",
    group="""
1 *7 R!H u0 {2,[S,D]} {3,[S,D]}
2 *6 R!H u0 {1,[S,D]} {4,[S,D]}
3 *4 R!H u0 {1,[S,D]} {5,S}
4 *5 R!H u0 {2,[S,D]} {6,[S,D]}
5 *1 S2s u0 p2 c0 {3,S} {7,S}
6 *3 R!H u1 {4,[S,D]}
7 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=24,
    label="XSR6J_SSSS",
    group="""
1 *7 R!H u0 {2,S} {3,S}
2 *6 R!H u0 {1,S} {4,S}
3 *4 R!H u0 {1,S} {5,S}
4 *5 R!H u0 {2,S} {6,S}
5 *1 S2s u0 p2 c0 {3,S} {7,S}
6 *3 R!H u1 {4,S}
7 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=25,
    label="XSR6J_SSSS_CsRRCs",
    group="""
1 *7 R!H u0 {2,S} {3,S}
2 *6 R!H u0 {1,S} {4,S}
3 *4 Cs  u0 {1,S} {5,S}
4 *5 Cs  u0 {2,S} {6,S}
5 *1 S2s u0 p2 c0 {3,S} {7,S}
6 *3 R!H u1 {4,S}
7 *2 R   u0 {5,S}
""",
    kinetics=None,
)

entry(
    index=26,
    label="XSR7J",
    group="""
1 *7 R!H u0 {2,[S,D]} {3,[S,D]}
2 *8 R!H u0 {1,[S,D]} {4,[S,D]}
3 *6 R!H u0 {1,[S,D]} {5,[S,D]}
4 *4 R!H u0 {2,[S,D]} {6,S}
5 *5 R!H u0 {3,[S,D]} {7,[S,D]}
6 *1 S2s u0 p2 c0 {4,S} {8,S}
7 *3 R!H u1 {5,[S,D]}
8 *2 R   u0 {6,S}
""",
    kinetics=None,
)

entry(
    index=27,
    label="CJ",
    group="""
1 *3 C u1
""",
    kinetics=None,
)

entry(
    index=28,
    label="CdsJ",
    group="""
1 *3 [Cd,Cdd] u1
""",
    kinetics=None,
)

entry(
    index=29,
    label="CsJ",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=30,
    label="CsJ-Cd",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=31,
    label="CsJ-CdCs",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=32,
    label="CsJ-CdSs",
    group="""
1 *3 Cs  u1 {2,S} {3,S}
2    Cd  u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=33,
    label="CsJ-CdH",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=34,
    label="CsJ-S2s",
    group="""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    R   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=35,
    label="CsJ-SsCs",
    group="""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=36,
    label="CsJ-SsSs",
    group="""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=37,
    label="CsJ-SsH",
    group="""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=38,
    label="CsJ-Cs",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=39,
    label="CsJ-CsCs",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=40,
    label="CsJ-CsH",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=41,
    label="CsJ-HH",
    group="""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=42,
    label="SsJ",
    group="""
1 *3 S2s u1
""",
    kinetics=None,
)

entry(
    index=43,
    label="S-H",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 H   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=44,
    label="S-C",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 C   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=45,
    label="S-Cs",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=46,
    label="S-Cs(NonDe)",
    group="""
1 *2 Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s    u0 p2 c0 {1,S}
3    [H,Cs] u0 {1,S}
4    [H,Cs] u0 {1,S}
5    [H,Cs] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=47,
    label="S-Cs(HHH)",
    group="""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s u0 p2 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=48,
    label="S-Cs(CsHH)",
    group="""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s u0 p2 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=49,
    label="S-Cs(CsCsH)",
    group="""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s u0 p2 c0 {1,S}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=50,
    label="S-Cs(CsCsCs)",
    group="""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s u0 p2 c0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=51,
    label="S-Cs(De)",
    group="""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 S2s              u0 p2 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    R                u0 {1,S}
5    R                u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=52,
    label="S-Cs(OneDe)",
    group="""
1 *1 S2s              u0 p2 c0 {2,S}
2 *2 Cs               u0 {1,S} {3,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=53,
    label="S-Cs(CdHH)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Cd  u0 {2,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=54,
    label="S-Cs(CdCsH)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Cd  u0 {2,S}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=55,
    label="S-Cs(CdCsCs)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Cd  u0 {2,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=56,
    label="S-Cs(CtHH)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Ct  u0 {2,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=57,
    label="S-Cs(CtCsH)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Ct  u0 {2,S}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=58,
    label="S-Cs(CtCsCs)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cs  u0 {1,S} {3,S} {4,S} {5,S}
3    Ct  u0 {2,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=59,
    label="S-Cs(TwoDe)",
    group="""
1 *1 S2s              u0 p2 c0 {2,S}
2 *2 Cs               u0 {1,S} {3,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [H,Cs]           u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=60,
    label="S-Cs(ThreeDe)",
    group="""
1 *1 S2s              u0 p2 c0 {2,S}
2 *2 Cs               u0 {1,S} {3,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=61,
    label="S-Ct",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Ct  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=62,
    label="S-Cb",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cb  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=63,
    label="S-Cd",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cd  u0 {1,S} {3,D}
3    C   u0 {2,D}
""",
    kinetics=None,
)

entry(
    index=64,
    label="S-Cds(H)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cd  u0 {1,S} {3,D} {4,S}
3    C   u0 {2,D}
4    H   u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=65,
    label="S-Cds(Cs)",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 Cd  u0 {1,S} {3,D} {4,S}
3    C   u0 {2,D}
4    Cs  u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=66,
    label="S-S",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 S   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=67,
    label="S-S2s",
    group="""
1 *1 S2s u0 p2 c0 {2,S}
2 *2 S2s u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=68,
    label="S-S2s(H)",
    group="""
1 *2 S2s u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S}
3    H   u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=69,
    label="S-S2s(Cs)",
    group="""
1 *2 S2s u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=70,
    label="S-S2s(S2s)",
    group="""
1 *2 S2s u0 {2,S} {3,S}
2 *1 S2s u0 p2 c0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics=None,
)

tree(
    """
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
            L4: XSR3J_S_Cs
            L4: XSR3J_S_Ss
        L3: XSR3J_D
    L2: XSR4J
        L3: XSR4J_SS
        L3: XSR4J_SD
        L3: XSR4J_DS
        L3: XSR4J_DD
    L2: XSR5J
        L3: XSR5J_SSS
            L4: XSR5J_SSS_CsRCs
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_DSS
        L3: XSR5J_DDS
        L3: XSR5J_DSD
        L3: XSR5J_SDD
        L3: XSR5J_DDD
    L2: XSR6J
        L3: XSR6J_SSSS
            L4: XSR6J_SSSS_CsRRCs
    L2: XSR7J
L1: YJ
    L2: CJ
        L3: CdsJ
        L3: CsJ
            L4: CsJ-Cd
                L5: CsJ-CdCs
                L5: CsJ-CdSs
                L5: CsJ-CdH
            L4: CsJ-S2s
                L5: CsJ-SsCs
                L5: CsJ-SsSs
                L5: CsJ-SsH
            L4: CsJ-Cs
                L5: CsJ-CsCs
                L5: CsJ-CsH
            L4: CsJ-HH
    L2: SsJ
L1: S-RR
    L2: S-H
    L2: S-C
        L3: S-Cs
            L4: S-Cs(NonDe)
                L5: S-Cs(HHH)
                L5: S-Cs(CsHH)
                L5: S-Cs(CsCsH)
                L5: S-Cs(CsCsCs)
            L4: S-Cs(De)
                L5: S-Cs(OneDe)
                    L6: S-Cs(CdHH)
                    L6: S-Cs(CdCsH)
                    L6: S-Cs(CdCsCs)
                    L6: S-Cs(CtHH)
                    L6: S-Cs(CtCsH)
                    L6: S-Cs(CtCsCs)
                L5: S-Cs(TwoDe)
                L5: S-Cs(ThreeDe)
        L3: S-Ct
        L3: S-Cb
        L3: S-Cd
            L4: S-Cds(H)
            L4: S-Cds(Cs)
    L2: S-S
        L3: S-S2s
            L4: S-S2s(H)
            L4: S-S2s(Cs)
            L4: S-S2s(S2s)
"""
)

forbidden(
    label="RR_13",
    group="""
1 *1 R u0 {2,[S,D]}
2 *3 R u1 {1,[S,D]}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="RR_birad",
    group="""
1 *3 R u1 {2,[S,D]}
2    R u1 {1,[S,D]}
""",
    shortDesc="""""",
    longDesc="""

""",
)
