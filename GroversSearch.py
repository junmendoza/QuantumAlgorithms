
# Grovers search algorithm
# The implementation attempts to closely match the mathematical expressions for every quantum state
import math

# Input qubits
n = 3

# Possible combinations
N = 2 ^ n

# Iterations
steps = math.sqrt(N)

# Quantum state index
i = 0

# Initialise input qubits
qstate = [1, 2, 3, 4, 5, 6]
qstate[i] = 0
i += 1

for x in range(0, int(steps)):

    # Phase Inversion
    qstate[i] = 0
    i += 1

    # Diffusion transform
    qstate[i] = 0
    i += 1
