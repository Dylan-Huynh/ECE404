import sys
from BitVector import *

def encrypt(plaintext, message, ciphertext):
    


plaintext = sys.arg[2]
message = sys.arg[3]
ciphertext = sys.arg[4]
if sys.arg[1] is "-e":
    encrypt(plaintext, message, ciphertext)