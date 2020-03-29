#!/usr/bin/python
'''This program simply prints the first 100
    Prime numbers in a csv file
    
    Extended Description.
        This Python file sends 100 to the primemodule
        and then puts that output into a variable that
        is then put into a csv file.    
'''

__author__= "Tamikal Johnson"
__license__=""
__version__=""
__email__="tamijohnson@valdosta.edu"
__status__="DONE"

from primepackage import *


def main():
    '''This drives the program and uses other defined
        functions in other python files
        
        There are no arguments being sent to this function.
        it sends and integer and a filename to another function.
        
        Returns:
            A csv file that will be in the same file as this python file.
         Exceptions:
             When anything goes wrong a message will display.
    '''
    try:
        primes = primemodule.getNPrime(100)
        primeio.write_primes(primes, 'output.csv')
    except:
        print("Something went wrong")
    finally:
        l = primeio.read_primes('output.csv')
        print(l)

if __name__ == '__main__':
    main()
