from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator
import numpy as np

def quantum_fourier():

    state_prep = Program(X(0))

    add_dummy_qubits = Program(I(1), I(2))

    wf_sim = WavefunctionSimulator()
    wavefunction = wf_sim.wavefunction(state_prep + add_dummy_qubits)
    print(wavefunction)

    compute_qft_prog = state_prep + qft3(0, 1, 2)
    wavefunction = wf_sim.wavefunction(compute_qft_prog)
    print(wavefunction.amplitudes)

    npfft = np.ifft(wavefunction.amplitudes, norm="ortho")
    print(npfft)

    return 0

def qft3(q0, q1, q2):

    p = Program()
    p += [SWAP(q0, q2),
          H(q0),
          CPHASE(-np.pi / 2.0, q0, q1),
          H(q1),
          CPHASE(-np.pi / 4.0, q0, q2),
          CPHASE(-np.pi / 2.0, q1, q2),
          H(q2)]

    return p