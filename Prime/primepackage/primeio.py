'''These are two functions that will both write to a file
    and read from the file.

'''

__author__= "Tamikal Johnson"
__license__=""
__version__=""
__email__="tamijohnson@valdosta.edu"
__status__="DONE"

def write_primes(l, file_name):
    '''This function takes two inputs, a variable that holds a list and a file name.
        When the two arguments are accepted the are written into the accepted file.
    
        Args:
             Array (list):input
            File (file_name):input
        
        Returns:
            Doesn't return anything. It writes to the file.
        Exception:
            If anything goes wrong with the file then a message will display.
            Example:
                If the file doesn't exist or if the file name doesn't match.
    '''
    try:
        file = open(file_name,'w')
        #file.write(str(l))
    except:
        print("Something with wrong with the file")
    finally:
        file.write(str(l))
            

def read_primes(file_name):
    '''This function takes just the one input which is a file and simply
        reads from the file.
    
        Args:
            File(file_name):input
        Returns:
            Doesn't return anything. It reads from file.
        Exception:
            If anything goes wrong with the file then a message will display.
            Example:
               If the file doesn't exist or if the file name doesn't match.
    '''
    try:
        file = open(file_name)
    except:
        print("Something with wrong with the file")
    finally:
        line = file.readline()
        return line
