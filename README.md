# QuantumPlayground
Quantum Playground is an open source project containing textbook examples of quantum algorithms in python. 

The algorithms are implemented manually without quantum libraries in order to explore and learn their 
core mathematical properties, behaviour and intermingling with classical computational models. 

They are also implemented in Qiskit so we can experiment running on simulators and actual quantum hardware.

Prerequisites:
 * Install Python 3.6
 * Install Qiskit. Refer to: https://qiskit.org/
 

Example command:
  python Algorithms/QuantumPlayground.py --algorithm=deutsch-jozsa-qiskit --dj-oracle-type=balanced --dj-input-qubits=2

Where:
  Algorithm = Runs Qiskit version of the Deutsch-Jozsa algorithm
  Oracle function = balanced
  Input qubits = 2




