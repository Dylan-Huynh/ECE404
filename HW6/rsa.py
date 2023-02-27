#Homework Number: 6
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/28/2023

import sys
from BitVector import *
from PrimeGenerator import *

def bgcd(a,b):
    abv = BitVector(intVal=a) 
    bbv = BitVector(intVal=b)
    if a == b: 
        return a #(A)
    if a == 0: 
        return b #(B)
    if b == 0: 
        return a #(C)
    if (~a & 1): #(D)
        if (b &1): #(E)
            return bgcd(a >> 1, b) #(F)
        else: #(G)
            return bgcd(a >> 1, b >> 1) << 1 #(H)
    if (~b & 1): #(I)
        this = ~b
        return bgcd(a, b >> 1) #(J)
    if (a > b): #(K)
        return bgcd( (a-b) >> 1, b) #(L)
    return bgcd( (b-a) >> 1, a ) #(M)

def prime_generate(p, q):
    pout = open(p, "w")
    qout = open(q, "w")
    generator = PrimeGenerator( bits = 128 ) 
    #generator = PrimeGenerator(bits = int(256))
    
    i = 0
    e = 65537
    while i == 0:
        i = 1
        p = generator.findPrime()
        q = generator.findPrime()
        pbv = BitVector(intVal = p)
        p0 = pbv[2]
        p1 = pbv[1]
        qbv = BitVector(intVal = q)
        q0 = qbv[0]
        q1 = qbv[1]
        if (p0 == 0 or p1 == 0 or q0 == 0 or q1 == 0 or p == q or
            bgcd(p-1, e) != 1 or bgcd(q-1, e)) != 1:
            i = 0
    pout.write('%d' % p)
    qout.write('%d' % q)



def encrypt(message, ptext, qtext, encrypted):
    encryptout = open(encrypted, "w")
    bv = BitVector(filename = message)
    pfile = open(ptext, "r")
    qfile = open(qtext, "r")
    p = pfile.readline()
    q = qfile.readline()
    n = p * q
    totientN = (p-1) * (q-1)
    e = 65537
    ebv = BitVector(intVal = e)
    d = ebv.multiplicative_inverse(totientN)
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        while (bitvec._getsize() % 128 != 0):
            bitvec.pad_from_right(1)
        bitvec.pad_from_left(128)
        



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
    elif sys.argv[1] == "-d":
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[4])
    else:
        sys.exit('''argument one is not of form "-g", "-e" or "-d"''')