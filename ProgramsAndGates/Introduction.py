from pyquil import Program
from pyquil.gates import *

p = Program()
ro = p.declare('ro', 'BIT', 1)
p += X(0)
p += MEASURE(0, ro[0])

print(p)

from pyquil import get_qc

qc = get_qc('Aspen-11-qvm') 
executable = qc.compile(p)
result = qc.run(executable)
bitstrings = result.readout_data.get('ro')
print(bitstrings)