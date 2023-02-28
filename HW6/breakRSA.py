import sys
from BitVector import *
from PrimeGenerator import *
from solve_pRoot import *



def encrypt(message, enc1, enc2, enc3, keys):
    keysF = open(keys, "w")
    enc1out = open(enc1, "w")
    enc2out = open(enc2, "w")
    enc3out = open(enc3, "w")
    p, q = prime_generate()
    n1 = p * q
    keysF.write("%d\n" % (n1))
    #keysF.write("\n")
    p, q = prime_generate()
    n2 = p * q
    keysF.write("%d\n" % (n2))
    #keysF.write("\n")
    p, q = prime_generate()
    n3 = p * q
    keysF.write("%d" % (n3))
    bv = BitVector(filename = message)
    actualEncrypt(enc1out, n1, bv)
    bv = BitVector(filename = message)
    actualEncrypt(enc2out, n2, bv)
    bv = BitVector(filename = message)
    actualEncrypt(enc3out, n3, bv)
    #totientN = (p-1) * (q-1)
    e = 65537
    #d = MI(e, totientN)

def actualEncrypt(outfile, n, bv):
    e = 3
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        while (bitvec._getsize() % 128 != 0):
            bitvec.pad_from_right(1)
        bitvec.pad_from_left(128)
        final = pow(bitvec.int_val(), e, n)
        final_bv = BitVector(intVal = final, size = 256)
        outfile.write(final_bv.get_bitvector_in_hex())

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

def prime_generate():
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
    return p, q

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


def breakRSA(enc1, enc2, enc3, keys, cracked):
    crackedF = open(cracked, "w")
    keyF = open(keys, "r")
    n1 = int(keyF.readline())
    n2 = int(keyF.readline())
    n3 = int(keyF.readline())
    enc1f = open(enc1, "r")
    text1 = enc1f.read()
    blocks = int( len(text1) / 64)
    enc2f = open(enc2, "r")
    text2 = enc2f.read()
    enc3f = open(enc3, "r")
    text3 = enc3f.read()
    N = n1 * n2 * n3
    n = [n1, n2, n3]
    MList = [int(N/n1), int(N/n2), int(N/n3)]
    M1inv = MI(MList[0], n1)
    M2inv = MI(MList[1], n2)
    M3inv = MI(MList[2], n3)
    Minv = [M1inv, M2inv, M3inv]

    for i in range(blocks):
        bitvec1 = BitVector(hexstring = text1[i * 64 + 0: i * 64 + 64])
        bitvec2 = BitVector(hexstring = text2[i * 64 + 0: i * 64 + 64])
        bitvec3 = BitVector(hexstring = text3[i * 64 + 0: i * 64 + 64])
        M1CRT = []
        M2CRT = []
        M3CRT = []
        McubedCRT = []
        for i in n:
            M1CRT.append(bitvec1.int_val() % i)
            M2CRT.append(bitvec2.int_val() % i)
            M3CRT.append(bitvec3.int_val() % i)
            McubedCRT.append(M1CRT[-1] * M2CRT[-1] * M3CRT[-1])
        Mcubed = 0
        for i in range(3):
            Mcubed = (Mcubed + McubedCRT[i] * MList[i] * Minv[i])
        Mcubed = Mcubed % N
        M = solve_pRoot(3, Mcubed)
        Mbv = BitVector(intVal = M, size = 256)
        half_M = Mbv[128:256]
        crackedF.write(half_M.get_bitvector_in_ascii())
        #Do we Multiply them together because its a cube operation?



if __name__ == "__main__":
    if len(sys.argv) != 4 | len(sys.argv) != 6:
        sys.exit('''Needs 4 or 6 command line arguments, one for '''
            '''the encryption or decrtpyion, one for the input text'''
            '''one for the key, and one for the output text''')
    if sys.argv[1] == "-e":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif sys.argv[1] == "-c":
        breakRSA(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        sys.exit('''argument one is not of form "-c" or "-e"''')