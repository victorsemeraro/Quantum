import numpy as np
from pyquil.quilbase import DefGate

ccnot_matrix = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0]
])

ccnot_gate = DefGate("CCNOT", ccnot_matrix)

from pyquil.quilbase import DefPermutationGate

ccnot_gate = DefPermutationGate("CCNOT", [0, 1, 2, 3, 4, 5, 7, 6])