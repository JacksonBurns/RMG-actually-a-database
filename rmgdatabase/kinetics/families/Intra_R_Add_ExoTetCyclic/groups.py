#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_ExoTetCyclic/groups"
shortDesc = ""
longDesc = """

"""

template(
    reactants=["R1_rad_R2_R3"], products=["R1_R2_Cycle", "R3_rad"], ownReverse=False
)

reverse = "Ring_Open_Rad_Addition"

reversible = True
recipe(
    actions=[
        ["BREAK_BOND", "*2", 1, "*3"],
        ["FORM_BOND", "*1", 1, "*2"],
        ["LOSE_RADICAL", "*1", "1"],
        ["GAIN_RADICAL", "*3", "1"],
    ]
)

boundaryAtoms = ["*1", "*2"]

entry(
    index=0,
    label="R1_rad_R2_R3",
    group="OR{R4, R5, R6, R7}",
    kinetics=None,
)

entry(
    index=1,
    label="multiplebond_intra",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S}
2 *3 [C,O,S2s] u0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index=2,
    label="radadd_intra",
    group="""
1 *1 R!H u1
""",
    kinetics=None,
)

entry(
    index=3,
    label="R4",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       u0 {1,[S,D,T,B]} {3,S}
3 *2 [C,O,S2s] u0 c0 {2,S} {4,S}
4 *3 [C,O,S2s] u0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=4,
    label="R4_S",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *2 [C,O,S2s] u0 c0 {2,S} {4,S}
4 *3 [C,O,S2s] u0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=5,
    label="R4_D",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *2 [C,O,S2s] u0 c0 {2,S} {4,S}
4 *3 [C,O,S2s] u0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=6,
    label="R4_T",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *2 [C,O,S2s] u0 c0 {2,S} {4,S}
4 *3 [C,O,S2s] u0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=7,
    label="R4_B",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *2 [C,O,S2s] u0 c0 {2,S} {4,S}
4 *3 [C,O,S2s] u0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=8,
    label="R5",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H       ux {2,[S,D,T,B]} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=9,
    label="R5_SS",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *5 R!H       u0 {2,S} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=10,
    label="R5_SD",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 Cd        u0 {1,S} {3,D}
3 *5 Cd        u0 {2,D} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=11,
    label="R5_DS",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *5 R!H       u0 {2,S} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=12,
    label="R5_ST",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 Ct        u0 {1,S} {3,T}
3 *5 Ct        u0 {2,T} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=13,
    label="R5_TS",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *5 R!H       u0 {2,S} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=14,
    label="R5_SB",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 Cb        u0 {1,S} {3,B}
3 *5 Cb        u0 {2,B} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=15,
    label="R5_BS",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *5 R!H       u0 {2,S} {4,S}
4 *2 [C,O,S2s] u0 c0 {3,S} {5,S}
5 *3 [C,O,S2s] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=16,
    label="R6",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H       ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H       ux {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=17,
    label="R6_RSR",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H       u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H       u0 {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=18,
    label="R6_SSR",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *6 R!H       u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H       u0 {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=19,
    label="R6_SSS",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *5 R!H       u0 {3,S} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=20,
    label="R6_SSM",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 [C,O,S2s]  u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s]  u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=21,
    label="R6_DSR",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *6 R!H       u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H       u0 {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=22,
    label="R6_DSS",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *5 R!H       u0 {3,S} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=23,
    label="R6_DSM",
    group="""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 [C,O,S2s]  u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s]  u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=24,
    label="R6_TSR",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *6 R!H       u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H       u0 {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=25,
    label="R6_TSS",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *5 R!H       u0 {3,S} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=26,
    label="R6_TSM",
    group="""
1 *1 R!H        u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 [C,O,S2s]  u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s]  u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=27,
    label="R6_BSR",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *6 R!H       u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H       u0 {3,[S,D,T,B]} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=28,
    label="R6_BSS",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *5 R!H       u0 {3,S} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=29,
    label="R6_BSM",
    group="""
1 *1 R!H        u1 {2,B}
2 *4 Cb         u0 {1,B} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 [C,O,S2s]  u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s]  u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=30,
    label="R6_SMS",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 [C,O,S2s]  u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s]  u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=31,
    label="R6_SBB",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 Cb        u0 {1,S} {3,B}
3 *6 Cbf       u0 {2,B} {4,B}
4 *5 Cb        u0 {3,B} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=32,
    label="R6_BBS",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cbf       u0 {1,B} {3,B}
3 *6 Cb        u0 {2,B} {4,S}
4 *5 R!H       u0 {3,S} {5,S}
5 *2 [C,O,S2s] u0 c0 {4,S} {6,S}
6 *3 [C,O,S2s] u0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=33,
    label="R7",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H       ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H       ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H       ux {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=34,
    label="R7_RSSR",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=35,
    label="R7_SSSR",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=36,
    label="R7_SSSS",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=37,
    label="R7_SSSM",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=38,
    label="R7_DSSR",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=39,
    label="R7_DSSS",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=40,
    label="R7_DSSM",
    group="""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=41,
    label="R7_TSSR",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=42,
    label="R7_TSSS",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=43,
    label="R7_TSSM",
    group="""
1 *1 R!H        u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=44,
    label="R7_BSSR",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=45,
    label="R7_BSSS",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *6 R!H       u0 {2,S} {4,S}
4 *7 R!H       u0 {3,S} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=46,
    label="R7_BSSM",
    group="""
1 *1 R!H        u1 {2,B}
2 *4 Cb         u0 {1,B} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=47,
    label="R7_RSMS",
    group="""
1 *1 R!H        u1 {2,[S,D,T,B]}
2 *4 R!H        u0 {1,[S,D,T,B]} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=48,
    label="R7_SSMS",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=49,
    label="R7_DSMS",
    group="""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=50,
    label="R7_TSMS",
    group="""
1 *1 R!H        u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=51,
    label="R7_BSMS",
    group="""
1 *1 R!H        u1 {2,B}
2 *4 Cb         u0 {1,B} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=52,
    label="R7_SMSR",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 R!H        u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H        u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=53,
    label="R7_SMSS",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 R!H        u0 {3,S} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=54,
    label="R7_SMSM",
    group="""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=55,
    label="R7_BBSR",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cbf       u0 {1,B} {3,B}
3 *6 Cb        u0 {2,B} {4,S}
4 *7 R!H       u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H       u0 {4,[S,D,T,B]} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=56,
    label="R7_BBSS",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cbf       u0 {1,B} {3,B}
3 *6 Cb        u0 {2,B} {4,S}
4 *7 R!H       u0 {3,S} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=57,
    label="R7_BBSM",
    group="""
1 *1 R!H        u1 {2,B}
2 *4 Cbf        u0 {1,B} {3,B}
3 *6 Cb         u0 {2,B} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 [C,O,S2s]  u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s]  u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=58,
    label="R7_RSBB",
    group="""
1 *1 R!H       u1 {2,[S,D,T,B]}
2 *4 R!H       u0 {1,[S,D,T,B]} {3,S}
3 *6 Cb        u0 {2,S} {4,B}
4 *7 Cbf       u0 {3,B} {5,B}
5 *5 Cb        u0 {4,B} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=59,
    label="R7_SSBB",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 R!H       u0 {1,S} {3,S}
3 *6 Cb        u0 {2,S} {4,B}
4 *7 Cbf       u0 {3,B} {5,B}
5 *5 Cb        u0 {4,B} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=60,
    label="R7_DSBB",
    group="""
1 *1 R!H       u1 {2,D}
2 *4 Cd        u0 {1,D} {3,S}
3 *6 Cb        u0 {2,S} {4,B}
4 *7 Cbf       u0 {3,B} {5,B}
5 *5 Cb        u0 {4,B} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=61,
    label="R7_TSBB",
    group="""
1 *1 R!H       u1 {2,T}
2 *4 Ct        u0 {1,T} {3,S}
3 *6 Cb        u0 {2,S} {4,B}
4 *7 Cbf       u0 {3,B} {5,B}
5 *5 Cb        u0 {4,B} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=62,
    label="R7_BSBB",
    group="""
1 *1 R!H       u1 {2,B}
2 *4 Cb        u0 {1,B} {3,S}
3 *6 Cb        u0 {2,S} {4,B}
4 *7 Cbf       u0 {3,B} {5,B}
5 *5 Cb        u0 {4,B} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=63,
    label="R7_SBBS",
    group="""
1 *1 R!H       u1 {2,S}
2 *4 Cb        u0 {1,S} {3,B}
3 *6 Cbf       u0 {2,B} {4,B}
4 *7 Cb        u0 {3,B} {5,S}
5 *5 R!H       u0 {4,S} {6,S}
6 *2 [C,O,S2s] u0 c0 {5,S} {7,S}
7 *3 [C,O,S2s] u0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=64,
    label="doublebond_intra",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S}
2 *3 C         u0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index=65,
    label="doublebond_intra_NdNd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S}
2 *3 C          u0 c0 {1,S} {3,S} {4,S}
3    [Cs,O,S2s] u0 {2,S}
4    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=66,
    label="doublebond_intra_NdNd_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S2s]       u0 {2,S}
5    [Cs,O,S2s]       u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=67,
    label="doublebond_intra_NdNd_secNd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s] u0 {1,S}
4    [Cs,O,S2s] u0 {2,S}
5    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=68,
    label="doublebond_intra_NdNd_pri",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    H          u0 {1,S}
4    [Cs,O,S2s] u0 {2,S}
5    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=69,
    label="doublebond_intra_NdDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S}
2 *3 C                u0 c0 {1,S} {3,S} {4,S}
3    [Cs,O,S2s]       u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=70,
    label="doublebond_intra_NdDe_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S2s]       u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=71,
    label="doublebond_intra_NdDe_secNd",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s]       u0 {1,S}
4    [Cs,O,S2s]       u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=72,
    label="doublebond_intra_NdDe_pri",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cs,O,S2s]       u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=73,
    label="doublebond_intra_NdCd_pri",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    H          u0 {1,S}
4    [Cs,O,S2s] u0 {2,S}
5    Cd         u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=74,
    label="doublebond_intra_NdCt_pri",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    H          u0 {1,S}
4    [Cs,O,S2s] u0 {2,S}
5    Ct         u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=75,
    label="doublebond_intra_DeDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S}
2 *3 C                u0 c0 {1,S} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=76,
    label="doublebond_intra_DeDe_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=77,
    label="doublebond_intra_DeDe_secNd",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s]       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=78,
    label="doublebond_intra_DeDe_pri",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=79,
    label="doublebond_intra_HDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S}
2 *3 C                u0 c0 {1,S} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=80,
    label="doublebond_intra_HDe_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=81,
    label="doublebond_intra_HDe_secNd",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s]       u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=82,
    label="doublebond_intra_HDe_pri",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    H                u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=83,
    label="doublebond_intra_HCd_pri",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S} {3,S}
2 *3 C         u0 c0 {1,S} {4,S} {5,S}
3    H         u0 {1,S}
4    H         u0 {2,S}
5    Cd        u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=84,
    label="doublebond_intra_HCt_pri",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S} {3,S}
2 *3 C         u0 c0 {1,S} {4,S} {5,S}
3    H         u0 {1,S}
4    H         u0 {2,S}
5    Ct        u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=85,
    label="doublebond_intra_HNd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S}
2 *3 C          u0 c0 {1,S} {3,S} {4,S}
3    H          u0 {2,S}
4    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=86,
    label="doublebond_intra_HNd_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cs,O,S2s]       u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=87,
    label="doublebond_intra_HNd_secNd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s] u0 {1,S}
4    H          u0 {2,S}
5    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=88,
    label="doublebond_intra_HNd_pri",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    H          u0 {1,S}
4    H          u0 {2,S}
5    [Cs,O,S2s] u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=89,
    label="doublebond_intra_2H",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S}
2 *3 C         u0 c0 {1,S} {3,S} {4,S}
3    H         u0 {2,S}
4    H         u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=90,
    label="doublebond_intra_2H_secDe",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 C                u0 c0 {1,S} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    H                u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=91,
    label="doublebond_intra_2H_secNd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 C          u0 c0 {1,S} {4,S} {5,S}
3    [Cs,O,S2s] u0 {1,S}
4    H          u0 {2,S}
5    H          u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=92,
    label="doublebond_intra_2H_pri",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S} {3,S}
2 *3 C         u0 c0 {1,S} {4,S} {5,S}
3    H         u0 {1,S}
4    H         u0 {2,S}
5    H         u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=93,
    label="carbonylbond_intra",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S}
2 *3 [O,S2s]   u0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index=94,
    label="carbonylbond_intra_De",
    group="""
1 *2 [C,O,S2s]        u0 c0 {2,S} {3,S}
2 *3 [O,S2s]          u0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=95,
    label="carbonylbond_intra_Nd",
    group="""
1 *2 [C,O,S2s]  u0 c0 {2,S} {3,S}
2 *3 [O,S2s]    u0 c0 {1,S}
3    [Cs,O,S2s] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=96,
    label="carbonylbond_intra_H",
    group="""
1 *2 [C,O,S2s] u0 c0 {2,S} {3,S}
2 *3 [O,S2s]   u0 c0 {1,S}
3    H         u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=97,
    label="radadd_intra_cs",
    group="""
1 *1 Cs u1
""",
    kinetics=None,
)

entry(
    index=98,
    label="radadd_intra_csNdNd",
    group="""
1 *1 Cs         u1 {2,S} {3,S}
2    [Cs,O,S2s] u0 {1,S}
3    [Cs,O,S2s] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=99,
    label="radadd_intra_csNdDe",
    group="""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cs,O,S2s]       u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=100,
    label="radadd_intra_csNdCd",
    group="""
1 *1 Cs         u1 {2,S} {3,S}
2    [Cs,O,S2s] u0 {1,S}
3    Cd         u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=101,
    label="radadd_intra_csNdCt",
    group="""
1 *1 Cs         u1 {2,S} {3,S}
2    [Cs,O,S2s] u0 {1,S}
3    Ct         u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=102,
    label="radadd_intra_csDeDe",
    group="""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=103,
    label="radadd_intra_csHDe",
    group="""
1 *1 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=104,
    label="radadd_intra_csHCd",
    group="""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=105,
    label="radadd_intra_csHCt",
    group="""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=106,
    label="radadd_intra_csHNd",
    group="""
1 *1 Cs         u1 {2,S} {3,S}
2    H          u0 {1,S}
3    [Cs,O,S2s] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=107,
    label="radadd_intra_cs2H",
    group="""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=108,
    label="radadd_intra_O",
    group="""
1 *1 O u1
""",
    kinetics=None,
)

entry(
    index=109,
    label="radadd_intra_Cb",
    group="""
1 *1 Cb u1
""",
    kinetics=None,
)

entry(
    index=110,
    label="radadd_intra_cdsingle",
    group="""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=111,
    label="radadd_intra_cdsingleH",
    group="""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=112,
    label="radadd_intra_cdsingleNd",
    group="""
1 *1 Cd         u1 {2,S}
2    [Cs,O,S2s] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=113,
    label="radadd_intra_cdsingleDe",
    group="""
1 *1 Cd               u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=114,
    label="radadd_intra_cddouble",
    group="""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics=None,
)

entry(
    index=115,
    label="radadd_intra_CO",
    group="""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics=None,
)

entry(
    index=116,
    label="radadd_intra_Ct",
    group="""
1 *1 Ct u1
""",
    kinetics=None,
)

tree(
    """
L1: R1_rad_R2_R3
    L2: R4
        L3: R4_S
        L3: R4_D
        L3: R4_T
        L3: R4_B
    L2: R5
        L3: R5_SS
        L3: R5_SD
        L3: R5_DS
        L3: R5_ST
        L3: R5_TS
        L3: R5_SB
        L3: R5_BS
    L2: R6
        L3: R6_RSR
            L4: R6_SSR
                L5: R6_SSS
                L5: R6_SSM
            L4: R6_DSR
                L5: R6_DSS
                L5: R6_DSM
            L4: R6_TSR
                L5: R6_TSS
                L5: R6_TSM
            L4: R6_BSR
                L5: R6_BSS
                L5: R6_BSM
        L3: R6_SMS
        L3: R6_SBB
        L3: R6_BBS
    L2: R7
        L3: R7_RSSR
            L4: R7_SSSR
                L5: R7_SSSS
                L5: R7_SSSM
            L4: R7_DSSR
                L5: R7_DSSS
                L5: R7_DSSM
            L4: R7_TSSR
                L5: R7_TSSS
                L5: R7_TSSM
            L4: R7_BSSR
                L5: R7_BSSS
                L5: R7_BSSM
        L3: R7_RSMS
            L4: R7_SSMS
            L4: R7_DSMS
            L4: R7_TSMS
            L4: R7_BSMS
        L3: R7_SMSR
            L4: R7_SMSS
            L4: R7_SMSM
        L3: R7_BBSR
            L4: R7_BBSS
            L4: R7_BBSM
        L3: R7_RSBB
            L4: R7_SSBB
            L4: R7_DSBB
            L4: R7_TSBB
            L4: R7_BSBB
        L3: R7_SBBS
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_NdNd
            L4: doublebond_intra_NdNd_secDe
            L4: doublebond_intra_NdNd_secNd
            L4: doublebond_intra_NdNd_pri
        L3: doublebond_intra_NdDe
            L4: doublebond_intra_NdDe_secDe
            L4: doublebond_intra_NdDe_secNd
            L4: doublebond_intra_NdDe_pri
                L5: doublebond_intra_NdCd_pri
                L5: doublebond_intra_NdCt_pri
        L3: doublebond_intra_DeDe
            L4: doublebond_intra_DeDe_secDe
            L4: doublebond_intra_DeDe_secNd
            L4: doublebond_intra_DeDe_pri
        L3: doublebond_intra_HDe
            L4: doublebond_intra_HDe_secDe
            L4: doublebond_intra_HDe_secNd
            L4: doublebond_intra_HDe_pri
                L5: doublebond_intra_HCd_pri
                L5: doublebond_intra_HCt_pri
        L3: doublebond_intra_HNd
            L4: doublebond_intra_HNd_secDe
            L4: doublebond_intra_HNd_secNd
            L4: doublebond_intra_HNd_pri
        L3: doublebond_intra_2H
            L4: doublebond_intra_2H_secDe
            L4: doublebond_intra_2H_secNd
            L4: doublebond_intra_2H_pri
    L2: carbonylbond_intra
        L3: carbonylbond_intra_De
        L3: carbonylbond_intra_Nd
        L3: carbonylbond_intra_H
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
            L4: radadd_intra_csHCt
        L3: radadd_intra_csHNd
        L3: radadd_intra_cs2H
    L2: radadd_intra_O
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label="bond21",
    group="""
1 *2 R!H u0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc="""""",
    longDesc="""

""",
)
