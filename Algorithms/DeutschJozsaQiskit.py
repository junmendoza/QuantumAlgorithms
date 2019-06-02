#
# Deutsch Jozsa Algorithm
# Implemented in Qiskit
#

# useful additional packages
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def deutschJozsaQiskit() :
    print("Running: deutschJozsaQiskit")

    # psi0: Init input qubits |001>
    #==============================
    print("psi0: Setting up input qubits")

    # Num input qubits
    n = 2
    # Oracle qubits
    m = 1
    nqubits = n + m + 1
    
    # Oracle qubit index
    q = n
    
    # Output qubit index
    k = nqubits - 1

    # Create the input + oracle qubits + 1 output qubit registers
    qregs = QuantumRegister(nqubits)

    # Create the bits that will store the final measurement
    regs = ClassicalRegister(n)

    # Create the quantum cirquit that contains the input qubits and measurement bits
    qcircuit = QuantumCircuit(qregs, regs)

    # Set the last qubit to be the |1>
    # This creates an initial state of |001>
    qcircuit.x(qregs[k])
    
    # Setup oracle function to always return 1
    # Constant 1 oracle function
    qcircuit.x(qregs[q])

    # psi1: Place all qubits in superposition
    #========================================
    print("psi1: Apply hadamard gates")

    # Apply hadamard to in an out qubits
    # This creates the state |+>|+>|->
    for i in range(nqubits):
        if i != q :
            qcircuit.h(qregs[i])


    # psi2: Apply the oracle function to the superposition of input qubits
    #=====================================================================
    print("psi2: Apply oracle function")

    # Start of oracle function
    qcircuit.barrier()
    
    # Apply constant 1 oracle function
    qcircuit.cx(qregs[q], qregs[k])

    # End of oracle function
    qcircuit.barrier()

    # psi3: Prepare for measurement
    #==============================
    print("psi3: Apply hadamard gates")

    # Apply hadamard to in qubits
    # Apply hadamard to out qubit
    for i in range(nqubits):
        if i != q :
            qcircuit.h(qregs[i])

    # Final measurement
    #==================
    print("Final measurement")
    
    # Start of measurement
    qcircuit.barrier()
    for i in range(n):
        qcircuit.measure(qregs[i], regs[i])

    print(regs)