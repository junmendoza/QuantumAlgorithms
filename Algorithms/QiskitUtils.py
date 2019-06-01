

# Setting up the IBM Qiskit account
from qiskit import IBMQ

def setupQiskit(token) :
    mytoken = token
    qiskit_url = 'https://api.quantum-computing.ibm.com/api/Hubs/ibm-q/Groups/open/Projects/main'
    
    # If you want to store the account to disk
    IBMQ.save_account(mytoken, qiskit_url)
    
    # Alternatively, if you want to store only for the current session
    #IBMQ.enable_account(mytoken)
    
    # Once account is stored, you can load them for every session using
    IBMQ.load_accounts()
