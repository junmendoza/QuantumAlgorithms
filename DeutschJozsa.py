#
# Deutsch Jozsa Algorithm
#
# The Deutsch Jozsa algorithm is a generalisation of the Deutsch’s algorithm.
# The goal is still to determine if a function is balanced or constant.
# The difference is that there can be more than 1 input to the oracle function.
# Note that the inputs to the function is guaranteed to be constant or balanced.
#
# + Model the quantum states of the Detusch Jozsa algorithm
# + Support n input qubits
# + The output qubit is not modelled as its effect is handled in the phase inversion
#

import numpy as np
from Definitions import H

# Oracle function
def f(x, max) :
    type = 2
    if type == 0:
        # Constant 0
        return 0
    elif type == 1:
        # Constant 1
        return 1

    # Balanced
    n = max / 2
    if x < n:
        return 0
    return 1

# Compute precision in decimal places
precision = 4

# Input qubits
n = 2

# Possible combinations
N = np.power(2, n)

# H Tensor n product
HTn = H
for i in range(n - 1) :
    HTn = np.kron(HTn, H)
HTn = HTn.round(precision)
print("H tensor {0} = \n{1}".format(n, HTn))

# Initial amplitude of all states
d = np.sqrt(N)
amplitude = 1 / d

# Quantum state index
qs = 0

# qstate1: Init input qubits |0...0>
qubit = [1, 0] # 1 qubit at state |0>
qstate = qubit
for i in range(n - 1):
    qstate = np.kron(qstate, [1, 0])
qstate = qstate.round(precision)
print("|qs{0}> = {1}".format(qs, qstate))
qs+=1

# qstate2: Apply hadamard to all input qubits
qstate = np.matmul(qstate, HTn)
qstate = qstate.round(precision)
print("|qs{0}> = {1}".format(qs, qstate))
qs+=1

# qstate3: Phase Inversion
# Apply the oracle function to x superposition of states
for x in range(N):
    # (-1)**f(x)|x>
    qstate[x] = qstate[x] * (-1)**f(x, N)
qstate = qstate.round(precision)
print("|qs{0}> = {1}".format(qs, qstate))
qs+=1

# qstate4: Final measurement
# Multiply the input qubits in vector form by the tensor product matrix
qstate = np.matmul(qstate, HTn)
qstate = qstate.round(precision)
print("|qs{0}> = {1}".format(qs, qstate))

# The function is constant if all qubits are measured to be 0 regardless of +/- phase
# The function is balanced if half of the qubits 0 and the other half are 1 regardless of +/- phase

