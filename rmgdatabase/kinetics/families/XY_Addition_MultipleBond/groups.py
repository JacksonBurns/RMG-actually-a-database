#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["Root"], products=["X_MultipleBond_Y"], ownReverse=False)

reverse = "XY_Elimination_MultipleBond"
reversible = True

reactantNum = 2

productNum = 1

autoGenerated = True

recipe(
    actions=[
        ["BREAK_BOND", "*3", 1, "*4"],
        ["CHANGE_BOND", "*1", -1, "*2"],
        ["FORM_BOND", "*1", 1, "*3"],
        ["FORM_BOND", "*2", 1, "*4"],
    ]
)

entry(
    index=0,
    label="Root",
    group="""
1 *3 [H,F1s,Cl1s,Br1s]  u0 {2,S}
2 *4 [F1s,Cl1s,Br1s]    u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=1,
    label="Root_1Br1sCl1sF1sH->Cl1s",
    group="""
1 *3 Cl1s               u0 {2,S}
2 *4 [F1s,Cl1s,Br1s]    u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=2,
    label="Root_N-1Br1sCl1sF1sH->Cl1s",
    group="""
1 *3 H                  u0 {2,S}
2 *4 [F1s,Cl1s,Br1s]    u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=3,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=4,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]} {5,[S,D,T,B,Q]}
5    R!H                ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=5,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    group="""
1 *3 H                  u0 r0 {2,S}
2 *4 F1s                u0 r0 {1,S}
3 *1 Ct                 u0 r0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 r0 {3,[D,T]} {5,S}
5    R!H                u0 r0 {4,S}
""",
    kinetics=None,
)

entry(
    index=6,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 [O2d,Cd]           u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]} {5,[S,D,T,B,Q]}
5    R!H                ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=7,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 [O2d,Cd]           u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H                ux {4,[S,D,T,B,Q]}
6    R!H                ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=8,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R",
    group="""
1 *3 H   u0 {2,S}
2 *4 F1s u0 {1,S}
3 *1 Cd  u0 {4,D} {7,[S,D,T,B,Q]}
4 *2 Cd  u0 {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H ux {4,[S,D,T,B,Q]}
6    R!H ux {4,[S,D,T,B,Q]}
7    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=9,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R",
    group="""
1 *3 H   u0 {2,S}
2 *4 F1s u0 {1,S}
3 *1 Cd  u0 {4,D} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
4 *2 Cd  u0 {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H ux {4,[S,D,T,B,Q]}
6    R!H ux {4,[S,D,T,B,Q]}
7    R!H ux {3,[S,D,T,B,Q]}
8    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=10,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 O2d                u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H                ux {4,[S,D,T,B,Q]}
6    R!H                ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=11,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 Cd                 u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H                ux {4,[S,D,T,B,Q]}
6    R!H                ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=12,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R",
    group="""
1 *3 H   u0 {2,S}
2 *4 F1s u0 {1,S}
3 *1 Cd  u0 {4,D} {6,[S,D,T,B,Q]}
4 *2 Cd  u0 {3,D} {5,S}
5    F   u0 {4,S}
6    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=13,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R",
    group="""
1 *3 H   u0 r0 {2,S}
2 *4 F1s u0 r0 {1,S}
3 *1 Cd  u0 r0 {4,D} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
4 *2 Cd  u0 r0 {3,D} {5,S}
5    F   u0 r0 {4,S}
6    R!H ux {3,[S,D,T,B,Q]}
7    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=14,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    group="""
1 *3 H                  u0 {2,S}
2 *4 F1s                u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
5    R!H                ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=15,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    group="""
1 *3 H                  u0 r0 {2,S}
2 *4 F1s                u0 r0 {1,S}
3 *1 Ct                 u0 r0 {4,[D,T]} {5,S}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 r0 {3,[D,T]}
5    R!H                u0 r0 {3,S}
""",
    kinetics=None,
)

entry(
    index=16,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    group="""
1 *3 H   u0 {2,S}
2 *4 F1s u0 {1,S}
3 *1 Cd  u0 {4,D} {5,[S,D,T,B,Q]}
4 *2 Cd  u0 {3,D}
5    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=17,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R",
    group="""
1 *3 H   u0 {2,S}
2 *4 F1s u0 {1,S}
3 *1 Cd  u0 {4,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4 *2 Cd  u0 {3,D}
5    R!H ux {3,[S,D,T,B,Q]}
6    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=18,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s",
    group="""
1 *3 H                  u0 {2,S}
2 *4 [Cl1s,Br1s]        u0 {1,S}
3 *1 [Cd,Cdd,Ct,CO,O2d] u0 {4,[D,T]}
4 *2 [Cd,Cdd,Ct,CO,O2d] u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=19,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    group="""
1 *3 H           u0 {2,S}
2 *4 [Cl1s,Br1s] u0 {1,S}
3 *1 Ct          u0 {4,[D,T]}
4 *2 Ct          u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=20,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Ct   u0 {4,[D,T]}
4 *2 Ct   u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=21,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Ct   u0 {4,T}
4 *2 Ct   u0 {3,T} {5,S}
5    Cl   u0 {4,S}
""",
    kinetics=None,
)

entry(
    index=22,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R",
    group="""
1 *3 H    u0 r0 {2,S}
2 *4 Cl1s u0 r0 {1,S}
3 *1 Ct   u0 r0 {4,T} {6,[S,D,T,B,Q]}
4 *2 Ct   u0 r0 {3,T} {5,S}
5    Cl   u0 r0 {4,S}
6    R!H  ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=23,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Ct   u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 Ct   u0 {3,[D,T]}
5    R!H  ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=24,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    group="""
1 *3 H    u0 r0 {2,S}
2 *4 Br1s u0 r0 {1,S}
3 *1 Ct   u0 r0 {4,T}
4 *2 Ct   u0 r0 {3,T}
""",
    kinetics=None,
)

entry(
    index=25,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    group="""
1 *3 H           u0 {2,S}
2 *4 [Cl1s,Br1s] u0 {1,S}
3 *1 Cd          u0 {4,[D,T]}
4 *2 Cd          u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=26,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]}
4 *2 Cd   u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=27,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]}
5    R!H  ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=28,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]}
5    Cl   ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=29,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]}
5    Cl   ux {3,[S,D,T,B,Q]}
6    Cl   ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=30,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]} {7,[S,D,T,B,Q]}
5    Cl   ux {3,[S,D,T,B,Q]}
6    Cl   ux {3,[S,D,T,B,Q]}
7    R!H  ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=31,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]} {7,[S,D,T,B,Q]} {8,[S,D,T,B,Q]}
5    Cl   ux {3,[S,D,T,B,Q]}
6    Cl   ux {3,[S,D,T,B,Q]}
7    R!H  ux {4,[S,D,T,B,Q]}
8    R!H  ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=32,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]} {6,[S,D,T,B,Q]}
5    Cl   ux {3,[S,D,T,B,Q]}
6    R!H  ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=33,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl",
    group="""
1 *3 H                     u0 r0 {2,S}
2 *4 Cl1s                  u0 r0 {1,S}
3 *1 Cd                    u0 r0 {4,D} {5,S}
4 *2 Cd                    u0 r0 {3,D}
5    [N,P,F,I,Br,O,C,Si,S] u0 r0 {3,S}
""",
    kinetics=None,
)

entry(
    index=34,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]}
4 *2 Cd   u0 {3,[D,T]} {5,[S,D,T,B,Q]}
5    R!H  ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=35,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    group="""
1 *3 H    u0 r0 {2,S}
2 *4 Cl1s u0 r0 {1,S}
3 *1 Cd   u0 r0 {4,D}
4 *2 Cd   u0 r0 {3,D} {5,[S,D,T,B,Q]} {6,[S,D,T,B,Q]}
5    R!H  ux {4,[S,D,T,B,Q]}
6    R!H  ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=36,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]}
4 *2 Cd   u0 {3,[D,T]} {5,[S,D,T,B,Q]}
5    C    ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=37,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    group="""
1 *3 H    u0 {2,S}
2 *4 Cl1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]}
4 *2 Cd   u0 {3,[D,T]} {5,[S,D,T,B,Q]}
5    Cl   ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=38,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    group="""
1 *3 H    u0 {2,S}
2 *4 Br1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]}
4 *2 Cd   u0 {3,[D,T]}
""",
    kinetics=None,
)

entry(
    index=39,
    label="Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    group="""
1 *3 H    u0 {2,S}
2 *4 Br1s u0 {1,S}
3 *1 Cd   u0 {4,[D,T]} {5,[S,D,T,B,Q]}
4 *2 Cd   u0 {3,[D,T]}
5    R!H  ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

tree(
    """
L1: Root
    L2: Root_1Br1sCl1sF1sH->Cl1s
    L2: Root_N-1Br1sCl1sF1sH->Cl1s
        L3: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
            L4: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
                            L8: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
            L4: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
        L3: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
            L4: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
            L4: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
                            L8: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
                                L9: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
                                    L10: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
                            L8: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
                        L7: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
                L5: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
                    L6: Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
"""
)
