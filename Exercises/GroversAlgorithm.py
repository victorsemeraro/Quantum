from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc
import numpy as np

def single_shot_grovers():

    return 0

M = np.array([0, 0, 1, 0])
print("Grovers Algorithm: ", single_shot_grovers(M))