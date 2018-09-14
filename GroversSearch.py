#
# Grovers search algorithm
#   + Model the quantum states of Grovers search algorithm
#   + Support n input qubits
#   + The output qubit is not modelled as its effect is handled in the phase inversion
#
import numpy as np
from Definitions import H

# Oracle function
def f(x) :
    if x == 2 :
        return 1
    return 0

# Compute precision in decimal places
precision = 4

# Input qubits
n = 3

# Possible combinations
N = np.power(2, n)

# Diffusion operator
DIFF = np.full((N, N), 2/N) - np.identity(N, N)
print("Diffusion operator = \n{0}".format(HTn))

# H Tensor n product
HTn = H
for i in range(n - 1) :
    HTn = np.kron(HTn, H)
HTn = HTn.round(precision)
print("H tensor {0} = \n{1}".format(n, HTn))

# Initial amplitude of all states
d = np.sqrt(N)
amplitude = 1 / d

# Iterations
steps = int(d)

# Quantum state index
qs = 0

# qstate1: Init input qubits |0...0>
qubit = [1, 0] # 1 qubit at state |0>
qstate = qubit
for i in range(n - 1):
    qstate = np.kron(qstate, [1, 0])
print("|qs{0}> = {1}".format(qs, qstate))
qs+=1

# qstate2: Apply hadamard to all input qubits
qstate = np.matmul(qstate, HTn)
print("|qs{0}> = {1}".format(qs, qstate))
qs+=1

# Begin iteration
for i in range(steps):
    # Phase Inversion of the amplitudes
    # Iterate through all states and call the oracle function
    for x in range(N):
        # (-1)**f(x)|x>
        qstate[x] = qstate[x] * (-1)**f(x)
    qstate = qstate.round(precision)
    print("|qs{0}> = {1}".format(qs, qstate))
    qs+=1

    # Diffusion transform
    qstate = np.matmul(qstate, DIFF)
    qstate = qstate.round(precision)
    print("|qs{0}> = {1}".format(qs, qstate))
    qs+=1

# Final measurement
amplitude_sum = np.matmul(qstate, qstate)
print("Amplitude Sum = <qs{0}|qs{1}> = {2}".format(qs, qs, amplitude_sum))