#!/usr/bin/env python

import sys
import BitVector

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
    sys.exit(1)

NUM, MOD = int(sys.argv[1]), int(sys.argv[2])
def MI(num, mod):
    '''
    This function uses ordinary integer arithmetic implementation of the
    Extended Euclid’s Algorithm to find the MI of the first-arg integer
    vis-a-vis the second-arg integer.
    '''

    NUM = BitVector(intVal = num); MOD = BitVector(intVal = mod)
    x, x_old = 0, 1
    y, y_old = 1, 0
    while mod:
        q = num # mod
        NUM, MOD = MOD, NUM % mod #changes to next step i.e. 35, 19 goes to 19, 16
        x, x_old = x_old - q * x, x #linearization, 
        y, y_old = y_old - q * y, y
    if num != 1:
        print("\nNO MI. However, the GCD of %d and %d is %u\n" % (num, mod, int(NUM)))
    else:
        MI = (x_old + mod) % mod
        print("\nMI of %d modulo %d is: %d\n" % (num, mod, MI))

MI(NUM, MOD)

def bmi(a,b, x, y):
    if a == b: print("\nNO MI. However, the GCD is %d\n" % (b)) #(A)
    if a == 0: print("\nNO MI. However, the GCD is %d\n" % (b)) #(B)
    if b == 0: print("\nNO MI. However, the GCD is %d\n" % (a)) #(C)
    if (~a & 1):
        if (b &1): #(E)
            bmi(a >> 1, b) #(F)
        else: #(G)
            bmi(a >> 1, b >> 1) << 1 #(H)
    if (~b & 1): #(I)
        bmi(a, b >> 1) #(J)
    if (a > b): #(K)
        bmi( (a-b) >> 1, b) #(L)
    ( (b-a) >> 1, a ) #(M)
bmi(a, b, 0, 1)