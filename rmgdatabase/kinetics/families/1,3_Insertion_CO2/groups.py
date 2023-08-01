#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["Root"], products=["R_(CO2)_R'"], ownReverse=False)

reverse = "1,2_Elimination_CO2"
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
1 *1 Cdd            u0 {2,D} {3,D}
2 *2 O2d            u0 {1,D}
3    O2d            u0 {1,D}
4 *3 [H,Cs,Cd,Cb,N] u0 c0 {5,S}
5 *4 [H,Cs,Cd,Cb,N] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="Root_5CbCdCsHN->Cs",
    group="""
1 *1 Cdd            u0 {2,D} {3,D}
2 *2 O2d            u0 {1,D}
3    O2d            u0 {1,D}
4 *3 [H,Cs,Cd,Cb,N] u0 c0 {5,S}
5 *4 Cs             u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=2,
    label="Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs",
    group="""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 Cs  u0 c0 {5,S}
5 *4 Cs  u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=3,
    label="Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs",
    group="""
1 *1 Cdd   u0 {2,D} {3,D}
2 *2 O2d   u0 {1,D}
3    O2d   u0 {1,D}
4 *3 [H,N] u0 c0 {5,S}
5 *4 Cs    u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=4,
    label="Root_N-5CbCdCsHN->Cs",
    group="""
1 *1 Cdd            u0 {2,D} {3,D}
2 *2 O2d            u0 {1,D}
3    O2d            u0 {1,D}
4 *3 [H,Cs,Cd,Cb,N] u0 c0 {5,S}
5 *4 [Cd,Cb,H,N]    u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=5,
    label="Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H",
    group="""
1 *1 Cdd         u0 {2,D} {3,D}
2 *2 O2d         u0 {1,D}
3    O2d         u0 {1,D}
4 *3 H           u0 c0 {5,S}
5 *4 [Cd,Cb,H,N] u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=6,
    label="Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd",
    group="""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 H   u0 c0 {5,S}
5 *4 Cd  u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=7,
    label="Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R",
    group="""
1 *1 Cdd u0 r0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 H   u0 c0 r0 {5,S}
5 *4 Cd  u0 c0 r0 {4,S} {6,D}
6    N   u0 r0 {5,D} {7,[S,D,T,B,Q]}
7    R!H ux {6,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=8,
    label="Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd",
    group="""
1 *1 Cdd u0 r0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 H   u0 c0 r0 {5,S}
5 *4 H   u0 c0 r0 {4,S}
""",
    kinetics=None,
)

entry(
    index=9,
    label="Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H",
    group="""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 Cs  u0 c0 {5,S}
5 *4 H   u0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index=10,
    label="Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R",
    group="""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 Cs  u0 c0 {5,S} {6,[S,D,T,B,Q]}
5 *4 H   u0 c0 {4,S}
6    R!H ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=11,
    label="Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R",
    group="""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
4 *3 Cs  u0 c0 {5,S} {6,[S,D,T,B,Q]} {7,[S,D,T,B,Q]}
5 *4 H   u0 c0 {4,S}
6    R!H ux {4,[S,D,T,B,Q]}
7    R!H ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

tree(
    """
L1: Root
    L2: Root_5CbCdCsHN->Cs
        L3: Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs
        L3: Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs
    L2: Root_N-5CbCdCsHN->Cs
        L3: Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H
            L4: Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd
                L5: Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R
            L4: Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd
        L3: Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H
            L4: Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R
                L5: Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R
"""
)
