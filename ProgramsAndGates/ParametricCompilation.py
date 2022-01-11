import numpy as np

from pyquil import Program
from pyquil.gates import RX, RZ, MEASURE

qubit = 0

p = Program()
ro = p.declare("ro", "BIT", 1)
theta_ref = p.declare("theta", "REAL")

p += RX(np.pi / 2, qubit)
p += RZ(theta_ref, qubit)
p += RX(-np.pi / 2, qubit)

p += MEASURE(qubit, ro[0])

from pyquil import get_qc

qc = get_qc("1q-qvm")
executable = qc.compile(p)

parametric_measurements = []
for theta in np.linspace(0, 2 * np.pi, 200):
    executable.write_memory(region_name='theta', value=theta)
    bitstrings = qc.run(executable).readout_data.get("ro")
    parametric_measurements.append(bitstrings)

print(bitstrings)