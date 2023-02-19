import sys
from BitVector import *
from AES import encrypt


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
    bv = BitVector(filename = image_file)


    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        while (bitvec._getsize() % 128 != 0):
            bitvec.pad_from_right(1)
        XORer = encrypt(iv, key_file)
        OutBlock = XORer ^ bitvec
        OutBlock.write_to_file(outfile)
        iv.set_value(intVal = (iv.int_val() + 1))

        print(iv)
