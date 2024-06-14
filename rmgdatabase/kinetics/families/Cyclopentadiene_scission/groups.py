#!/usr/bin/env python
# encoding: utf-8

name = "Cyclopentadiene_scission/groups"
shortDesc = "Scission of one of the adjacent single bonds in a CPD subunit to form a conjugated singlet carbene"
longDesc = """
Currently, family will only scission a fused CPD + cyclopropane bicyclic subunit using calculated kinetics from 2003
Miller and Klippenstein Propargyl recombination PES. Data needed before other entries can be added (e.g., simple CPD
scission)
"""

template(reactants=["Root"], products=["conjugated_singlet_carbene"], ownReverse=False)

reverse = "Intra_singlet_carbene_addition"
reversible = True

reactantNum = 1
productNum = 1
autoGenerated = True

recipe(
    actions=[
        ["BREAK_BOND", "*1", 1, "*2"],
        ["CHANGE_BOND", "*2", -1, "*3"],
        ["CHANGE_BOND", "*4", -1, "*5"],
        ["CHANGE_BOND", "*1", 1, "*5"],
        ["CHANGE_BOND", "*4", 1, "*3"],
        ["GAIN_PAIR", "*2", "1"],
    ]
)

boundaryAtoms = ["*1", "*2"]

entry(
    index=0,
    label="Root",
    group="""
1 *1 C  u0 {2,S} {5,S}
2 *2 Cd u0 {1,S} {3,D}
3 *3 Cd u0 {2,D} {4,S}
4 *4 Cd u0 {3,S} {5,D}
5 *5 Cd u0 {1,S} {4,D}
""",
    kinetics=None,
)

tree(
    """
L1: Root
"""
)