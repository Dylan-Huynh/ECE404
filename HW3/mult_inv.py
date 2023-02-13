import sys
from BitVector import *

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <integer> <modulus>\n" % sys.argv[0])
    sys.exit(1)

def bitMultiplyRecurse(a, b, product):
    if (b <= 0):
        return product
    if(b & 1 == 1):
        product = product + a
    return bitMultiplyRecurse(a << 1, b >> 1, product)
    

def bitMultiply(a, b):
    negcheck = 0
    product = 0
    realA = abs(a)
    realB = abs(b)
    if a > 0 and b < 0 or a < 0 and b > 0:
        negcheck = 1
    product = bitMultiplyRecurse(realA, realB, product)
    if(negcheck):
        return (-1 * product)
    return product    



def bitRemainder(a,b):
    
    remainder,final = 0,0
    for i in range(255, -1, -1):
        if (remainder +(b << i) <= a):

            remainder = remainder + b << i
            final = final + 1 << i
            
    return final



NUM, MOD = int(sys.argv[1]), int(sys.argv[2])
def MI(num, mod):
    NUM = num; MOD = mod
    x, x_old = 0, 1
    y, y_old = 1, 0
    while mod:
        q = bitRemainder(num, mod)
        num, mod = mod, num % mod
        x, x_old = x_old - bitMultiply(q, x), x
        y, y_old = y_old - bitMultiply(q, y), y
    if num != 1:
        print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, MOD, num))
    else:
        MI = (x_old + MOD) % MOD
        print("\nMI of %d modulo %d is: %d\n" % (NUM, MOD, MI))
MI(NUM, MOD)