
import argparse

from QiskitUtils            import setupQiskit
from DeutschAlgorithm       import deutschAlgorithm
from DeutschJozsa           import deutschJozsa
from GroversSearch          import groversSearch
from DeutschAlgorithmQiskit import deutschAlgorithmQiskit
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
        default='0',
        choices=['0', '1', '2', '3', '4', '5', '6'],
        help=
            'Specify algorithm to run: '
            '0=run all, '
            '1=Deutschs Algorithm, '
            '2=Deutch Jozsa, '
            '3=Grovers Search, '
            '4=Deutschs Algorithm Qiskit, '
            '5=Deutch Jozsa Qiskit, '
            '6=Grovers Search Qiskit, '
        )
    args = parser.parse_args()
    
    token = str(args.token)
    algorithm = int(args.algorithm)
    
    setupQiskit(token)
    
    if algorithm == 0 or algorithm == 1 :
        deutschAlgorithm()
        
    if algorithm == 0 or algorithm == 2 :
        deutschJozsa()
        
    if algorithm == 0 or algorithm == 3 :
        groversSearch()
        
    if algorithm == 0 or algorithm == 4 :
        deutschAlgorithmQiskit()
        
    if algorithm == 0 or algorithm == 5 :
        deutschJozsaQiskit()
        
    if algorithm == 0 or algorithm == 6 :
        groversSearchQiskit()

if __name__ == "__main__" :
    main();

