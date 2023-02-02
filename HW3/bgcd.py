#!/usr/bin/env python
## BGCD.py
import sys
from BitVector import *

if len(sys.argv) != 3:
    sys.exit("\nUsage: %s <integer> <integer>\n" % sys.argv[0])
a,b = int(sys.argv[1]),int(sys.argv[2])
def bgcd(a,b):
    abv = BitVector(intVal=a) 
    bbv = BitVector(intVal=b)
    print(a,b)
    print(abv, bbv)
    if a == b: 
        print("a==b")
        return a #(A)
    if a == 0: 
        print("a=0")
        return b #(B)
    if b == 0: 
        print("b=0")
        return a #(C)
    if (~a & 1): #(D)
        if (b &1): #(E)
            print("inner ~b&1")
            return bgcd(a >> 1, b) #(F)
        else: #(G)
            print("inner else")
            return bgcd(a >> 1, b >> 1) << 1 #(H)
    if (~b & 1): #(I)
        print(~b)
        this = ~b
        print(str(int(~bbv)))
        print("~b&1")
        return bgcd(a, b >> 1) #(J)
    if (a > b): #(K)
        print("a>b")
        return bgcd( (a-b) >> 1, b) #(L)
    print("else")
    return bgcd( (b-a) >> 1, a ) #(M)
gcdval = bgcd(a, b)
print("\nBGCD: %d\n" % gcdval)