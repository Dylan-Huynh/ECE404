#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
    sys.exit(1)

NUM, MOD = int(sys.argv[1]), int(sys.argv[2])
def MI(num, mod):
    NUM, MOD = num, mod
    x, x_old = 0, 1
    y, y_old = 1, 0
    while mod:
        q = num # mod
        remainder = bitRemainder(num, mod)
        num, mod = mod, bitRemainder(num, mod) #changes to next step i.e. 35, 19 goes to 19, 16
        new_x = bitMultiply(q, x)
        new_y = bitMultiply(q, y)
        x, x_old = x_old - new_x, x #linearization, 
        y, y_old = y_old - new_y, y
    if num != 1:
        print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, MOD, num))
    else:
        MI = (x_old + MOD) % MOD
        print("\nMI of %d modulo %d is: %d\n" % (NUM, MOD, MI))

MI(NUM, MOD)

def bitMultiply(a, b):
    if (b == 0):
        return a
    if (~b & 1):
        return bitMultiply(a, b >> 1)
    else:
        return bitMultiply(a << 1, b >> 1)

def bitRemainder(a,b):
    if a == b: return a #(A)
    if a == 0: return b #(B)
    if b == 0: return a #(C)
    if (~a & 1):
        if (b &1): #(E)
            return bitRemainder(a >> 1, b) #(F)
        else: #(G)
            return bitRemainder(a >> 1, b >> 1) << 1 #(H)
    if (~b & 1): #(I)
        return bitRemainder(a, b >> 1) #(J)
    if (a > b): #(K)
        return b