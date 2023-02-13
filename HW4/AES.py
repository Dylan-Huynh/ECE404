import sys
from BitVector import *

AES_modulus = BitVector(bitstring='100011011')
subBytesTable = []                                                  # for encryption
invSubBytesTable = []  

def generate_tables():
    c = BitVector(bitstring='01100011')
    d = BitVector(bitstring='00000101')
    for i in range(0, 256):
        # For the encryption SBox
        a = BitVector(intVal = i, size=8).gf_MI(AES_modulus, 8) if i != 0 else BitVector(intVal=0)
        # For bit scrambling for the encryption SBox entries:
        a1,a2,a3,a4 = [a.deep_copy() for x in range(4)]
        a ^= (a1 >> 4) ^ (a2 >> 5) ^ (a3 >> 6) ^ (a4 >> 7) ^ c
        subBytesTable.append(int(a))
        # For the decryption Sbox:
        b = BitVector(intVal = i, size=8)
        # For bit scrambling for the decryption SBox entries:
        b1,b2,b3 = [b.deep_copy() for x in range(3)]
        b = (b1 >> 2) ^ (b2 >> 5) ^ (b3 >> 7) ^ d
        check = b.gf_MI(AES_modulus, 8)
        b = check if isinstance(check, BitVector) else 0
        invSubBytesTable.append(int(b))

def sub_bytes(state_array):
    for i in range(4):
        for j in range(4):
            state_array[i][j] = subBytesTable[state_array[i][j]]

def shift_rows(state_array):
    new_state_array = state_array.copy()
    for i in range(4):
        for j in range(4):
            k = i
            if k + j > 3:
                k = k - 4
            new_state_array[i][j] = subBytesTable[state_array[i][k + j]]
                

def mix_columns(state_array):
    new_state_array = state_array.copy()
    for i in range(4):
        for j in range(4):
            if (i == 0):
                new_state_array = subBytesTable[state_array[0][j]] * 2 ^ subBytesTable[state_array[1][j]] * 3 ^...
                subBytesTable[state_array[2][j]] ^ subBytesTable[state_array[3][j]] 
            elif (i == 1):
                new_state_array = subBytesTable[state_array[1][j]] * 2 ^ subBytesTable[state_array[2][j]] * 3 ^...
                subBytesTable[state_array[3][j]] ^ subBytesTable[state_array[0][j]] 
            elif (i == 2):
                new_state_array = subBytesTable[state_array[0][j]] * 2 ^ subBytesTable[state_array[1][j]] * 3 ^...
                subBytesTable[state_array[2][j]] ^ subBytesTable[state_array[3][j]] 
            elif (i == 3):
                new_state_array = subBytesTable[state_array[0][j]] * 2 ^ subBytesTable[state_array[1][j]] * 3 ^...
                subBytesTable[state_array[2][j]] ^ subBytesTable[state_array[3][j]] 
            


def encrypt(plaintext, key, ciphertext):
    outfile = open(ciphertext, "w")
    bv = BitVector(filename = plaintext)
    generate_tables()
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        statearray = [[0 for x in range(4)] for x in range(4)]
        for i in range(4):
            for j in range(4):
                statearray[j][i] = bitvec[32*i + 8*j:32*i + 8*(j+1)]


def decrypt(ciphertext, key, plaintext):
    outfile = open(plaintext, "w")
    ctext = BitVector(filename = ciphertext)
    statearray = [[0 for x in range(4)] for x in range(4)]






plaintext = sys.arg[2]
key = sys.arg[3]
ciphertext = sys.arg[4]
if sys.arg[1] is "-e":
    encrypt(plaintext, key, ciphertext)
if sys.arg[1] is "-d":
    decrypt(plaintext, key, ciphertext)