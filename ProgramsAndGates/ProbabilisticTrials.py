from pyquil import Program
from pyquil.gates import *

p = Program()

N = 16
qubits = []
for i in range(16):
    qubits.append(i)

ro = p.declare('ro', 'BIT', len(qubits))

for i, q in enumerate(qubits):
    p += MEASURE(q, ro[i])

print(p)

p.wrap_in_numshots_loop(1000)