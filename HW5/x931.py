#Homework Number: 5
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/21/2023

import sys
from BitVector import *
from AES import encrypt

def x931(v0, dt, totalNum, key_file):
    '''
    * Arguments:
      v0:      128-bit BitVector object containing the seed value
      dt:      128-bit BitVector object symbolizing the date and time
      totalNum: The total number of random numbers to generate
      key_file: Filename for text file containing the ASCII encryption key for AES
    * Function Description:
      This function uses the arguments with the X9.31 algorithm to generate totalNum
         random numbers as BitVector objects.
      Returns a list of BitVector objects, with each BitVector object representing a
         random number generated from X9.31.
    '''
    AES_dt = encrypt(dt, key_file)
    R = []
    v = [v0]
    for i in range(totalNum):
        vj = v[i]
        XOR_vj_dt = vj ^ AES_dt
        R.append(encrypt(XOR_vj_dt, key_file))
        XOR_Rj_dt = R[-1] ^ AES_dt
        v.append(encrypt(XOR_Rj_dt, key_file))
    return R



