#!/usr/bin/env python
# encoding: utf-8


name = "SurfaceThermoPt111"
shortDesc = "Surface adsorbates on Pt(111)"
longDesc = """
Some surface species adsorbed on Pt(111). The thermochemistry of all adsorbates with up to 2 heavy atoms was calculated by Katrin Blondal at Brown University around 2018,
based on DFT calculations by Jelena Jelic at KIT. See https://doi.org/10.1021/acs.iecr.9b01464 for the details on the computational methods as well as the results. This database was 
extended with DFT calculations for larger adsorbates by Bjarne Kreitz (Brown University). 
The computational methods for the extension are explained in detail in https://doi.org/10.1021/acscatal.2c03378. If you use this database in your work, please cite the publications mentioned above. 
Note: "-h" means "horizontal".
"""
#

entry(
    index=1,
    label="vacant",
    molecule="""
1 X  u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                    0.000000000e00,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(3000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(3000.0, "K"),
    ),
    metal="Pt",
    facet="111",
)

entry(
    index=2,
    label="H_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.96702988e00,
                    1.67920714e-02,
                    -2.50314139e-05,
                    1.80485455e-08,
                    -5.11491197e-12,
                    -3.21277026e03,
                    7.68211257e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.71968546e00,
                    -1.07696656e-03,
                    2.00193294e-06,
                    -1.12865983e-09,
                    2.11269165e-13,
                    -4.24701712e03,
                    -1.52793490e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.479 eV.
            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=3,
    label="H2_ads",
    molecule="""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.78935111e00,
                    1.10148021e-03,
                    -2.31320100e-06,
                    2.11937826e-09,
                    -6.31350224e-13,
                    -1.86700333e03,
                    -1.00616465e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.06700165e00,
                    -5.01780079e-04,
                    6.70738856e-07,
                    -1.79170942e-10,
                    8.86886631e-15,
                    -1.89107687e03,
                    -1.12621699e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.054 eV.
            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
            The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=4,
    label="H2O_ads",
    molecule="""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.53777266e00,
                    9.45372010e-03,
                    -1.41325664e-05,
                    1.16730945e-08,
                    -3.67657640e-12,
                    -3.27590463e04,
                    -5.36548561e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.84789466e00,
                    -3.31526816e-03,
                    5.62018785e-06,
                    -2.75864893e-09,
                    4.61279066e-13,
                    -3.34885608e04,
                    -2.15622699e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.189 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18932 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 49.5 and 68.6 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=5,
    label="OH_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.07348583e00,
                    1.72652206e-02,
                    -3.17712232e-05,
                    2.71536568e-08,
                    -8.69449304e-12,
                    -1.96002909e04,
                    -5.65622336e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.01870328e00,
                    -1.35424298e-03,
                    2.27686310e-06,
                    -1.09407298e-09,
                    1.79396487e-13,
                    -2.02979842e04,
                    -2.41159621e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.970 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18039 eV, gamma_O(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=6,
    label="HO-OH_ads",
    molecule="""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.83724199e00,
                    1.40375175e-02,
                    -1.46380418e-05,
                    8.15474904e-09,
                    -1.74266851e-12,
                    -2.52673006e04,
                    -5.58358715e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.63866612e00,
                    -4.64978374e-03,
                    8.11017779e-06,
                    -4.17891893e-09,
                    7.28657000e-13,
                    -2.67186621e04,
                    -3.48518226e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.286 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.28574 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 10.6 and 50.4 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=7,
    label="O2_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.44370346e-01,
                    2.11027468e-02,
                    -3.61266754e-05,
                    2.91032111e-08,
                    -9.01689834e-12,
                    -1.45323684e04,
                    -4.83356832e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.79639127e00,
                    -7.49042336e-04,
                    1.40680168e-06,
                    -7.97092567e-10,
                    1.49696529e-13,
                    -1.55278968e04,
                    -2.89715227e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.347 eV.
            Linear scaling parameters: ref_adatom_O1 = -3.586 eV, ref_adatom_O2 = -3.586 eV, psi = 3.23943 eV, gamma_O1(X) = 0.500, gamma_O2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=8,
    label="OOH_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.30951701e00,
                    1.58303400e-02,
                    -2.48037342e-05,
                    1.93368066e-08,
                    -5.83664367e-12,
                    -1.65355567e04,
                    -1.33537537e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.82755313e00,
                    -2.15021793e-03,
                    3.74021314e-06,
                    -1.91291320e-09,
                    3.31650646e-13,
                    -1.74991919e04,
                    -3.53134909e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.742 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.05105 eV, gamma_O(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=9,
    label="O_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.79722382e-01,
                    1.25453156e-02,
                    -2.29924588e-05,
                    1.94187177e-08,
                    -6.22414099e-12,
                    -1.73402246e04,
                    -2.22409728e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.92050897e00,
                    -2.70455589e-04,
                    5.15610634e-07,
                    -2.93911213e-10,
                    5.54030466e-14,
                    -1.78369003e04,
                    -1.50940536e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.586 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.00000 eV, gamma_O(X) = 1.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=10,
    label="O-NH2_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.40658689e00,
                    1.61838708e-02,
                    -1.58074626e-05,
                    8.48925729e-09,
                    -1.83038307e-12,
                    -8.83680682e03,
                    -7.56970401e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.42636683e00,
                    -5.74378741e-03,
                    1.01435819e-05,
                    -5.32742710e-09,
                    9.43135142e-13,
                    -1.06436383e04,
                    -4.31963080e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.698 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.09537 eV, gamma_O(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=11,
    label="O-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.88933974e00,
                    1.02968448e-02,
                    5.34962049e-06,
                    -1.25531705e-08,
                    5.32156610e-12,
                    -2.04952765e04,
                    -1.15047899e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.12817565e01,
                    -9.42267565e-03,
                    1.67985868e-05,
                    -8.95802947e-09,
                    1.60456258e-12,
                    -2.29996396e04,
                    -5.57516428e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.41957 eV, gamma_O(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=12,
    label="NH3_ads",
    molecule="""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.31496774e00,
                    1.46998289e-02,
                    -1.30679071e-05,
                    6.99360870e-09,
                    -1.52920905e-12,
                    -1.45305774e04,
                    -4.29992592e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.39460262e00,
                    -7.22640455e-03,
                    1.26169819e-05,
                    -6.50952664e-09,
                    1.13563586e-12,
                    -1.63659104e04,
                    -4.02856883e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.673 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67337 eV, gamma_N(X) = 0.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=13,
    label="NH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.89010759e00,
                    2.86217997e-02,
                    -4.34545237e-05,
                    3.34143285e-08,
                    -9.99500135e-12,
                    -4.87893528e03,
                    6.34997611e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.67968147e00,
                    -4.64266766e-03,
                    8.12871035e-06,
                    -4.20436074e-09,
                    7.35132153e-13,
                    -6.75225639e03,
                    -3.55181494e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.030 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.58258 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=14,
    label="NH_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.68663098e00,
                    2.89197486e-02,
                    -4.76398566e-05,
                    3.77368064e-08,
                    -1.14895177e-11,
                    -1.39698939e03,
                    9.81076735e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.82700699e00,
                    -2.46380210e-03,
                    4.35378855e-06,
                    -2.27895186e-09,
                    4.02508146e-13,
                    -2.92453268e03,
                    -2.63392973e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.440 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.54193 eV, gamma_N(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=15,
    label="N_ads",
    molecule="""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -8.62158075e-01,
                    1.65321723e-02,
                    -2.95187453e-05,
                    2.44741387e-08,
                    -7.73894837e-12,
                    4.56391760e03,
                    2.27263793e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.87812725e00,
                    -4.32547150e-04,
                    8.18868468e-07,
                    -4.65641564e-10,
                    8.76522110e-14,
                    3.86307901e03,
                    -1.54118153e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.352 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=16,
    label="H2N-OH_ads",
    molecule="""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.21930023e00,
                    1.83079214e-02,
                    -1.28981748e-05,
                    3.11969459e-09,
                    5.17141885e-13,
                    -1.53124559e04,
                    5.24764240e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.02488842e01,
                    -7.98164013e-03,
                    1.40252369e-05,
                    -7.31456224e-09,
                    1.28796464e-12,
                    -1.77173300e04,
                    -4.57361564e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.654 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.65407 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 17.1 and 68.9 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=17,
    label="HN-O_ads",
    molecule="""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.01921333e00,
                    1.32114264e-02,
                    -1.38865889e-05,
                    8.22652454e-09,
                    -2.08098816e-12,
                    -8.20311734e03,
                    -7.36585771e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.47524494e00,
                    -3.96252296e-03,
                    7.10187157e-06,
                    -3.81135483e-09,
                    6.86348467e-13,
                    -9.61232525e03,
                    -3.50542775e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=18,
    label="HN-OH_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -9.43834528e-02,
                    2.79801301e-02,
                    -3.68717092e-05,
                    2.54797165e-08,
                    -7.02746542e-12,
                    -1.18361390e04,
                    -1.14442838e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.44761833e00,
                    -5.66879769e-03,
                    1.00234569e-05,
                    -5.26997420e-09,
                    9.33985172e-13,
                    -1.40902663e04,
                    -4.85973626e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.08004 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=19,
    label="NO_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.91253452e00,
                    1.19742948e-02,
                    -1.74150740e-05,
                    1.31050130e-08,
                    -3.98440482e-12,
                    -1.39133497e04,
                    -9.50920619e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.58200160e00,
                    -1.44698193e-03,
                    2.66840782e-06,
                    -1.48667738e-09,
                    2.75613483e-13,
                    -1.47707534e04,
                    -2.76785587e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.580 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.13417 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=20,
    label="NO-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.23151905e00,
                    6.07214925e-03,
                    -7.46345407e-06,
                    5.43212687e-09,
                    -1.71496758e-12,
                    -1.16357520e04,
                    -1.30278030e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.54859951e00,
                    -1.48179602e-03,
                    2.71394293e-06,
                    -1.49952005e-09,
                    2.76147146e-13,
                    -1.22336367e04,
                    -2.47556107e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.390 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 1.51181 eV, gamma_N(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=21,
    label="NOH_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.02968349e-01,
                    2.37024940e-02,
                    -3.55330194e-05,
                    2.65623392e-08,
                    -7.77662656e-12,
                    -1.08269894e04,
                    -4.53311528e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.64521455e00,
                    -2.91720741e-03,
                    5.16378086e-06,
                    -2.71526676e-09,
                    4.81634389e-13,
                    -1.23572356e04,
                    -3.85225151e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.260 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.35381 eV, gamma_N(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=22,
    label="H2N-NH2_ads",
    molecule="""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.10937730e-01,
                    1.85814957e-02,
                    -5.98243737e-06,
                    -4.76023454e-09,
                    3.31121935e-12,
                    -2.75700009e03,
                    2.41162427e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.18367700e01,
                    -1.13177753e-02,
                    1.99338993e-05,
                    -1.04342217e-08,
                    1.84230855e-12,
                    -5.85969683e03,
                    -5.52432432e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.977 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.97746 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.9 and 79.2 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=23,
    label="HN-NH_ads",
    molecule="""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.62480603e-01,
                    2.37463930e-02,
                    -2.79127702e-05,
                    1.76454048e-08,
                    -4.52195226e-12,
                    1.08677882e04,
                    -3.53945184e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.40098406e00,
                    -5.98653308e-03,
                    1.06136322e-05,
                    -5.60544216e-09,
                    9.96914912e-13,
                    8.66255190e03,
                    -4.84441559e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.676 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67607 eV, gamma_N(X) = 0.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=24,
    label="NN_ads",
    molecule="""
1 X  u0 p0 c0 
2 N  u0 p1 c0 {3,T}
3 N  u0 p1 c0 {2,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.13993917e00,
                    -9.92755910e-04,
                    1.76704033e-06,
                    -1.57884342e-10,
                    -3.64206712e-13,
                    -4.38199802e03,
                    -7.98299353e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.38660517e00,
                    -1.50692391e-03,
                    2.67640594e-06,
                    -1.41531803e-09,
                    2.51363379e-13,
                    -4.48345747e03,
                    -9.36216462e00,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.109 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.10949 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=25,
    label="HN-NH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.47120056e-01,
                    2.68375643e-02,
                    -2.81255056e-05,
                    1.59595219e-08,
                    -3.61741193e-12,
                    5.50809497e03,
                    -2.02313697e000,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.11788248e01,
                    -8.42590935e-03,
                    1.48660894e-05,
                    -7.79652734e-09,
                    1.37881132e-12,
                    2.71736311e03,
                    -5.77901499e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.18029 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=26,
    label="N-NH_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.09323941e00,
                    1.85333628e-02,
                    -2.46837629e-05,
                    1.77191679e-08,
                    -5.17017679e-12,
                    1.00757302e04,
                    -5.67671443e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.47568498e00,
                    -3.83877359e-03,
                    6.87143107e-06,
                    -3.67728572e-09,
                    6.60773743e-13,
                    8.54387815e03,
                    -3.74961335e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.060 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.39360 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=27,
    label="N-NH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.70129737e-01,
                    2.46815562e-02,
                    -3.14357040e-05,
                    2.15189651e-08,
                    -5.94088667e-12,
                    5.19445129e03,
                    -4.18649200e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.37520921e00,
                    -5.75057579e-03,
                    1.01557341e-05,
                    -5.32940833e-09,
                    9.43101134e-13,
                    3.07692090e03,
                    -4.81449524e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.040 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.86160 eV, gamma_N(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=28,
    label="HN-NH-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.33495414e-01,
                    2.26610551e-02,
                    -2.36224444e-05,
                    1.28389765e-08,
                    -2.73372991e-12,
                    9.54917115e03,
                    -2.29491427e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.35953068e00,
                    -6.29553535e-03,
                    1.11894199e-05,
                    -5.93532774e-09,
                    1.05926511e-12,
                    7.23245336e03,
                    -4.84748217e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.982 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 1.91976 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=29,
    label="HN-N-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -9.33366824e-03,
                    2.28486010e-02,
                    -3.13931005e-05,
                    2.25104861e-08,
                    -6.48527412e-12,
                    7.54468891e03,
                    -1.63253226e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.45448958e00,
                    -3.87308208e-03,
                    6.93696999e-06,
                    -3.71519284e-09,
                    6.68194144e-13,
                    5.79074311e03,
                    -3.86806230e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.280 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 3.07184 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=30,
    label="HN-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.90039015e-01,
                    2.20932553e-02,
                    -9.26149163e-06,
                    -3.13927989e-09,
                    2.92569788e-12,
                    -5.59423948e03,
                    -2.83380870e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.30787664e01,
                    -1.20311946e-02,
                    2.13949410e-05,
                    -1.13636331e-08,
                    2.02934094e-12,
                    -9.10419311e03,
                    -6.80318827e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.850 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.40192 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=31,
    label="N-CH2_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.25178555e-01,
                    2.12826243e-02,
                    -2.34081427e-05,
                    1.47028746e-08,
                    -3.89854468e-12,
                    2.52272059e03,
                    -4.11114694e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.38157685e00,
                    -6.59021782e-03,
                    1.17682807e-05,
                    -6.28180522e-09,
                    1.12615562e-12,
                    3.18498804e02,
                    -4.78840793e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.660 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.21342 eV, gamma_N(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=32,
    label="N-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.57582464e-01,
                    2.08227846e-02,
                    -1.31666200e-05,
                    2.48777975e-09,
                    6.58681443e-13,
                    -5.31493961e03,
                    -3.12938558e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.12334649e01,
                    -9.61392101e-03,
                    1.71661622e-05,
                    -9.17060199e-09,
                    1.64510419e-12,
                    -8.26608573e03,
                    -5.86567081e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.050 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.14794 eV, gamma_N(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

# entry(
#     index = 33,
#     label = "ON-O_ads",
#     molecule =
# """
# 1 X  u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[
#              1.908949200E+00,   2.036846110E-02,  -3.030122180E-05,   2.191995790E-08,
#              -6.250090720E-12,   9.003214300E+03,  -2.726671970E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#             NASAPolynomial(coeffs=[
#              7.636130060E+00,  -1.383989810E-03,   2.571362700E-06,  -1.448349250E-09,
#              2.709019330E-13,   7.732608970E+03,  -3.081328960E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#         ],
#         Tmin = (298.0, 'K'),
#         Tmax = (2000.0, 'K'),
#     ),
#     longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb).
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.688 eV.
#            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#            The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.""",
# )

entry(
    index=34,
    label="C_ads",
    molecule="""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.73430697e00,
                    1.89855471e-02,
                    -3.23563661e-05,
                    2.59269890e-08,
                    -7.99102104e-12,
                    6.36385922e03,
                    6.25445028e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.82193241e00,
                    -6.61177416e-04,
                    1.24180431e-06,
                    -7.03993893e-10,
                    1.32276605e-13,
                    5.46467816e03,
                    -1.55251271e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.00000 eV, gamma_C(X) = 1.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=35,
    label="C-C_ads",
    molecule="""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.22282794e-01,
                    1.96908600e-02,
                    -3.07626817e-05,
                    2.35937440e-08,
                    -7.12438442e-12,
                    2.42830208e04,
                    -3.03635113e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.60759796e00,
                    -1.41921856e-03,
                    2.63409811e-06,
                    -1.47830656e-09,
                    2.75649745e-13,
                    2.31084908e04,
                    -2.93177601e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.910 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.84219 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=36,
    label="C-CH2_ads",
    molecule="""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.04785706e00,
                    3.38148654e-02,
                    -4.45775300e-05,
                    3.08318279e-08,
                    -8.56901355e-12,
                    -2.28268064e03,
                    6.64469050e000,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.42830381e00,
                    -6.48123487e-03,
                    1.15879773e-05,
                    -6.19494276e-09,
                    1.11218928e-12,
                    -5.01217502e03,
                    -5.04945175e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.60024 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=37,
    label="C-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.57603104e-01,
                    2.34293413e-02,
                    -1.86683661e-05,
                    7.29234370e-09,
                    -8.79008671e-13,
                    -1.12523534e04,
                    -1.73582278e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.13050336e01,
                    -9.40622931e-03,
                    1.67935678e-05,
                    -8.96901500e-09,
                    1.60855621e-12,
                    -1.42348165e04,
                    -5.88363790e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.590 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52567 eV, gamma_C(X) = 0.750.""",
    metal="Pt",
    facet="111",
)

entry(
    index=38,
    label="CH_ads",
    molecule="""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.00950779e00,
                    3.02193341e-02,
                    -4.99546294e-05,
                    3.99478464e-08,
                    -1.23021593e-11,
                    -3.13353859e03,
                    1.12314464e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    4.88482023e00,
                    -2.70846119e-03,
                    4.84648118e-06,
                    -2.58513645e-09,
                    4.63180319e-13,
                    -4.75082800e03,
                    -2.67870735e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.240 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.17590 eV, gamma_C(X) = 0.750.""",
    metal="Pt",
    facet="111",
)

entry(
    index=39,
    label="CH-CH_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.68898057e00,
                    3.52831263e-02,
                    -4.97578493e-05,
                    3.62176199e-08,
                    -1.04588699e-11,
                    2.14683932e02,
                    6.75238906e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.57180447e00,
                    -5.98074762e-03,
                    1.06737584e-05,
                    -5.68837233e-09,
                    1.01860349e-12,
                    -2.37703001e03,
                    -4.88869924e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.010 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 4.74337 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=40,
    label="CH-CH-vdw_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.11180282e00,
                    2.49061659e-02,
                    -3.96404401e-05,
                    3.23914869e-08,
                    -1.01975824e-11,
                    2.12123842e04,
                    4.05476651e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.55328593e00,
                    -4.89148968e-03,
                    8.55317549e-06,
                    -4.41304892e-09,
                    7.69510301e-13,
                    1.96129058e04,
                    -3.21219245e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.200 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20021 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 8.5 and 8.7 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=41,
    label="CH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.26602367e00,
                    2.92517765e-02,
                    -4.32728797e-05,
                    3.30655723e-08,
                    -9.93242641e-12,
                    -2.23619445e02,
                    8.22751288e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.82572636e00,
                    -5.17192506e-03,
                    9.19551938e-06,
                    -4.87101486e-09,
                    8.67713091e-13,
                    -2.26886621e03,
                    -3.64410753e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.640 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.26541 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=42,
    label="CH2-CH2_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.39737604e00,
                    3.73194353e-02,
                    -3.73140702e-05,
                    1.98435109e-08,
                    -4.15883994e-12,
                    -8.09105589e03,
                    9.52383811e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.32599664e01,
                    -1.17874099e-02,
                    2.10016909e-05,
                    -1.11823349e-08,
                    2.00074750e-12,
                    -1.21090188e04,
                    -6.98822356e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.950 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.42761 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=43,
    label="CH3_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.80099877e-01,
                    1.66399977e-02,
                    -1.39164870e-05,
                    6.70631582e-09,
                    -1.31079175e-12,
                    -6.31046932e03,
                    -7.57148375e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.67869881e00,
                    -7.84238420e-03,
                    1.38956076e-05,
                    -7.33600190e-09,
                    1.30321431e-12,
                    -8.45079729e03,
                    -4.20966823e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.770 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.08242 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=44,
    label="CH3-CH3_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.19974851e00,
                    7.93841719e-03,
                    2.69413164e-05,
                    -3.53453703e-08,
                    1.32207821e-11,
                    -1.45807566e04,
                    -1.67952705e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.59169609e01,
                    -1.75616860e-02,
                    3.12255463e-05,
                    -1.65874969e-08,
                    2.96156965e-12,
                    -1.86136199e04,
                    -6.98567509e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.219 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.21852 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 5.6 and 8.8 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=45,
    label="CH4_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.26247002e00,
                    -7.42703413e-03,
                    3.36472336e-05,
                    -3.29401150e-08,
                    1.10259250e-11,
                    -1.16038320e04,
                    -1.00920541e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.54981008e00,
                    -1.03719404e-02,
                    1.83183536e-05,
                    -9.63332916e-09,
                    1.70558531e-12,
                    -1.32717208e04,
                    -3.45374475e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.122 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.12206 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 3.2 and 8.1 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=46,
    label="CN_ads",
    molecule="""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,T}
3 N  u0  p1 c0 {2,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.11759999e00,
                    2.61925458e-03,
                    -2.38597242e-06,
                    1.99370899e-09,
                    -8.12410469e-13,
                    7.23851375e03,
                    -1.73631138e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.52418021e00,
                    -1.46883611e-03,
                    2.67356881e-06,
                    -1.46454792e-09,
                    2.67815680e-13,
                    6.83798413e03,
                    -2.46384099e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.340 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.64671 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=47,
    label="CNH_ads",
    molecule="""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.59496949e00,
                    1.65089177e-02,
                    -2.53974408e-05,
                    2.02468005e-08,
                    -6.32103397e-12,
                    -2.38409128e03,
                    -1.15883837e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.61905419e00,
                    -2.92187763e-03,
                    5.15479567e-06,
                    -2.69525498e-09,
                    4.75495658e-13,
                    -3.50064919e03,
                    -3.61906347e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.740 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.63638 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=48,
    label="CNH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.53087538e00,
                    2.16230806e-02,
                    -2.71329649e-05,
                    1.84938021e-08,
                    -5.09305792e-12,
                    -1.03698193e04,
                    -8.38468416e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.40468481e00,
                    -5.41327535e-03,
                    9.51693401e-06,
                    -4.95946907e-09,
                    8.72860901e-13,
                    -1.22719497e04,
                    -4.77373490e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.060 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.00119 eV, gamma_C(X) = 0.750.""",
    metal="Pt",
    facet="111",
)

entry(
    index=49,
    label="CO-f_ads",
    molecule="""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.70112272e00,
                    8.76650166e-03,
                    -1.29512418e-05,
                    1.04194594e-08,
                    -3.39700490e-12,
                    -3.49476634e04,
                    -1.28730512e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    5.52820880e00,
                    -1.52631254e-03,
                    2.79791895e-06,
                    -1.54550129e-09,
                    2.84523223e-13,
                    -3.56231280e04,
                    -2.69156979e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.480 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=50,
    label="COH_ads",
    molecule="""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    8.63437744e-01,
                    2.14806054e-02,
                    -3.00009525e-05,
                    2.11729011e-08,
                    -5.90923491e-12,
                    -3.09990999e04,
                    -5.10749731e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.59479056e00,
                    -3.06847382e-03,
                    5.43592647e-06,
                    -2.86463560e-09,
                    5.09149225e-13,
                    -3.25424988e04,
                    -3.83674793e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.260 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.80370 eV, gamma_C(X) = 0.750.""",
    metal="Pt",
    facet="111",
)

entry(
    index=51,
    label="H2C-CH_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.71741524e00,
                    4.45639232e-02,
                    -5.86622119e-05,
                    4.05880256e-08,
                    -1.12584803e-11,
                    -2.98721220e03,
                    1.37056124e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.14826601e01,
                    -8.87645080e-03,
                    1.58590687e-05,
                    -8.47088253e-09,
                    1.51944591e-12,
                    -6.59838559e03,
                    -6.19545665e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.770 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.29437 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=52,
    label="H2C-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    6.32861243e-01,
                    2.34315125e-02,
                    -6.21561097e-06,
                    -7.04743109e-09,
                    4.32504726e-12,
                    -1.03526448e04,
                    -4.22788616e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.50901779e01,
                    -1.47664787e-02,
                    2.62942501e-05,
                    -1.39941239e-08,
                    2.50255356e-12,
                    -1.44464142e04,
                    -7.55761454e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.06163 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=53,
    label="H2C-NH_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.22576461e-01,
                    2.08807519e-02,
                    -1.29691654e-05,
                    1.29682800e-09,
                    1.40594827e-12,
                    3.66393668e03,
                    6.82500696e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.02705016e01,
                    -9.06171664e-03,
                    1.61074586e-05,
                    -8.55119082e-09,
                    1.52673350e-12,
                    7.87732523e02,
                    -4.76927508e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.228 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.22807 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 46.0 and 79.7 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=54,
    label="H2C-NH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.94472063e-01,
                    2.62082323e-02,
                    -2.05472442e-05,
                    7.54576090e-09,
                    -5.98066735e-13,
                    -1.00349448e04,
                    -1.63394338e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.30763281e01,
                    -1.10941325e-02,
                    1.95968859e-05,
                    -1.03005801e-08,
                    1.82465302e-12,
                    -1.33699538e04,
                    -6.45023766e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.29283 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=55,
    label="H2C-O_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.87258154e00,
                    -3.80708439e-03,
                    2.29126729e-05,
                    -2.34870004e-08,
                    7.95457450e-12,
                    -2.09616356e04,
                    -1.09618928e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.42973399e00,
                    -6.84404724e-03,
                    1.22430399e-05,
                    -6.56317791e-09,
                    1.18019535e-12,
                    -2.23198421e04,
                    -3.11097315e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.184 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.18361 eV, gamma_C(X) = 0.000.""",
    metal="Pt",
    facet="111",
)

entry(
    index=56,
    label="H2C-OH_ads",
    molecule="""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    6.90559347e-01,
                    2.31880081e-02,
                    -1.92723889e-05,
                    7.42264515e-09,
                    -6.88671342e-13,
                    -3.54054895e04,
                    -1.78049680e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.13189670e01,
                    -8.55328894e-03,
                    1.51576215e-05,
                    -8.00760803e-09,
                    1.42446093e-12,
                    -3.82049819e04,
                    -5.60575095e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.890 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.19820 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=57,
    label="H2CN-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -8.02719609e-01,
                    2.77232113e-02,
                    -3.31822780e-05,
                    2.12596176e-08,
                    -5.54256988e-12,
                    2.08108433e03,
                    1.56425884e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.43341136e00,
                    -6.49223331e-03,
                    1.16024225e-05,
                    -6.20150120e-09,
                    1.11316221e-12,
                    -4.41424500e02,
                    -4.98315612e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.710 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.37462 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=58,
    label="H2CNH-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.22318867e00,
                    4.08379516e-02,
                    -5.08218184e-05,
                    3.33893656e-08,
                    -8.81880680e-12,
                    -2.40066395e03,
                    1.16307500e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.13347841e01,
                    -8.90691781e-03,
                    1.58626750e-05,
                    -8.43510814e-09,
                    1.50807029e-12,
                    -5.92362341e03,
                    -6.11697683e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.756 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.75753 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=59,
    label="H3C-NH2_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    7.90575940e-01,
                    1.65852324e-02,
                    6.48184437e-06,
                    -1.79298156e-08,
                    7.87674440e-12,
                    -1.51012090e04,
                    2.42587438e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.37729719e01,
                    -1.46798316e-02,
                    2.60099894e-05,
                    -1.37425622e-08,
                    2.44401396e-12,
                    -1.89207219e04,
                    -6.57899167e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.879 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.87925 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.6 and 84.5 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=60,
    label="H3C-OH_ads",
    molecule="""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.70506726e00,
                    1.00913594e-02,
                    1.00260680e-05,
                    -1.80909603e-08,
                    7.44539499e-12,
                    -3.09647604e04,
                    -4.48135960e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.21539459e01,
                    -1.13173411e-02,
                    2.00342036e-05,
                    -1.05724068e-08,
                    1.87852776e-12,
                    -3.38115989e04,
                    -5.44617359e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.316 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.31650 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.5 and 57.9 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=61,
    label="HC-C_ads",
    molecule="""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    5.41170551e-02,
                    2.52700921e-02,
                    -3.75803933e-05,
                    2.82910883e-08,
                    -8.39575978e-12,
                    1.42484565e04,
                    -1.63766387e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.62295055e00,
                    -3.43322498e-03,
                    6.14771846e-06,
                    -3.28932116e-09,
                    5.91021494e-13,
                    1.25529905e04,
                    -3.88019444e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.100 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.96689 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

# This is actually bidentate, so this input is not correct (should be the same as index 51).
# entry(
#    index = 62,
#    label = "HC-CH2_ads",
#    molecule =
# """
# 1 X  u0  p0 c0 {2,S}
# 2 C  u0  p0 c0 {1,S} {3,D} {4,S}
# 3 C  u0  p0 c0 {2,D} {5,S} {6,S}
# 4 H  u0  p0 c0 {2,S}
# 5 H  u0  p0 c0 {3,S}
# 6 H  u0  p0 c0 {3,S}
# """,
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[
#             -3.761998800E+00,   4.463873830E-02,  -5.865136870E-05,   4.048714140E-08,
#             -1.120403080E-11,  -2.545452840E+03,   1.391918370E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[
#             1.147737520E+01,  -8.889811580E-03,   1.588277200E-05,  -8.483602150E-09,
#             1.521747930E-12,  -6.167735370E+03,  -6.194706680E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0, 'K'),
#        Tmax = (2000.0, 'K'),
#    ),
#    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb).
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -2.790 eV.
#            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.09643 eV, gamma_C(X) = 0.250.""",
# )

entry(
    index=63,
    label="HC-CH3_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.39195145e-01,
                    2.71965302e-02,
                    -1.96479590e-05,
                    6.17925647e-09,
                    -1.84661314e-13,
                    -5.60696357e03,
                    2.67225219e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.32714698e01,
                    -1.19649775e-02,
                    2.13410724e-05,
                    -1.13827464e-08,
                    2.03915294e-12,
                    -9.25414727e03,
                    -6.90961026e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.580 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20205 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=64,
    label="HCN_ads",
    molecule="""
1 X  u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 H  u0  p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.17889171e00,
                    1.61639690e-02,
                    -2.31637957e-05,
                    1.78894661e-08,
                    -5.51067178e-12,
                    1.10206116e04,
                    1.94585596e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.54320202e00,
                    -3.51550718e-03,
                    6.26384435e-06,
                    -3.32803966e-09,
                    5.94359917e-13,
                    9.77019618e03,
                    -2.63488571e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.010 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.00995 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 51.9 and 72.8 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=65,
    label="HCN-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.45901289e-02,
                    2.36120976e-02,
                    -3.37215849e-05,
                    2.50959079e-08,
                    -7.46308917e-12,
                    3.55589882e03,
                    -1.50225522e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.52979178e00,
                    -3.89004433e-03,
                    6.99537195e-06,
                    -3.76746392e-09,
                    6.80266036e-13,
                    1.81662108e03,
                    -3.86174029e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.650 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 2.37733 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.667.""",
    metal="Pt",
    facet="111",
)

entry(
    index=66,
    label="HCNH_ads",
    molecule="""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    8.05598404e-01,
                    2.12578896e-02,
                    -2.26826133e-05,
                    1.31095137e-08,
                    -3.07357265e-12,
                    4.10897731e01,
                    -1.71828775e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.39843610e00,
                    -6.24337353e-03,
                    1.11012002e-05,
                    -5.89092739e-09,
                    1.05148038e-12,
                    -2.13728786e03,
                    -4.51639342e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.220 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52691 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=67,
    label="HCNH-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.13239946e00,
                    2.98484244e-02,
                    -3.78145776e-05,
                    2.53616976e-08,
                    -6.86307261e-12,
                    -3.16836112e03,
                    3.30113143e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.37828967e00,
                    -6.30048833e-03,
                    1.12203407e-05,
                    -5.96428012e-09,
                    1.06621044e-12,
                    -5.70392882e03,
                    -4.92130115e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.490 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.71054 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.""",
    metal="Pt",
    facet="111",
)

entry(
    index=68,
    label="HCNH2_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.11835944e-01,
                    2.41104719e-02,
                    -2.20379983e-05,
                    1.06103035e-08,
                    -1.92226443e-12,
                    -7.35704782e03,
                    -2.41270253e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.11491706e01,
                    -8.75052593e-03,
                    1.54802187e-05,
                    -8.15334058e-09,
                    1.44682582e-12,
                    -1.01528629e04,
                    -5.48979853e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.670 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.70666 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=69,
    label="HCO_ads",
    molecule="""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.94156388e00,
                    1.30882912e-02,
                    -1.34260003e-05,
                    7.97044677e-09,
                    -2.06719711e-12,
                    -2.80413711e04,
                    -5.97802577e0,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.49136303e00,
                    -4.18949199e-03,
                    7.54544313e-06,
                    -4.07863095e-09,
                    7.38421146e-13,
                    -2.94916141e04,
                    -3.42076640e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.210 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52049 eV, gamma_C(X) = 0.250.""",
    metal="Pt",
    facet="111",
)

entry(
    index=70,
    label="HCO-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -7.63229192e-02,
                    2.34818104e-02,
                    -3.17556441e-05,
                    2.22347561e-08,
                    -6.25650920e-12,
                    -2.44241519e04,
                    -1.42351290e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    7.61171587e00,
                    -3.81051175e-03,
                    6.86938717e-06,
                    -3.71585312e-09,
                    6.73352174e-13,
                    -2.62393600e04,
                    -3.96330591e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.900 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.99512 eV, gamma_C1(X) = 0.500, gamma_O2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=71,
    label="HCOH_ads",
    molecule="""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.68649725e-01,
                    2.04972050e-02,
                    -1.85506813e-05,
                    8.22998468e-09,
                    -1.23251062e-12,
                    -2.63024443e04,
                    -9.21769145e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.39449002e00,
                    -6.56375678e-03,
                    1.17141780e-05,
                    -6.25387815e-09,
                    1.12161443e-12,
                    -2.86359494e04,
                    -4.64113344e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.960 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.42191 eV, gamma_C(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=72,
    label="H2CO-h_ads",
    molecule="""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.02400610e-01,
                    2.37197512e-02,
                    -2.57930815e-05,
                    1.52033151e-08,
                    -3.68397327e-12,
                    -2.14196483e04,
                    -4.98129327e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.52719632e00,
                    -6.50602819e-03,
                    1.16581384e-05,
                    -6.25773731e-09,
                    1.12684291e-12,
                    -2.38121944e04,
                    -4.81511621e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298.0, "K"),
        Tmax=(2000.0, "K"),
    ),
    longDesc="""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.236 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.96700 eV, gamma_C1(X) = 0.250, gamma_O2(X) = 0.500.""",
    metal="Pt",
    facet="111",
)

entry(
    index=73,
    label="COOH_ads",
    molecule="""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.59051461e-01,
                    2.50172545e-02,
                    -3.09587526e-05,
                    2.00287012e-08,
                    -5.26520494e-12,
                    -5.77593927e04,
                    3.53119101e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.16264817e00,
                    -4.70146235e-03,
                    8.43555601e-06,
                    -4.53366378e-09,
                    8.17971447e-13,
                    -5.99111113e04,
                    -4.05936773e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied: kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2.DFT binding energy: -2.571 eV. The two lowest frequencies, 36.7 and 64.6 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=74,
    label="CO2_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.00959799e00,
                    1.33597565e-02,
                    -1.62303912e-05,
                    1.10029585e-08,
                    -3.14484550e-12,
                    -5.27878435e04,
                    -2.58903015e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    6.98298937e00,
                    -3.09872260e-03,
                    5.62883746e-06,
                    -3.07847748e-09,
                    5.62449582e-13,
                    -5.40395049e04,
                    -2.76481477e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied: kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2.DFT binding energy: -0.062 eV. The two lowest frequencies, 10.8 and 12.0 cm-1, where replaced by the 2D gas model. The heat of formation of CO2 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index=75,
    label="HCOO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.61659601e00,
                    1.91323831e-02,
                    -1.56426057e-05,
                    5.33726639e-09,
                    -3.02650266e-13,
                    -5.40963560e04,
                    -8.06287760e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.01220820e01,
                    -5.52918679e-03,
                    1.00078607e-05,
                    -5.45403486e-09,
                    9.94268481e-13,
                    -5.63827709e04,
                    -5.17074860e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.606 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=76,
    label="CH2CO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.89187265e-01,
                    2.92112653e-02,
                    -3.68630528e-05,
                    2.57772068e-08,
                    -7.38835035e-12,
                    -2.28623191e04,
                    3.26236781e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.10991553e01,
                    -7.40804127e-03,
                    1.32480136e-05,
                    -7.08463685e-09,
                    1.27176536e-12,
                    -2.54828850e04,
                    -5.03667784e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.619 eV. The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=77,
    label="CH3CO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.23038408e00,
                    2.13641887e-02,
                    -1.09879577e-05,
                    -4.08548110e-10,
                    1.72792683e-12,
                    -3.60116136e04,
                    4.16359473e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.28961233e01,
                    -1.06029491e-02,
                    1.89557851e-05,
                    -1.01458960e-08,
                    1.82293047e-12,
                    -3.92596953e04,
                    -5.99504141e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.551 eV. The two lowest frequencies, 23.8 and 88.9 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=78,
    label="CHCO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.37761371e00,
                    3.72565997e-02,
                    -5.30168625e-05,
                    3.85555128e-08,
                    -1.11934628e-11,
                    -2.69999496e04,
                    3.96229085e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.01988493e01,
                    -5.11717278e-03,
                    9.26394034e-06,
                    -5.03840097e-09,
                    9.16957643e-13,
                    -2.96733996e04,
                    -5.32680120e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.460 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=79,
    label="CCHCH2_ads",
    molecule="""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.25479749e00,
                    3.76847805e-02,
                    -3.93538492e-05,
                    2.16708327e-08,
                    -4.77858725e-12,
                    -2.91574221e03,
                    4.10178815e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.39365153e01,
                    -1.03605118e-02,
                    1.85207758e-05,
                    -9.90839299e-09,
                    1.77999302e-12,
                    -6.79286011e03,
                    -7.28413395e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -5.430 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=80,
    label="CHCHCH2_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {8,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -4.00241403e00,
                    5.22189088e-02,
                    -5.89122044e-05,
                    3.51035783e-08,
                    -8.41934161e-12,
                    -2.62744487e03,
                    1.50822089e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.59486678e01,
                    -1.28837296e-02,
                    2.30283272e-05,
                    -1.23167595e-08,
                    2.21202132e-12,
                    -7.61190609e03,
                    -8.54536705e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -4.131 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=81,
    label="CHCHCH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.57393128e00,
                    4.77399245e-02,
                    -4.59807447e-05,
                    2.35135768e-08,
                    -4.74550260e-12,
                    -8.29333311e03,
                    9.44154348e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.79080385e01,
                    -1.55492702e-02,
                    2.77729619e-05,
                    -1.48415413e-08,
                    2.66313378e-12,
                    -1.36082222e04,
                    -9.46976696e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.399 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=82,
    label="CH3CHCH2_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.01283183e00,
                    3.96054673e-02,
                    -2.41796124e-05,
                    3.23567437e-09,
                    1.99314176e-12,
                    -1.04958272e04,
                    3.34183380e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.95941002e01,
                    -1.84981215e-02,
                    3.29579796e-05,
                    -1.75535179e-08,
                    3.14139881e-12,
                    -1.61291822e04,
                    -1.02828351e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.713 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=83,
    label="CH2CH2CH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -5.78976324e-01,
                    3.71915827e-02,
                    -1.22898025e-05,
                    -8.77177071e-09,
                    6.04039735e-12,
                    -1.44128666e04,
                    1.47277870e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.15363954e01,
                    -2.15932574e-02,
                    3.85299240e-05,
                    -2.05691913e-08,
                    3.68755975e-12,
                    -2.06558044e04,
                    -1.13399138e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.333 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=84,
    label="CH3CH2CH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.15856144e00,
                    2.48539972e-02,
                    1.53525973e-05,
                    -3.25302366e-08,
                    1.35067652e-11,
                    -1.91235202e04,
                    -8.74139325e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.32832355e01,
                    -2.45407014e-02,
                    4.37313468e-05,
                    -2.33036993e-08,
                    4.17150294e-12,
                    -2.54500100e04,
                    -1.20201845e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.241 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=85,
    label="CH2CCH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.72979307e00,
                    4.77487399e-02,
                    -4.57827060e-05,
                    2.34519012e-08,
                    -4.78486001e-12,
                    -9.28933791e03,
                    9.23470861e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.78566754e01,
                    -1.57310158e-02,
                    2.81077398e-05,
                    -1.50276611e-08,
                    2.69754383e-12,
                    -1.46426673e04,
                    -9.54811248e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.195 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=86,
    label="CH3CHCH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.40036274e-01,
                    3.58616425e-02,
                    -1.11021659e-05,
                    -8.97397908e-09,
                    5.91635074e-12,
                    -1.50319218e04,
                    -9.77178836e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.15065179e01,
                    -2.15386628e-02,
                    3.84133775e-05,
                    -2.04904605e-08,
                    3.67103983e-12,
                    -2.11553220e04,
                    -1.13463590e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.157 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=87,
    label="CH2CHCH2-h_ads",
    molecule="""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  X u0 p0 c0 {1,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.02780964e00,
                    4.86827920e-02,
                    -4.64697726e-05,
                    2.28751861e-08,
                    -4.23877600e-12,
                    -1.00974953e04,
                    1.15070732e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.77787700e01,
                    -1.55322169e-02,
                    2.76898539e-05,
                    -1.47575432e-08,
                    2.64275606e-12,
                    -1.54845701e04,
                    -9.42606313e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.286 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=88,
    label="CO3_ads",
    molecule="""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  O u0 p2 c0 {1,D} 
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {1,S} {6,S}
5  X u0 p0 c0 {3,S}
6  X u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.60792367e-01,
                    2.96600289e-02,
                    -3.74624110e-05,
                    2.35857040e-08,
                    -5.97914773e-12,
                    -6.29108649e04,
                    4.32145289e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.00467967e01,
                    -3.51639012e-03,
                    6.49178066e-06,
                    -3.63351889e-09,
                    6.76298145e-13,
                    -6.52863404e04,
                    -4.46693341e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.027 eV. The two lowest frequencies, 89.5 and 92.5 cm-1, where replaced by the 2D gas model. The heat of formation of CO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index=89,
    label="HCO3_ads",
    molecule="""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.01328212e00,
                    3.26276222e-02,
                    -3.70609785e-05,
                    2.09604143e-08,
                    -4.66694045e-12,
                    -7.71501268e04,
                    -4.75360741e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.28523396e01,
                    -5.70822904e-03,
                    1.02857884e-05,
                    -5.56715096e-09,
                    1.01065162e-12,
                    -8.01071414e04,
                    -6.44493277e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.365 eV. The heat of formation of HCO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index=90,
    label="HCOOH_ads",
    molecule="""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.35698005e00,
                    1.65817950e-02,
                    -8.93246966e-06,
                    -5.96590960e-10,
                    1.65711542e-12,
                    -5.37225169e04,
                    -5.39293969e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.10477913e01,
                    -7.24274370e-03,
                    1.29091018e-05,
                    -6.88021503e-09,
                    1.23289550e-12,
                    -5.61258326e04,
                    -4.54689420e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.216 eV. The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=91,
    label="HCO2CH3_ads",
    molecule="""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.37688850e00,
                    1.71682950e-02,
                    1.02263070e-05,
                    -2.31122378e-08,
                    9.75945366e-12,
                    -5.67118072e04,
                    -7.58680924e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.73815092e01,
                    -1.48389347e-02,
                    2.65610657e-05,
                    -1.42501123e-08,
                    2.56517842e-12,
                    -6.09344090e04,
                    -8.16429248e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.318 eV. The two lowest frequencies, 62.9 and 75.5 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=92,
    label="H2CO2CH3_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {10,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    1.68079896e00,
                    3.12126215e-02,
                    -8.07893400e-06,
                    -1.08377033e-08,
                    6.48220713e-12,
                    -4.78338034e04,
                    -5.80786049e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    2.04132198e01,
                    -1.73601838e-02,
                    3.10764492e-05,
                    -1.66713256e-08,
                    3.00083064e-12,
                    -5.31769352e04,
                    -1.03396841e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -1.997 eV. (This could also be considered as a bidentate)""",
    metal="Pt",
    facet="111",
)

entry(
    index=93,
    label="H2CO2_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 O u0 p2 c0 {2,S} {7,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {5,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.69923804e-01,
                    2.86585416e-02,
                    -2.78936419e-05,
                    1.36526428e-08,
                    -2.53912516e-12,
                    -3.69470080e04,
                    -3.70031423e-01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.22233961e01,
                    -7.74165833e-03,
                    1.39418350e-05,
                    -7.54192659e-09,
                    1.36669487e-12,
                    -4.00280609e04,
                    -6.06800543e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.554 eV. (No stable gas-phase species)""",
    metal="Pt",
    facet="111",
)


entry(
    index=94,
    label="OCH2CH3_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.61067651e-01,
                    2.53309271e-02,
                    -2.95243491e-06,
                    -1.26602001e-08,
                    6.61140934e-12,
                    -2.62935878e04,
                    3.46251964e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.67501781e01,
                    -1.61554398e-02,
                    2.88603109e-05,
                    -1.54358268e-08,
                    2.77154673e-12,
                    -3.09818842e04,
                    -8.15935002e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -1.905 eV. The two lowest frequencies, 12.0 and 92.3 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=95,
    label="CCCH2_ads",
    molecule="""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -3.82821995e-01,
                    3.18369145e-02,
                    -4.01391269e-05,
                    2.76197052e-08,
                    -7.78850595e-12,
                    1.14754087e04,
                    5.76357647e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.11180258e01,
                    -7.40595551e-03,
                    1.32616442e-05,
                    -7.10517630e-09,
                    1.27762668e-12,
                    8.66373268e03,
                    -5.18305539e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.773 eV. The two lowest frequencies, 12.0 and 99.7 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=96,
    label="CCCH2-h_ads",
    molecule="""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.27103445e00,
                    4.27539019e-02,
                    -5.61652527e-05,
                    3.84419292e-08,
                    -1.06004164e-11,
                    1.37333466e04,
                    6.93062665e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.21290474e01,
                    -7.57219828e-03,
                    1.36015955e-05,
                    -7.32089312e-09,
                    1.32157610e-12,
                    1.02970059e04,
                    -6.48251627e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.582 eV. The two lowest frequencies, 12.0 and 99.7 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=97,
    label="CCH2CH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -4.07836856e-01,
                    3.38179738e-02,
                    -1.82365043e-05,
                    -2.17799277e-10,
                    2.78237156e-12,
                    -1.53170989e04,
                    3.03397088e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.76952935e01,
                    -1.61873878e-02,
                    2.89121382e-05,
                    -1.54560860e-08,
                    2.77424706e-12,
                    -2.03225660e04,
                    -9.05055229e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -6.099 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=98,
    label="CCH2OH_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -4.14367704e-01,
                    2.97866357e-02,
                    -2.42611023e-05,
                    8.22145796e-09,
                    -2.81785012e-13,
                    -2.93557009e04,
                    7.22298177e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.30250135e01,
                    -9.79365971e-03,
                    1.74609646e-05,
                    -9.31041024e-09,
                    1.66893053e-12,
                    -3.29194661e04,
                    -6.15374355e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -5.950 eV. The two lowest frequencies, 12.0 and 51.0 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=99,
    label="CCHO_ads",
    molecule="""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.54881082e-01,
                    2.46650429e-02,
                    -2.78829260e-05,
                    1.67435167e-08,
                    -4.17255119e-12,
                    -2.30389364e04,
                    5.36584771e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    9.17648225e00,
                    -5.39008423e-03,
                    9.76740931e-06,
                    -5.32718475e-09,
                    9.71578780e-13,
                    -2.54039985e04,
                    -4.17920992e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -5.378 eV. The two lowest frequencies, 20.1 and 76.7 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=100,
    label="CCO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.82296413e-01,
                    2.58715605e-02,
                    -3.93603870e-05,
                    3.04629746e-08,
                    -9.36533490e-12,
                    -2.01388552e04,
                    -3.57376015e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    8.07081859e00,
                    -3.00851572e-03,
                    5.51539311e-06,
                    -3.04805549e-09,
                    5.61469009e-13,
                    -2.18535359e04,
                    -4.08625858e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -5.276 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=101,
    label="CH3CH2CO_ads",
    molecule="""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {2,S} {10,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    3.17980384e-01,
                    3.37808273e-02,
                    -1.47996341e-05,
                    -3.84914220e-09,
                    3.93637206e-12,
                    -3.72477194e04,
                    3.57589905e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.93377956e01,
                    -1.74343755e-02,
                    3.11976589e-05,
                    -1.67226574e-08,
                    3.00798190e-12,
                    -4.25883073e04,
                    -9.50685040e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.348 eV. The two lowest frequencies, 12.0 and 63.5 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=102,
    label="CH3CH2OH_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
10 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.44141648e00,
                    2.01418511e-02,
                    1.00444529e-05,
                    -2.46324618e-08,
                    1.06436492e-11,
                    -3.27245208e04,
                    -2.15863074e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.85992615e01,
                    -1.79442101e-02,
                    3.18809278e-05,
                    -1.69157790e-08,
                    3.01870762e-12,
                    -3.75223426e04,
                    -8.72712384e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.023 eV. The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=103,
    label="CH3CHOH_ads",
    molecule="""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -9.38075627e-02,
                    3.25418587e-02,
                    -1.95081006e-05,
                    1.90337747e-09,
                    2.01784423e-12,
                    -3.55702904e04,
                    5.48133949e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.68236097e01,
                    -1.50325950e-02,
                    2.67326715e-05,
                    -1.41983594e-08,
                    2.53584549e-12,
                    -4.01922375e04,
                    -8.16882260e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.332 eV. The two lowest frequencies, 12.0 and 96.1 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=104,
    label="CH3COH_ads",
    molecule="""
1 O u0 p2 c0 {3,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -2.76577612e-01,
                    3.17759863e-02,
                    -2.80855737e-05,
                    1.30653955e-08,
                    -2.28758679e-12,
                    -3.51324540e04,
                    6.43691395e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.41585643e01,
                    -1.19340084e-02,
                    2.12465017e-05,
                    -1.12990846e-08,
                    2.01967067e-12,
                    -3.89269552e04,
                    -6.71888781e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.952 eV. The two lowest frequencies, 12.0 and 58.0 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=105,
    label="CHCCH2_ads",
    molecule="""
1 C u0 p0 c0 {3,D} {4,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.47420628e00,
                    4.21450105e-02,
                    -5.01975896e-05,
                    3.19228373e-08,
                    -8.24990770e-12,
                    8.39600503e03,
                    6.36468208e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.41133329e01,
                    -9.85218182e-03,
                    1.76095803e-05,
                    -9.41496495e-09,
                    1.69037771e-12,
                    4.55106546e03,
                    -7.19224209e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.423 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=106,
    label="CHCH2CH3_ads",
    molecule="""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    -1.60792265e00,
                    3.65072698e-02,
                    -1.73028330e-05,
                    -2.63268524e-09,
                    3.77289172e-12,
                    -7.90376874e03,
                    1.17218751e01,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.86868441e01,
                    -1.88617963e-02,
                    3.36944612e-05,
                    -1.80170490e-08,
                    3.23426057e-12,
                    -1.35592834e04,
                    -9.33362093e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.650 eV. The two lowest frequencies, 12.0 and 74.1 cm-1, where replaced by the 2D gas model.""",
    metal="Pt",
    facet="111",
)

entry(
    index=107,
    label="CH3CCH3_ads",
    molecule="""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    4.03765346e-01,
                    3.43477499e-02,
                    -1.58933907e-05,
                    -2.43971983e-09,
                    3.40954348e-12,
                    -1.01401151e04,
                    -2.81376113e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.97785534e01,
                    -1.85076861e-02,
                    3.30425254e-05,
                    -1.76515167e-08,
                    3.16607226e-12,
                    -1.55475137e04,
                    -1.03131111e02,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -3.420 eV.""",
    metal="Pt",
    facet="111",
)

entry(
    index=108,
    label="CH3CHO_ads",
    molecule="""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(
                coeffs=[
                    2.76865237e00,
                    1.54209040e-02,
                    5.76787174e-06,
                    -1.58270365e-08,
                    6.75180571e-12,
                    -3.01424357e04,
                    -5.05547920e00,
                ],
                Tmin=(298.0, "K"),
                Tmax=(1000.0, "K"),
            ),
            NASAPolynomial(
                coeffs=[
                    1.48477497e01,
                    -1.33581956e-02,
                    2.38689301e-05,
                    -1.27693401e-08,
                    2.29305318e-12,
                    -3.37383429e04,
                    -6.86709011e01,
                ],
                Tmin=(1000.0, "K"),
                Tmax=(2000.0, "K"),
            ),
        ],
        Tmin=(298, "K"),
        Tmax=(2000, "K"),
    ),
    longDesc="""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -0.259 eV. The two lowest frequencies, 30.5 and 72.0 cm-1, where replaced by the 2D gas model..""",
    metal="Pt",
    facet="111",
)
