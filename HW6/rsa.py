#Homework Number: 6
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/28/2023

import sys
from BitVector import *
from PrimeGenerator import *

def bgcd(a,b):
    if a == b: 
        return a
    if a == 0: 
        return b
    if b == 0: 
        return a
    if (~a & 1):
        if (b &1):
            return bgcd(a >> 1, b)
        else:
            return bgcd(a >> 1, b >> 1) << 1
    if (~b & 1):
        this = ~b
        return bgcd(a, b >> 1)
    if (a > b):
        return bgcd( (a-b) >> 1, b)
    return bgcd( (b-a) >> 1, a )

def MI(num, mod):
    '''
    This function uses ordinary integer arithmetic implementation of the
    Extended Euclid's Algorithm to find the MI of the first-arg integer
    vis-a-vis the second-arg integer.
    '''
    NUM = num; MOD = mod
    x, x_old = 0, 1
    y, y_old = 1, 0
    while mod:
        q = num // mod
        num, mod = mod, num % mod
        x, x_old = x_old - q * x, x
        y, y_old = y_old - q * y, y
    if num != 1:
        print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, MOD, num))
        return 0
    else:
        MI = (x_old + MOD) % MOD
        return MI
    

def prime_generate(p, q):
    pout = open(p, "w")
    qout = open(q, "w")
    generator = PrimeGenerator( bits = 128 ) 
    
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
    p = int(pfile.readline())
    q = int(qfile.readline())
    n = p * q
    e = 65537
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        while (bitvec._getsize() % 128 != 0):
            bitvec.pad_from_right(1)
        bitvec.pad_from_left(128)
        final = pow(bitvec.int_val(), e, n)
        final_bv = BitVector(intVal = final, size = 256)
        encryptout.write(final_bv.get_bitvector_in_hex())



def decrypt(encrypted, ptext, qtext, decrypted):
    decryptout = open(decrypted, "w")
    encryptedf = open(encrypted, "r")
    text = encryptedf.read()
    blocks = int( len(text) / 64)
    e = 65537
    pfile = open(ptext, "r")
    qfile = open(qtext, "r")
    p = int(pfile.readline())
    q = int(qfile.readline())
    n = p * q
    totientN = (p-1) * (q-1)
    d = MI(e, totientN)
    for i in range(blocks):
        bitvec = BitVector(hexstring = text[i * 64 + 0: i * 64 + 64])
        if bitvec._getsize() > 0:
            C = bitvec.int_val()
            Vp = pow(C, d, p)
            Vq = pow(C, d, q)
            Xp = q * MI(q, p)
            Xq = p * MI(p, q)
            final = (Vp * Xp + Vq * Xq) % n
            final_bv = BitVector(intVal = final, size = 128)
            decryptout.write(final_bv.get_bitvector_in_ascii())


if __name__ == "__main__":
    if len(sys.argv) != 4 | len(sys.argv) != 6:
        sys.exit('''Needs 2 or 6 command line arguments, one for '''
            '''the encryption or decrtpyion, one for the input text'''
            '''one for the key, and one for the output text''')
    if sys.argv[1] == "-g":
        prime_generate(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-e":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == "-d":
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        sys.exit('''argument one is not of form "-g", "-e" or "-d"''')