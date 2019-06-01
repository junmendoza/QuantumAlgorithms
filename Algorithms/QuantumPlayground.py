
from QiskitUtils        import setupQiskit
from DeutschAlgorithm   import deutschExample
from DeutschJozsa       import deutschJozsaExample
from GroversSearch      import groversSearchExample 
    
def main():
    setupQiskit()
    deutschExample()
    deutschJozsaExample()
    groversSearchExample()

if __name__ == "__main__" :
    main();

