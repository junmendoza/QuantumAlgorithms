
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
        default='',
        help='Specify token from IBM account'
        )
    parser.add_argument(
        '--algorithm',
        dest='algorithm',
        default='all',
        choices=['all', 'deutsch', 'dj', 'grovers', 'dj-qiskit', 'grovers-qiskit'],
        help='Specify algorithm to run'
        )

    # Deutch Jozsa args
    parser.add_argument(
        '--dj-oracle-type',
        dest='dj_oracle_type',
        default='constant',
        choices=['constant', 'balanced'],
        help='Specify dj oracle type'
        )
    parser.add_argument(
        '--dj-input-qubits',
        dest='dj_input_qubits',
        default=1,
        type=int,
        help='Specify dj number of input qubits'
        )

    # Grovers Search args
    parser.add_argument(
        '--grovers-oracle-type',
        dest='grovers_oracle_type',
        default='default',
        choices=['default'],
        help='Specify grovers search oracle type'
        )
    parser.add_argument(
        '--grovers-input-qubits',
        dest='grovers_input_qubits',
        default=1,
        type=int,
        help='Specify grovers search input qubits'
        )
    args = parser.parse_args()

    token = str(args.token)
    algorithm = args.algorithm

    setupQiskit(token)

    if algorithm == 'all' or algorithm == 'deutsch' :
        deutschAlgorithm()

    if algorithm == 'all' or algorithm == 'dj' :
        deutschJozsa(
            args.dj_oracle_type,
            args.dj_input_qubits
            )

    if algorithm == 'all' or algorithm == 'grovers' :
        groversSearch(
            args.grovers_oracle_type,
            args.grovers_input_qubits
            )

    if algorithm == 'all' or algorithm == 'dj-qiskit' :
        deutschJozsaQiskit(
            args.dj_oracle_type,
            args.dj_input_qubits
            )

    if algorithm == 'all' or algorithm == 'grovers-qiskit' :
        groversSearchQiskit(
            args.grovers_oracle_type,
            args.grovers_input_qubits
            )

if __name__ == "__main__" :
    main();

