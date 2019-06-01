#
# Deutsch's Algorithm
#
# The goal is  to determine if a function is balanced or constant.
# Note that the inputs to the function is guaranteed to be constant or balanced.
#
# + Model the quantum states of the Detusch  algorithm
# + 1 input qubit and 1 output qubit
#

import numpy as np
from Definitions import H

# Oracle function
def f(x) :
    type = 1
    if type == 0:
        # Constant 0
        return 0
    elif type == 1:
        # Constant 1
        return 1
    else:
        # Balanced
        # Return the not of the argument
        return ~x

def deutschAlgorithm() :
    print("Running: deutschAlgorithm")
    
    # Compute precision in decimal places
    precision = 4
    
    # Input qubits
    n = 1
    
    # Possible combinations
    N = np.power(2, n)
    
    # H Tensor n product
    # The numpy kronocker product is the tensor product
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
    
    # psi0: Init input qubits |0...0>
    qubit = [1, 0] # 1 qubit at state |0>
    qstate = qubit
    print("psi{0} = {1}".format(qs, qstate))
    qs+=1
    
    # qstate2: Apply hadamard to all input qubits
    qstate = np.matmul(qstate, HTn)
    qstate = qstate.round(precision)
    print("psi{0} = {1}".format(qs, qstate))
    qs+=1
    
    # qstate3: Phase Inversion
    # Apply the oracle function to x superposition of states
    for x in range(N):
        # (-1)**f(x)|x>
        qstate[x] = qstate[x] * (-1)**f(x)
    qstate = qstate.round(precision)
    print("psi{0} = {1}".format(qs, qstate))
    qs+=1
    
    # qstate4: Final measurement
    # Multiply the input qubits in vector form by the tensor product matrix
    qstate = np.matmul(qstate, HTn)
    qstate = qstate.round(precision)
    print("psi{0} = {1}".format(qs, qstate))
    
    # The function is constant if all qubits are measured to be 0 regardless of +/- phase
    # The function is balanced if half of the qubits 0 and the other half are 1 regardless of +/- phase

