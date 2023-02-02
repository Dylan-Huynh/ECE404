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
        remainder - bitRemainder(num, mod)
        num, mod = mod, bitRemainder(num, mod) #changes to next step i.e. 35, 19 goes to 19, 16
        tempx = x
        while (tempx > 0):
            if (~tempx & 1):
                q << 1
            tempx >> x
        x, x_old = x_old - q, x #linearization, 
        
        q = num
        tempy = y
        while (tempy > 0):
            if (~tempy & 1):
                q << 1
            tempy >> 1
        y, y_old = y_old - q, y
    if num != 1:
        print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, MOD, num))
    else:
        MI = (x_old + MOD) % MOD
        print("\nMI of %d modulo %d is: %d\n" % (NUM, MOD, MI))

MI(NUM, MOD)

def bitDivide(a, b):

def bitMultiply(a, b):

def bitRemainder(a,b):
    

a, b = int(sys.argv[1]), int(sys.argv[2])
def bmi(a,b, x, y):
    print(a,b)
    if a == b: return a #(A)
    if a == 0: return b #(B)
    if b == 0: return a #(C)
    if (~a & 1):
        if (b & 1): #(E)
            print("inner a>b")
            bmi(a >> 1, b, x, y) #(F)
        else: #(G)
            print("innerelse")
            bmi(a >> 1, b >> 1, x, y) << 1 #(H)
    if (~b & 1): #(I)
        print("~b&1")
        bmi(a, b >> 1, x, y) #(J)
    if (a > b): #(K)
        print("a>b")
        bmi((a-b) >> 1, b, x, y) #(L)
    print("else")
    ((b-a) >> 1, a, x, y) #(M)
bmi(a, b, 0, 1)
