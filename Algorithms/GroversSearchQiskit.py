#
# Grovers Search Algorithm
# Implemented in Qiskit
#

def groversSearchQiskit(oracle_type, input_qubits) :
    print("Running: groversSearchQiskit")
    
    # psi0: Init input qubits |001>
    #==============================
    print("psi0: Setting up input qubits")
    
    # psi1: Place all qubits in superposition
    #========================================
    print("psi1: Apply hadamard gates")
    
    # psi2: Apply the oracle function to the superposition of input qubits
    #=====================================================================
    print("psi2: Apply oracle function")

    # psi3: Prepare for measurement
    #==============================
    print("psi3: Apply hadamard gates")

    # Final measurement
    #==================
    print("Final measurement")
    

