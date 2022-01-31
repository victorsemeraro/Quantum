from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc
import numpy as np

def single_shot_grovers(arr):
    
    p = Program()
    ro = p.declare('ro', 'BIT', len(arr))

    # Initialize the System to the Uniform Superposition Over all States
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    s = (1 / np.sqrt(len(arr))) * sum 

    # Grover Iteration


    # Measure the Result
    

    return 0

M = np.array([0, 0, 1, 0])
# print("Grovers Algorithm: ", single_shot_grovers(M))

def grovers_diffusion_operator(arr):

    I = np.eye(len(arr))
    print(I)

    e = 2 / len(arr)
    d = 2 / (len(arr)  - 1)
    A = d * I

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != d:
                A[i][j] = e

    G = A

    return G

print("Grovers Diffusion Operator: ", "\n", grovers_diffusion_operator(M))