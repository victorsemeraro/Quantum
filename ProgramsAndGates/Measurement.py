from pyquil import Program
from pyquil.gates import *

p = Program()
qubits = [5, 6, 7]
ro = p.declare('ro', 'BIT', len(qubits))
p += H(0)
p += CNOT(0, 1)

for i, q in enumerate(qubits):
    p += MEASURE(q, ro[i])

print(p)

