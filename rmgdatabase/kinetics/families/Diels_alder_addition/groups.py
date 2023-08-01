#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["Root"], products=["Six_Ring"], ownReverse=False)

reverse = "Retro_Diels_Alder_Addition"
reversible = True

reactantNum = 2

productNum = 1

autoGenerated = True

recipe(
    actions=[
        ["CHANGE_BOND", "*1", -1, "*2"],
        ["CHANGE_BOND", "*3", -1, "*4"],
        ["CHANGE_BOND", "*4", 1, "*5"],
        ["CHANGE_BOND", "*5", -1, "*6"],
        ["FORM_BOND", "*1", 1, "*3"],
        ["FORM_BOND", "*2", 1, "*6"],
    ]
)

entry(
    index=0,
    label="Root",
    group="""
1 *4 [Cd,S4d,S6d,N3d,N5dc]                                                 u0 {2,S} {3,D}
2 *5 [Cd,S4d,S6d,N3d,N5dc]                                                 u0 {1,S} {4,D}
3 *3 Cd                                                                    u0 {1,D}
4 *6 Cd                                                                    u0 {2,D}
5 *1 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {6,[D,T]}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {5,[D,T]}
""",
    kinetics=None,
)

entry(
    index=1,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    group="""
1 *4 Cd u0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,[D,T]}
6 *2 Cd u0 {5,[D,T]}
""",
    kinetics=None,
)

entry(
    index=2,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing",
    group="""
1 *4 Cd u0 r1 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,D}
6 *2 Cd u0 {5,D}
""",
    kinetics=None,
)

entry(
    index=3,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,[D,T]}
6 *2 Cd u0 {5,[D,T]}
""",
    kinetics=None,
)

entry(
    index=4,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 {1,S} {4,D}
3 *3 Cd  u0 {1,D} {7,[S,D,T,B,Q]}
4 *6 Cd  u0 {2,D}
5 *1 Cd  u0 {6,[D,T]}
6 *2 Cd  u0 {5,[D,T]}
7    R!H ux {3,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=5,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D} {7,[S,D,T,B,Q]}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,[D,T]} {8,[S,D,T,B,Q]}
6 *2 Cd u0 {5,[D,T]}
7    C  ux {3,[S,D,T,B,Q]}
8    C  ux {5,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=6,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D} {7,S}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,D} {8,[S,D,T,B,Q]}
6 *2 Cd u0 {5,D} {9,S}
7    C  u0 {3,S}
8    C  ux {5,[S,D,T,B,Q]}
9    C  u0 {6,S}
""",
    kinetics=None,
)

entry(
    index=7,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    group="""
1  *4 Cd  u0 r0 {2,S} {3,D}
2  *5 Cd  u0 {1,S} {4,D}
3  *3 Cd  u0 {1,D} {7,S}
4  *6 Cd  u0 {2,D}
5  *1 Cd  u0 {6,D} {8,[S,D,T,B,Q]}
6  *2 Cd  u0 {5,D} {9,S}
7     C   u0 r0 {3,S}
8     C   ux {5,[S,D,T,B,Q]} {10,[S,D,T,B,Q]}
9     C   u0 r0 {6,S}
10    R!H ux {8,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=8,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 {1,S} {4,D}
3 *3 Cd  u0 {1,D} {7,[S,D,T,B,Q]}
4 *6 Cd  u0 {2,D}
5 *1 Cd  u0 {6,[D,T]} {8,[S,D,T,B,Q]}
6 *2 Cd  u0 {5,[D,T]}
7    C   ux {3,[S,D,T,B,Q]}
8    C   ux {5,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=9,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D} {7,S}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,D}
6 *2 Cd u0 {5,D} {8,S}
7    C  u0 {3,S}
8    C  u0 {6,S}
""",
    kinetics=None,
)

entry(
    index=10,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 r0 {1,S} {4,D}
3 *3 Cd  u0 r0 {1,D} {7,S}
4 *6 Cd  u0 r0 {2,D}
5 *1 Cd  u0 r0 {6,D}
6 *2 Cd  u0 r0 {5,D} {8,S}
7    C   u0 r0 {3,S}
8    C   u0 r0 {6,S} {9,[S,D,T,B,Q]}
9    R!H ux {8,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=11,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 {1,S} {4,D}
3 *3 Cd  u0 {1,D} {7,[S,D,T,B,Q]}
4 *6 Cd  u0 {2,D} {8,[S,D,T,B,Q]}
5 *1 Cd  u0 {6,[D,T]}
6 *2 Cd  u0 {5,[D,T]}
7    R!H ux {3,[S,D,T,B,Q]}
8    R!H ux {4,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=12,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D} {7,S}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,D}
6 *2 Cd u0 {5,D}
7    C  u0 {1,S}
""",
    kinetics=None,
)

entry(
    index=13,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D} {7,S}
2 *5 Cd  u0 r0 {1,S} {4,D}
3 *3 Cd  u0 r0 {1,D}
4 *6 Cd  u0 r0 {2,D}
5 *1 Cd  u0 r0 {6,D}
6 *2 Cd  u0 r0 {5,D} {8,[S,D,T,B,Q]}
7    C   u0 r0 {1,S}
8    R!H ux {6,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=14,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D} {7,S}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,D}
6 *2 Cd u0 {5,D}
7    C  u0 {2,S}
""",
    kinetics=None,
)

entry(
    index=15,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 r0 {1,S} {4,D} {7,S}
3 *3 Cd  u0 r0 {1,D}
4 *6 Cd  u0 r0 {2,D}
5 *1 Cd  u0 r0 {6,D} {8,[S,D,T,B,Q]}
6 *2 Cd  u0 r0 {5,D}
7    C   u0 r0 {2,S}
8    R!H ux {5,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=16,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,[D,T]} {7,[S,D,T,B,Q]}
6 *2 Cd u0 {5,[D,T]}
7    C  ux {5,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=17,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    group="""
1 *4 Cd u0 r0 {2,S} {3,D}
2 *5 Cd u0 {1,S} {4,D}
3 *3 Cd u0 {1,D}
4 *6 Cd u0 {2,D}
5 *1 Cd u0 {6,[D,T]} {7,[S,D,T,B,Q]}
6 *2 Cd u0 {5,[D,T]} {8,S}
7    C  ux {5,[S,D,T,B,Q]}
8    C  u0 {6,S}
""",
    kinetics=None,
)

entry(
    index=18,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 {1,S} {4,D}
3 *3 Cd  u0 {1,D}
4 *6 Cd  u0 {2,D}
5 *1 Cd  u0 {6,[D,T]} {7,[S,D,T,B,Q]}
6 *2 Cd  u0 {5,[D,T]} {8,S}
7    C   ux {5,[S,D,T,B,Q]} {9,[S,D,T,B,Q]}
8    C   u0 r0 {6,S}
9    R!H ux {7,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=19,
    label="Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    group="""
1 *4 Cd  u0 r0 {2,S} {3,D}
2 *5 Cd  u0 {1,S} {4,D}
3 *3 Cd  u0 {1,D}
4 *6 Cd  u0 {2,D}
5 *1 Cd  u0 {6,[D,T]}
6 *2 Cd  u0 {5,[D,T]} {7,[S,D,T,B,Q]}
7    R!H ux {6,[S,D,T,B,Q]}
""",
    kinetics=None,
)

entry(
    index=20,
    label="Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    group="""
1 *4 Cd                                                                    u0 {2,S} {3,D}
2 *5 Cd                                                                    u0 {1,S} {4,D}
3 *3 Cd                                                                    u0 {1,D}
4 *6 Cd                                                                    u0 {2,D}
5 *1 [CS,S6t,N5dc,S6d,Cdd,S2d,N3d,S4t,S6td,S4d,N3t,S6tt,Ct,O2d,N5tc,CO]    u0 {6,[D,T]}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {5,[D,T]}
""",
    kinetics=None,
)

entry(
    index=21,
    label="Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    group="""
1 *4 Cd                                                                    u0 r0 {2,S} {3,D}
2 *5 Cd                                                                    u0 r0 {1,S} {4,D}
3 *3 Cd                                                                    u0 r0 {1,D}
4 *6 Cd                                                                    u0 r0 {2,D}
5 *1 Ct                                                                    u0 {6,[D,T]}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {5,[D,T]}
""",
    kinetics=None,
)

entry(
    index=22,
    label="Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    group="""
1 *4 Cd                                                                    u0 {2,S} {3,D}
2 *5 Cd                                                                    u0 {1,S} {4,D}
3 *3 Cd                                                                    u0 {1,D}
4 *6 Cd                                                                    u0 {2,D}
5 *1 [Cdd,CO]                                                              u0 {6,D}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {5,D}
""",
    kinetics=None,
)

entry(
    index=23,
    label="Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd",
    group="""
1 *4 Cd                                                                    u0 {2,S} {3,D}
2 *5 Cd                                                                    u0 {1,S} {4,D}
3 *3 Cd                                                                    u0 {1,D}
4 *6 Cd                                                                    u0 {2,D}
5 *1 Cdd                                                                   u0 r0 {6,D}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 r0 {5,D}
""",
    kinetics=None,
)

entry(
    index=24,
    label="Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd",
    group="""
1 *4 Cd                                                                    u0 {2,S} {3,D}
2 *5 Cd                                                                    u0 {1,S} {4,D}
3 *3 Cd                                                                    u0 {1,D}
4 *6 Cd                                                                    u0 {2,D}
5 *1 CO                                                                    u0 r0 {6,D}
6 *2 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc,Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 r0 {5,D}
""",
    kinetics=None,
)

tree(
    """
L1: Root
    L2: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
        L3: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
        L3: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
            L4: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
                    L6: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
                        L7: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
                    L6: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
                    L6: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
            L4: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
            L4: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
            L4: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
                L5: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
                    L6: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
            L4: Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    L2: Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
        L3: Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
        L3: Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
            L4: Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
            L4: Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
"""
)

forbidden(
    label="benzene_diene1",
    group="""
1 *3 Cd u0 {2,D} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_diene2",
    group="""
1 *3 Cd u0 {2,D} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S}
5 *8 Cd ux {4,S} {6,D}
6 *7 Cd ux {1,S} {5,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_diene_partial1",
    group="""
1 *3 Cd u0 {2,D} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_diene_partial2",
    group="""
1 *5 Cd u0 {2,D} {6,S}
2 *6 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_ene",
    group="""
1 *1 Cd u0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_monoSub1",
    group="""
1 *3 Cd u0 {2,D} {6,S} {7,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S} {8,S}
5 *7 Cd ux {4,S} {6,D}
6 *8 Cd ux {1,S} {5,D}
7    H  u0 {1,S}
8 *9 R  ux {4,S}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_monoSub2",
    group="""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {7,S} {8,S}
5    H  u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R  ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_twoSub1",
    group="""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {7,S} {8,S}
5    H  u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R  ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzene_twoSub2",
    group="""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {7,S} {8,S}
5    H  u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R  ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzyl_isomer1",
    group="""
1 C u0 {2,D}
2 C u0 {1,D} {3,S} {7,S}
3 C u0 {2,S} {4,D}
4 C u0 {3,D} {5,S}
5 C u1 {4,S} {6,S}
6 C u0 {5,S} {7,D}
7 C u0 {2,S} {6,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="benzyl_isomer2",
    group="""
1 C u0 {2,D}
2 C u0 {1,D} {3,S} {7,S}
3 C u1 {2,S} {4,S}
4 C u0 {3,S} {5,D}
5 C u0 {4,D} {6,S}
6 C u0 {5,S} {7,D}
7 C u0 {2,S} {6,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="threeMemberedRing_2342",
    group="""
1 *3 Cd u0 {2,D}
2 *4 Cd u0 {1,D} {3,S} {4,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {2,S} {3,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)

forbidden(
    label="threeMemberedRing_3213",
    group="""
1 *3 Cd u0 {2,D} {3,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {1,S} {2,S} {4,D}
4 *6 Cd u0 {3,D}
""",
    shortDesc="""""",
    longDesc="""

""",
)
