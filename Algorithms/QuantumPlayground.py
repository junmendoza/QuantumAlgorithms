
import argparse

from QiskitUtils            import setupQiskit
from DeutschAlgorithm       import deutschAlgorithm
from DeutschJozsa           import deutschJozsa
from GroversSearch          import groversSearch
from DeutschJozsaQiskit     import deutschJozsaQiskit
from GroversSearchQiskit    import groversSearchQiskit

def main():

    parser = argparse.ArgumentParser(description='Run quantum algorithms')
    parser.add_argument(
        '--token',
        dest='token',
        default='token not set',
        help='Specify token from IBM account'
        )
    parser.add_argument(
        '--algorithm',
        dest='algorithm',
        default='all',
        choices=['all', 'deutsch', 'deutsch-jozsa', 'grovers', 'deutsch-jozsa-qiskit', 'grovers-qiskit'],
        help='Specify algorithm to run'
        )
    parser.add_argument(
        '--dj-oracle-type',
        dest='dj_oracle_type',
        default='constant',
        choices=['constant', 'balanced'],
        help='Specify deutsch-jozsa oracle type'
        )
    parser.add_argument(
        '--dj-input-qubits',
        dest='dj_input_qubits',
        default=1,
        type=int,
        help='Specify deutsch-jozsa number of input qubits'
        )
    args = parser.parse_args()

    token = str(args.token)
    algorithm = args.algorithm

    setupQiskit(token)

    if algorithm == 'all' or algorithm == 'deutsch' :
        deutschAlgorithm()

    if algorithm == 'all' or algorithm == 'deutsch-jozsa' :
        deutschJozsa()

    if algorithm == 'all' or algorithm == 'grovers' :
        groversSearch()

    if algorithm == 'all' or algorithm == 'deutsch-jozsa-qiskit' :
        deutschJozsaQiskit(
            args.dj_oracle_type,
            args.dj_input_qubits
            )

    if algorithm == 'all' or algorithm == 'grovers-qiskit' :
        groversSearchQiskit()

if __name__ == "__main__" :
    main();

