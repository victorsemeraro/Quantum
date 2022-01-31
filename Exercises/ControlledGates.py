from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc
from pyquil.api import WavefunctionSimulator
import numpy as np

def controlled(arr):
    # Hadamard Transform
    # Kronecker Product 

    p = Program()
    ro = p.declare('ro', 'BIT', len(arr) * len(arr))

    for i in range(len(arr)):

        p += CNOT(0, 1)

        for j in range(len(arr[i])):

            p += MEASURE(j, ro[i])  

    qc = get_qc('Aspen-11-qvm') 
    executable = qc.compile(p)
    result = qc.run(executable)
    bitstrings = result.readout_data.get('ro')
    
    CQ = np.zeros((len(arr), len(arr)))
    for i in range(len(bitstrings)):
        for j in range(len(bitstrings[i])):
            CQ[i][j] = bitstrings[i][j]

    U = np.kron(CQ, CQ)

    return U

U = np.array([[1, 1], [1 , 1]])
print("Controlled Gates: ", "\n", controlled(U))

def controlledWaveFunction():

    wf_sim = WavefunctionSimulator()
    coin_flip = Program(Y(1))
    wf_sim.wavefunction(coin_flip)

    coin_flip = Program(Y(1))
    wavefunction = wf_sim.wavefunction(coin_flip)
    print("Quantum State Amplitude: ", wavefunction)

    print("Amplitude As Array: ", wavefunction.amplitudes)
    prob_dict = wavefunction.get_outcome_probs()
    print("Probabilities: ", prob_dict)
    prob_dict.keys()

    return prob_dict

print("Controlled Wavefunction: ", controlledWaveFunction())