import numpy as np
from pyquil import Program
from pyquil.quil import DefGate

sqrt_x = np.array([
    [0.5 + 0.5j, 0.5 - 0.5j], 
    [0.5 - 0.5j, 0.5 + 0.5j]
    ])

sqrt_x_definition = DefGate("SQRT-X", sqrt_x)
SQRT_X = sqrt_x_definition.get_constructor()

p = Program()
p += sqrt_x_definition
p += SQRT_X(0)
print(p)

x_gate_matrix = np.array(([0.0, 1.0], [1.0, 0.0]))
sqrt_x = np.array([
    [0.5 + 0.5j, 0.5 - 0.5j], 
    [0.5 - 0.5j, 0.5 + 0.5j]
    ])
x_sqrt_x = np.kron(x_gate_matrix, sqrt_x)

x_sqrt_x_definition = DefGate("X-SQRT-X", x_sqrt_x)
X_SQRT_X = x_sqrt_x_definition.get_constructor()

p = Program()
p += sqrt_x_definition
p += SQRT_X(0)
print(p)