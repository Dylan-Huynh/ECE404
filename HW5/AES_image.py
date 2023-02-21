#Homework Number: 5
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/21/2023

import sys
from BitVector import *
from AES import encrypt

AES_modulus = BitVector(bitstring='100011011')

def ctr_aes_image(iv, image_file='image.ppm', out_file='enc_image.ppm',
    key_file='keyCTR.txt'):
    '''
    * Arguments:
    iv: 128-bit initialization vector
    image_file: input .ppm image file name
    out_file: encrypted .ppm image file name
    key_file: Filename containing encryption key (in ASCII)
    * Function Description:
    This function encrypts image_file using CTR mode AES and writes the encryption
     to out_file. No return value is required.
    '''
    infile = open(image_file, "rb")
    outfile = open(out_file, "wb")
    magicNumber = infile.readline()
    dimension = infile.readline()
    color = infile.readline()
    outfile.write(magicNumber)
    outfile.write(dimension)
    outfile.write(color)
    #base_iv = iv.int_val()
    #bv = BitVector(filename = image_file)

    if(iv._getsize() != 128):
            print("wrong")
    while (1):
        bits = infile.read(16)
        if len(bits) == 0:
            break
        bitvec = BitVector(rawbytes = bits)
        #while (bitvec._getsize() % 128 != 0):
        #    bitvec.pad_from_right(1)
        XORer = encrypt(iv, key_file)
        OutBlock = XORer ^ bitvec
        OutBlock.write_to_file(outfile)
        iv = BitVector(intVal = (iv.int_val() + 1), size =128)
        if(iv._getsize() != 128):
            print(iv._getsize())