#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech 3.0"
shortDesc = "An optimized detailed reaction mechanism for natural gas combustion in flames and ignition."
longDesc = """
The thermodynamic and kinetic parameters in the GRI-Mech 3.0 mechanism have 
been collectively estimated from literature search and then optimized to a set 
of representative experimental targets. For this reason you should generally
use GRI-Mech in its entirety, and generally should not tweak any of its
parameter values.

GRI-Mech is the result of collaborative research of the Gas Research Institute
and carried out at The University of California at Berkeley, Stanford 
University, The University of Texas at Austin, and SRI International.
"""
entry(
    index=0,
    label="O",
    molecule="""
multiplicity 3
1 O u2 p2 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.16827,
                    -0.00327932,
                    6.64306e-06,
                    -6.12807e-09,
                    2.11266e-12,
                    29122.3,
                    2.05193,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.56942,
                    -8.59741e-05,
                    4.19485e-08,
                    -1.00178e-11,
                    1.22834e-15,
                    29217.6,
                    4.78434,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=1,
    label="O2",
    molecule="""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.78246,
                    -0.00299673,
                    9.8473e-06,
                    -9.6813e-09,
                    3.24373e-12,
                    -1063.94,
                    3.65768,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.28254,
                    0.00148309,
                    -7.57967e-07,
                    2.09471e-10,
                    -2.16718e-14,
                    -1088.46,
                    5.45323,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=2,
    label="H",
    molecule="""
multiplicity 2
1 H u1 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.5,
                    7.05333e-13,
                    -1.99592e-15,
                    2.30082e-18,
                    -9.27732e-22,
                    25473.7,
                    -0.446683,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.5,
                    -2.30843e-11,
                    1.61562e-14,
                    -4.73515e-18,
                    4.98197e-22,
                    25473.7,
                    -0.446683,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=3,
    label="H2",
    molecule="""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.34433,
                    0.00798052,
                    -1.94782e-05,
                    2.01572e-08,
                    -7.37612e-12,
                    -917.935,
                    0.68301,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.33728,
                    -4.94025e-05,
                    4.99457e-07,
                    -1.79566e-10,
                    2.00255e-14,
                    -950.159,
                    -3.20502,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=4,
    label="OH",
    molecule="""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.99202,
                    -0.00240132,
                    4.61794e-06,
                    -3.88113e-09,
                    1.36411e-12,
                    3615.08,
                    -0.103925,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.09289,
                    0.00054843,
                    1.26505e-07,
                    -8.79462e-11,
                    1.17412e-14,
                    3858.66,
                    4.4767,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=5,
    label="H2O",
    molecule="""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.19864,
                    -0.00203643,
                    6.5204e-06,
                    -5.48797e-09,
                    1.77198e-12,
                    -30293.7,
                    -0.849032,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.03399,
                    0.00217692,
                    -1.64073e-07,
                    -9.7042e-11,
                    1.68201e-14,
                    -30004.3,
                    4.96677,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=6,
    label="HO2",
    molecule="""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.3018,
                    -0.00474912,
                    2.11583e-05,
                    -2.42764e-08,
                    9.29225e-12,
                    294.808,
                    3.71666,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.01721,
                    0.00223982,
                    -6.33658e-07,
                    1.14246e-10,
                    -1.07909e-14,
                    111.857,
                    3.7851,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=7,
    label="H2O2",
    molecule="""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.27611,
                    -0.000542822,
                    1.67336e-05,
                    -2.15771e-08,
                    8.62454e-12,
                    -17702.6,
                    3.43505,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.165,
                    0.00490832,
                    -1.90139e-06,
                    3.71186e-10,
                    -2.87908e-14,
                    -17861.8,
                    2.91616,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=8,
    label="C(T)",
    molecule="""
multiplicity 3
1 C u2 p1 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.55424,
                    -0.000321538,
                    7.33792e-07,
                    -7.32235e-10,
                    2.66521e-13,
                    85443.9,
                    4.53131,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.49267,
                    4.79889e-05,
                    -7.24335e-08,
                    3.74291e-11,
                    -4.87278e-15,
                    85451.3,
                    4.8015,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=9,
    label="CH",
    molecule="""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.48982,
                    0.000323836,
                    -1.68899e-06,
                    3.16217e-09,
                    -1.40609e-12,
                    70797.3,
                    2.08401,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.87846,
                    0.000970914,
                    1.44446e-07,
                    -1.30688e-10,
                    1.76079e-14,
                    71012.4,
                    5.48498,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=10,
    label="CH2",
    molecule="""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.76268,
                    0.000968872,
                    2.7949e-06,
                    -3.85091e-09,
                    1.68742e-12,
                    46004,
                    1.56253,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.8741,
                    0.00365639,
                    -1.40895e-06,
                    2.6018e-10,
                    -1.87728e-14,
                    46263.6,
                    6.17119,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=11,
    label="CH2(S)",
    molecule="""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.1986,
                    -0.00236661,
                    8.23296e-06,
                    -6.68816e-09,
                    1.94315e-12,
                    50496.8,
                    -0.769119,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.29204,
                    0.00465589,
                    -2.01192e-06,
                    4.17906e-10,
                    -3.39716e-14,
                    50926,
                    8.6265,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=12,
    label="CH3",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.67359,
                    0.00201095,
                    5.73022e-06,
                    -6.87117e-09,
                    2.54386e-12,
                    16445,
                    1.60456,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.28572,
                    0.0072399,
                    -2.98714e-06,
                    5.95685e-10,
                    -4.67154e-14,
                    16775.6,
                    8.48007,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=13,
    label="CH4",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.14988,
                    -0.013671,
                    4.91801e-05,
                    -4.84743e-08,
                    1.66694e-11,
                    -10246.6,
                    -4.6413,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    0.0748515,
                    0.0133909,
                    -5.73286e-06,
                    1.22293e-09,
                    -1.01815e-13,
                    -9468.34,
                    18.4373,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=14,
    label="CO",
    molecule="""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.57953,
                    -0.000610354,
                    1.01681e-06,
                    9.07006e-10,
                    -9.04424e-13,
                    -14344.1,
                    3.50841,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.71519,
                    0.00206253,
                    -9.98826e-07,
                    2.30053e-10,
                    -2.03648e-14,
                    -14151.9,
                    7.81869,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=15,
    label="CO2",
    molecule="""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.35677,
                    0.0089846,
                    -7.12356e-06,
                    2.45919e-09,
                    -1.437e-13,
                    -48372,
                    9.90105,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.85746,
                    0.00441437,
                    -2.21481e-06,
                    5.2349e-10,
                    -4.72084e-14,
                    -48759.2,
                    2.27164,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=16,
    label="HCO",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.22119,
                    -0.00324393,
                    1.37799e-05,
                    -1.33144e-08,
                    4.33769e-12,
                    3839.56,
                    3.39437,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.77217,
                    0.00495696,
                    -2.48446e-06,
                    5.89162e-10,
                    -5.33509e-14,
                    4011.92,
                    9.79834,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=17,
    label="CH2O",
    molecule="""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.79372,
                    -0.00990833,
                    3.7322e-05,
                    -3.79285e-08,
                    1.31773e-11,
                    -14309,
                    0.602813,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.76069,
                    0.0092,
                    -4.42259e-06,
                    1.00641e-09,
                    -8.83856e-14,
                    -13995.8,
                    13.6563,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=18,
    label="CH2OH",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.86389,
                    0.00559672,
                    5.93272e-06,
                    -1.04532e-08,
                    4.36967e-12,
                    -3193.91,
                    5.47302,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.69267,
                    0.00864577,
                    -3.75101e-06,
                    7.87235e-10,
                    -6.48554e-14,
                    -3242.51,
                    5.81043,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=19,
    label="CH3O",
    molecule="""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.1062,
                    0.0072166,
                    5.33847e-06,
                    -7.37764e-09,
                    2.07561e-12,
                    978.601,
                    13.1522,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.7708,
                    0.0078715,
                    -2.65638e-06,
                    3.94443e-10,
                    -2.11262e-14,
                    127.833,
                    2.92957,
                ],
                Tmin=(1000, "K"),
                Tmax=(3000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(3000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=20,
    label="CH3OH",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.7154,
                    -0.0152309,
                    6.52441e-05,
                    -7.10807e-08,
                    2.61353e-11,
                    -25642.8,
                    -1.5041,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.78971,
                    0.0140938,
                    -6.36501e-06,
                    1.38171e-09,
                    -1.1706e-13,
                    -25374.9,
                    14.5024,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=21,
    label="C2H",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.88966,
                    0.01341,
                    -2.8477e-05,
                    2.94791e-08,
                    -1.09332e-11,
                    66839.4,
                    6.22296,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.16781,
                    0.00475222,
                    -1.83787e-06,
                    3.0419e-10,
                    -1.77233e-14,
                    67121.1,
                    6.63589,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=22,
    label="C2H2",
    molecule="""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    0.808681,
                    0.0233616,
                    -3.55172e-05,
                    2.80152e-08,
                    -8.50073e-12,
                    26429,
                    13.9397,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.14757,
                    0.00596167,
                    -2.37295e-06,
                    4.67412e-10,
                    -3.61235e-14,
                    25936,
                    -1.23028,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=23,
    label="C2H3",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.21247,
                    0.00151479,
                    2.59209e-05,
                    -3.57658e-08,
                    1.47151e-11,
                    34859.8,
                    8.51054,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.01672,
                    0.0103302,
                    -4.68082e-06,
                    1.01763e-09,
                    -8.62607e-14,
                    34612.9,
                    7.78732,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=24,
    label="C2H4",
    molecule="""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.9592,
                    -0.00757052,
                    5.7099e-05,
                    -6.91589e-08,
                    2.69884e-11,
                    5089.78,
                    4.09733,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.03611,
                    0.0146454,
                    -6.71078e-06,
                    1.47223e-09,
                    -1.25706e-13,
                    4939.89,
                    10.3054,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=25,
    label="C2H5",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.30647,
                    -0.00418659,
                    4.97143e-05,
                    -5.99127e-08,
                    2.30509e-11,
                    12841.6,
                    4.70721,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.95466,
                    0.0173973,
                    -7.98207e-06,
                    1.75218e-09,
                    -1.49642e-13,
                    12857.5,
                    13.4624,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=26,
    label="C2H6",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.29142,
                    -0.00550154,
                    5.99438e-05,
                    -7.08466e-08,
                    2.68686e-11,
                    -11522.2,
                    2.66682,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.07188,
                    0.0216853,
                    -1.00256e-05,
                    2.21412e-09,
                    -1.90003e-13,
                    -11426.4,
                    15.1156,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=27,
    label="CH2CO",
    molecule="""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.13584,
                    0.0181189,
                    -1.73947e-05,
                    9.34398e-09,
                    -2.01458e-12,
                    -7042.92,
                    12.2156,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.5113,
                    0.0090036,
                    -4.1694e-06,
                    9.23346e-10,
                    -7.94838e-14,
                    -7551.05,
                    0.632247,
                ],
                Tmin=(1000, "K"),
                Tmax=(3500, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(3500, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=28,
    label="HCCO",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.25172,
                    0.017655,
                    -2.37291e-05,
                    1.72758e-08,
                    -5.06648e-12,
                    20059.4,
                    12.4904,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.62821,
                    0.00408534,
                    -1.59345e-06,
                    2.86261e-10,
                    -1.94078e-14,
                    19327.2,
                    -3.93026,
                ],
                Tmin=(1000, "K"),
                Tmax=(4000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(4000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=29,
    label="HCCOH",
    molecule="""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.24237,
                    0.0310722,
                    -5.08669e-05,
                    4.31371e-08,
                    -1.40146e-11,
                    8031.61,
                    13.8743,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.92383,
                    0.00679236,
                    -2.56586e-06,
                    4.49878e-10,
                    -2.99401e-14,
                    7264.63,
                    -7.60177,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=30,
    label="H2CN",
    molecule="""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.85166,
                    0.00569523,
                    1.07114e-06,
                    -1.62261e-09,
                    -2.35111e-13,
                    28637.8,
                    8.99275,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.2097,
                    0.00296929,
                    -2.85559e-07,
                    -1.63555e-10,
                    3.04326e-14,
                    27677.1,
                    -4.44448,
                ],
                Tmin=(1000, "K"),
                Tmax=(4000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(4000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=31,
    label="HCN",
    molecule="""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.25899,
                    0.0100512,
                    -1.33518e-05,
                    1.00923e-08,
                    -3.0089e-12,
                    14712.6,
                    8.91644,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.80224,
                    0.00314642,
                    -1.06322e-06,
                    1.66198e-10,
                    -9.79976e-15,
                    14407.3,
                    1.57546,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=32,
    label="HNO",
    molecule="""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.53349,
                    -0.00566962,
                    1.84732e-05,
                    -1.71371e-08,
                    5.54546e-12,
                    11548.3,
                    1.74984,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.97925,
                    0.00349441,
                    -7.85498e-07,
                    5.74796e-11,
                    -1.93359e-16,
                    11750.6,
                    8.60637,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=33,
    label="N",
    molecule="""
multiplicity 4
1 N u3 p1 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[2.5, 0, 0, 0, 0, 56104.6, 4.19391],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.41594,
                    0.000174891,
                    -1.19024e-07,
                    3.02262e-11,
                    -2.0361e-15,
                    56133.8,
                    4.64961,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=34,
    label="NNH",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.34469,
                    -0.00484971,
                    2.00595e-05,
                    -2.17265e-08,
                    7.94695e-12,
                    28792,
                    2.97794,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.76675,
                    0.00289151,
                    -1.04166e-06,
                    1.68426e-10,
                    -1.00919e-14,
                    28650.7,
                    4.47051,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=35,
    label="N2O",
    molecule="""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p2 c-1 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.25715,
                    0.0113047,
                    -1.36713e-05,
                    9.68198e-09,
                    -2.93072e-12,
                    8741.77,
                    10.758,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.82307,
                    0.00262703,
                    -9.58509e-07,
                    1.60007e-10,
                    -9.77523e-15,
                    8073.4,
                    -2.20172,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=36,
    label="NH",
    molecule="""
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.49291,
                    0.000311792,
                    -1.48905e-06,
                    2.48164e-09,
                    -1.0357e-12,
                    41880.6,
                    1.84833,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.78369,
                    0.00132984,
                    -4.2478e-07,
                    7.83485e-11,
                    -5.50445e-15,
                    42120.8,
                    5.74078,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=37,
    label="NH2",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.204,
                    -0.00210614,
                    7.10683e-06,
                    -5.61152e-09,
                    1.64407e-12,
                    21885.9,
                    -0.141842,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.83474,
                    0.00320731,
                    -9.33908e-07,
                    1.3703e-10,
                    -7.92061e-15,
                    22172,
                    6.52042,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=38,
    label="NH3",
    molecule="""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.28603,
                    -0.00466052,
                    2.17185e-05,
                    -2.28089e-08,
                    8.2638e-12,
                    -6741.73,
                    -0.625373,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.63445,
                    0.00566626,
                    -1.72787e-06,
                    2.38672e-10,
                    -1.25788e-14,
                    -6544.7,
                    6.56629,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=39,
    label="NO",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.21848,
                    -0.00463898,
                    1.1041e-05,
                    -9.33614e-09,
                    2.80358e-12,
                    9844.62,
                    2.28085,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.26061,
                    0.0011911,
                    -4.2917e-07,
                    6.94577e-11,
                    -4.03361e-15,
                    9920.97,
                    6.3693,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=40,
    label="NO2",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.94403,
                    -0.00158543,
                    1.66578e-05,
                    -2.04754e-08,
                    7.83506e-12,
                    2896.62,
                    6.31199,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.88475,
                    0.0021724,
                    -8.28069e-07,
                    1.57475e-10,
                    -1.05109e-14,
                    2316.5,
                    -0.117417,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=41,
    label="HCNO",
    molecule="""
multiplicity 3
1 C u1 p0 c0 {2,D} {4,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.64728,
                    0.0127505,
                    -1.04794e-05,
                    4.41433e-09,
                    -7.57521e-13,
                    19299,
                    10.7333,
                ],
                Tmin=(298, "K"),
                Tmax=(1382, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.5986,
                    0.00302779,
                    -1.07704e-06,
                    1.71667e-10,
                    -1.01439e-14,
                    17966.1,
                    -10.3307,
                ],
                Tmin=(1382, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=42,
    label="HOCN",
    molecule="""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.78605,
                    0.00688668,
                    -3.21488e-06,
                    5.17196e-10,
                    1.19361e-14,
                    -2826.98,
                    5.63292,
                ],
                Tmin=(298, "K"),
                Tmax=(1368, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.89785,
                    0.00316789,
                    -1.11801e-06,
                    1.77243e-10,
                    -1.04339e-14,
                    -3706.53,
                    -6.18168,
                ],
                Tmin=(1368, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=43,
    label="HNCO",
    molecule="""
1 N u0 p1 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.63096,
                    0.00730282,
                    -2.2805e-06,
                    -6.61271e-10,
                    3.62236e-13,
                    -15587.4,
                    6.19458,
                ],
                Tmin=(298, "K"),
                Tmax=(1478, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.22395,
                    0.00317864,
                    -1.09379e-06,
                    1.70735e-10,
                    -9.95022e-15,
                    -16659.9,
                    -8.38225,
                ],
                Tmin=(1478, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=44,
    label="NCO",
    molecule="""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.82693,
                    0.00880517,
                    -8.38661e-06,
                    4.8017e-09,
                    -1.33136e-12,
                    14682.5,
                    9.55046,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.15218,
                    0.00230518,
                    -8.80332e-07,
                    1.47891e-10,
                    -9.0978e-15,
                    14004.1,
                    -2.54427,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=45,
    label="CN",
    molecule="""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.61294,
                    -0.000955513,
                    2.1443e-06,
                    -3.15163e-10,
                    -4.64304e-13,
                    51708.3,
                    3.9805,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    3.74598,
                    4.34508e-05,
                    2.9706e-07,
                    -6.86518e-11,
                    4.41342e-15,
                    51536.2,
                    2.78676,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=46,
    label="HCNN",
    molecule="""
multiplicity 2
1 C u0 p1 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p1 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.52432,
                    0.0159606,
                    -1.88164e-05,
                    1.21255e-08,
                    -3.23574e-12,
                    54262,
                    11.6759,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.89464,
                    0.0039896,
                    -1.59824e-06,
                    2.92494e-10,
                    -2.00947e-14,
                    53452.9,
                    -5.10305,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=47,
    label="N2",
    molecule="""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.29868,
                    0.00140824,
                    -3.96322e-06,
                    5.64152e-09,
                    -2.44485e-12,
                    -1020.9,
                    3.95037,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.92664,
                    0.00148798,
                    -5.68476e-07,
                    1.0097e-10,
                    -6.75335e-15,
                    -922.798,
                    5.98053,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=48,
    label="Ar",
    molecule="""
1 Ar u0 p4 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[2.5, 0, 0, 0, 0, -745.375, 4.366],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[2.5, 0, 0, 0, 0, -745.375, 4.366],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=49,
    label="C3H8",
    molecule="""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    0.933554,
                    0.0264246,
                    6.10597e-06,
                    -2.19775e-08,
                    9.51493e-12,
                    -13958.5,
                    19.2017,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.53414,
                    0.0188722,
                    -6.27185e-06,
                    9.14756e-10,
                    -4.78381e-14,
                    -16467.5,
                    -17.8923,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=50,
    label="C3H7",
    molecule="""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.05155,
                    0.025992,
                    2.38005e-06,
                    -1.96096e-08,
                    9.37325e-12,
                    10631.9,
                    21.1226,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.7027,
                    0.0160442,
                    -5.28332e-06,
                    7.62986e-10,
                    -3.93923e-14,
                    8298.43,
                    -15.4802,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)

entry(
    index=51,
    label="CH3CHO",
    molecule="""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.72946,
                    -0.00319329,
                    4.75349e-05,
                    -5.74586e-08,
                    2.19311e-11,
                    -21572.9,
                    4.10302,
                ],
                Tmin=(200, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.40411,
                    0.0117231,
                    -4.22631e-06,
                    6.83725e-10,
                    -4.09849e-14,
                    -22593.1,
                    -3.48079,
                ],
                Tmin=(1000, "K"),
                Tmax=(6000, "K"),
            ),
        ],
        Tmin=(200, "K"),
        Tmax=(6000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""

""",
)

entry(
    index=52,
    label="CH2CHO",
    molecule="""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.40906,
                    0.0107386,
                    1.89149e-06,
                    -7.15858e-09,
                    2.86738e-12,
                    1521.48,
                    9.55829,
                ],
                Tmin=(298, "K"),
                Tmax=(1000, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.97567,
                    0.00813059,
                    -2.74362e-06,
                    4.0703e-10,
                    -2.17602e-14,
                    490.322,
                    -5.04525,
                ],
                Tmin=(1000, "K"),
                Tmax=(5000, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(5000, "K"),
    ),
    reference=Reference(
        authors=[
            "G. P. Smith",
            "D. M. Golden",
            "M. Frenklach",
            "N. W. Moriarty",
            "B. Eiteneer",
            "M. Goldenberg",
            "C. T. Bowman",
            "R. K. Hanson",
            "S. Song",
            "W. C. Gardiner, Jr.",
            "V. V. Lissianski",
            "Z. Qin.",
        ],
        title="GRI-Mech 3.0.",
        year="1999",
        url="http://www.me.berkeley.edu/gri-mech/version30/text30.html",
    ),
    referenceType="review",
    shortDesc="""""",
    longDesc="""
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
)
