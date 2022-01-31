from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator
import numpy as np

wf_sim = WavefunctionSimulator()
coin_flip = Program(H(0))
wf_sim.wavefunction(coin_flip)

coin_flip = Program(H(0))
wavefunction = wf_sim.wavefunction(coin_flip)
print("Quantum State Amplitude: ", wavefunction)

assert wavefunction[0] == 1 / np.sqrt(2)
print("Amplitude As Array: ", wavefunction.amplitudes)
prob_dict = wavefunction.get_outcome_probs()
print("Probabilities: ", prob_dict)
prob_dict.keys()
assert len(wavefunction) == 1