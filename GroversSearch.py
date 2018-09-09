
# Grovers search algorithm
# The implementation attempts to closely match the mathematical expressions for every quantum state
import numpy as np

# Oracle function
def f(x) :
    if x == 3 :
        return 1
    return 0

# Constants
hadamard_amplitude = 1 / np.sqrt(2)

# Hadamard matrix
H = hadamard_amplitude * np.matrix('1  1 ; 1 -1')
print(H)

# Input qubits
n = 3
# Possible combinations
N = np.power(2, n)

# H Tensor n product
HTn = H
for i in range(n - 1) :
    HTn = np.kron(HTn, H)
HTn = HTn.round(4)
print(HTn)

# Diffusion operator
DIFF = np.full((N, N), 2/N) - np.identity(N, N)

d = np.sqrt(N)
amplitude = 1 / d

# Iterations
steps = int(d)

# Quantum state init
n = 0
qstate = np.full((1, N), amplitude)

for i in range(steps):

    # Phase Inversion of the amplitudes
    # Iterate through all states and call the oracle function
    for x in range(N):
        # (-1)**f(x)|x>
        qstate[0][x] = qstate[0][x] * (-1)**f(x)
    qstate = qstate.round(4)
    print(qstate)

    # Diffusion transform
    qstate = np.matmul(qstate, DIFF)
    qstate = qstate.round(4)
    print(qstate)