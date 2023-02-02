#!/usr/bin/env python

import sys
from BitVector import *

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
    sys.exit(1)
'''
NUM, MOD = int(sys.argv[1]), int(sys.argv[2])
def MI(num, mod):

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
'''

def bmi(a,b, x, y):
    print(a,b)
    if a == b: 
        print("a==b")
        print(str(int(b))) #(A)
    if int(a) == 0: 
        print("a=0")
        print(str(int(b))) #(B)
    if int(b) == 0: 
        print("b=0")
        print(str(int(a))) #(C)
    if (~a):
        if (b): #(E)
            print("a>b")
            bmi(a >> 1, b, x, y) #(F)
        else: #(G)
            print("a>b")
            bmi(a >> 1, b >> 1, x, y) << 1 #(H)
    if (~b): #(I)
        print("~b&1")
        bmi(a, b >> 1, x, y) #(J)
    if (a > b): #(K)
        print("a>b")
        bmi((a-b) >> 1, b, x, y) #(L)
    print("else")
    ((b-a) >> 1, a, x, y) #(M)
a, b = BitVector(intVal = int(sys.argv[1])), BitVector(intVal = int(sys.argv[2]))
bmi(a, b, 0, 1)