#Homework Number: 6
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/28/2023

import sys
from BitVector import *
import PrimeGenerator

def prime_generate(p, q):
    pout = open(p, "w")
    qout = open(q, "w")


def encrypt(message, p, q, encrypted):
    encryptout = open(encrypted, "w")

def decrypt(encrypted, p, q, decrypted):
    decryptout = open(decrypted, "w")

if __name__ == "__main__":
    if len(sys.argv) != 4 | len(sys.argv) != 6:
        sys.exit('''Needs 4 or 6 command line arguments, one for '''
            '''the encryption or decrtpyion, one for the input text'''
            '''one for the key, and one for the output text''')
    if sys.argv[1] == "-g":
        prime_generate(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-e":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[6])
    elif sys.argv[1] == "-d"
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[4])
    else:
        sys.exit('''argument one is not of form "-g", "-e" or "-d"''')