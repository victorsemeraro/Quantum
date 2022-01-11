from pyquil import Program

p = Program()
ro = p.declare('ro', 'BIT', 16)
theta = p.declare('theta', 'REAL')

print(p)