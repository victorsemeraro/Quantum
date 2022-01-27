from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc

def throw_octahedral_die():
    # Return the result of throwing an 8 sided die

    p = Program()
    ro = p.declare('ro', 'BIT', 8)   

    for i in range(8):
        p += H(i)
        p += MEASURE(i, ro[i])

    qc = get_qc('Aspen-11-qvm') 
    executable = qc.compile(p)
    result = qc.run(executable)
    bitstrings = result.readout_data.get('ro')
    
    dice = 0
    for i in range(len(bitstrings)):
        for j in range(len(bitstrings[i])):
            dice += bitstrings[i][j]

    return dice

# Call Octahedral Function
print("Throwing Eight Sided Die: ", throw_octahedral_die())

def throw_polyhedral_die(num_sides):
    # Return the result of throwing a num_sides sided die

    p = Program()
    ro = p.declare('ro', 'BIT', num_sides)   

    for i in range(num_sides):
        p += H(i)
        p += MEASURE(i, ro[i])

    qc = get_qc('Aspen-11-qvm') 
    executable = qc.compile(p)
    result = qc.run(executable)
    bitstrings = result.readout_data.get('ro')
    
    dice = 0
    for i in range(len(bitstrings)):
        for j in range(len(bitstrings[i])):
            dice += bitstrings[i][j]

    return dice

# Call Polyhedral Function
print("Throwing Polyhedral Die: ", throw_polyhedral_die(16))