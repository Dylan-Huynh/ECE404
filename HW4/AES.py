#Homework Number: 4
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 2/14/2023

import sys
from BitVector import *

AES_modulus = BitVector(bitstring='100011011')
subBytesTable = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 
                202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 
                183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 
                4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 
                9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 
                83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 
                208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 
                81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 
                205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 
                96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 
                224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 
                231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 
                186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 
                112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 
                225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 
                140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
                                                                 # for encryption
invSubBytesTable = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251,
                    124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203,
                    84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78,
                    8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37,
                    114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146,
                    108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132,
                    144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6,
                    208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107,
                    58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115,
                    150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110,
                    71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27,
                    252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244,
                    31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95,
                    96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239,
                    160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97,
                    23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]  

def sub_bytes(state_array):
    for i in range(4):
        for j in range(4):
            xin = (state_array[i][j]).int_val()
            state_array[i][j] = BitVector(intVal = subBytesTable[xin], size = 8)
    return state_array

def shift_rows(state_array):
    new_state_array = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            k = i
            if k + j > 3:
                k = k - 4
            new_state_array[i][j] = state_array[i][k + j]
    return new_state_array

def mix_columns(state_array):
    new_state_array = [[0 for x in range(4)] for x in range(4)]
    two = BitVector(bitstring = "10")
    three = BitVector(bitstring = "11")
    for i in range(4):
        for j in range(4):
            if (i == 0):
                new_state_array[i][j] = (state_array[0][j].gf_multiply_modular(two, AES_modulus, 8) ^ 
                state_array[1][j].gf_multiply_modular(three, AES_modulus, 8) ^state_array[2][j] ^ state_array[3][j])
            elif (i == 1):
                new_state_array[i][j] = (state_array[1][j].gf_multiply_modular(two, AES_modulus, 8) ^ 
                state_array[2][j].gf_multiply_modular(three, AES_modulus, 8) ^state_array[3][j] ^ state_array[0][j])
            elif (i == 2):
                new_state_array[i][j] = (state_array[2][j].gf_multiply_modular(two, AES_modulus, 8) ^ 
                state_array[3][j].gf_multiply_modular(three, AES_modulus, 8) ^state_array[0][j] ^ state_array[1][j])
            elif (i == 3):
                new_state_array[i][j] = (state_array[3][j].gf_multiply_modular(two, AES_modulus, 8) ^ 
                state_array[0][j].gf_multiply_modular(three, AES_modulus, 8) ^state_array[1][j] ^ state_array[2][j])
    return new_state_array


def xor_round_keys(state_array, key_words, round):
    new_state_array = state_array.copy()
    for i in range(4):
        for j in range(4):
            new_state_array[j][i] = state_array[j][i] ^ key_words[round * 4 + i][j*8:j*8+8]
    return new_state_array


def inverse_sub_bytes(state_array):
    for i in range(4):
        for j in range(4):
            xin = (state_array[i][j]).int_val()
            state_array[i][j] = BitVector(intVal = invSubBytesTable[xin], size = 8)
    return state_array

def inverse_shift_rows(state_array):
    new_state_array = [[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            k = -i
            if j + k < 0:
                k = k + 4
            new_state_array[i][j] = state_array[i][j + k]
    return new_state_array

def inverse_mix_columns(state_array):
    new_state_array = [[0 for x in range(4)] for x in range(4)]
    E = BitVector(bitstring = "00001110")
    B = BitVector(bitstring = "00001011")
    D = BitVector(bitstring = "00001101")
    nine = BitVector(bitstring = "00001001")
    
    for i in range(4):
        for j in range(4):
            if (i == 0):
                new_state_array[i][j] = (state_array[0][j].gf_multiply_modular(E, AES_modulus, 8) ^ 
                state_array[1][j].gf_multiply_modular(B, AES_modulus, 8) ^ 
                state_array[2][j].gf_multiply_modular(D, AES_modulus, 8) ^ 
                state_array[3][j].gf_multiply_modular(nine, AES_modulus, 8))
            elif (i == 1):
                new_state_array[i][j] = (state_array[1][j].gf_multiply_modular(E, AES_modulus, 8) ^ 
                state_array[2][j].gf_multiply_modular(B, AES_modulus, 8) ^
                state_array[3][j].gf_multiply_modular(D, AES_modulus, 8) ^ 
                state_array[0][j].gf_multiply_modular(nine, AES_modulus, 8))
            elif (i == 2):
                new_state_array[i][j] = (state_array[2][j].gf_multiply_modular(E, AES_modulus, 8) ^ 
                state_array[3][j].gf_multiply_modular(B, AES_modulus, 8) ^
                state_array[0][j].gf_multiply_modular(D, AES_modulus, 8) ^ 
                state_array[1][j].gf_multiply_modular(nine, AES_modulus, 8))
            elif (i == 3):
                new_state_array[i][j] = (state_array[3][j].gf_multiply_modular(E, AES_modulus, 8) ^ 
                state_array[0][j].gf_multiply_modular(B, AES_modulus, 8) ^
                state_array[1][j].gf_multiply_modular(D, AES_modulus, 8) ^ 
                state_array[2][j].gf_multiply_modular(nine, AES_modulus, 8))
    return new_state_array



def gen_key_schedule_256(key_bv):
    #  We need 60 keywords (each keyword consists of 32 bits) in the key schedule for
    #  256 bit AES. The 256-bit AES uses the first four keywords to xor the input
    #  block with.  Subsequently, each of the 14 rounds uses 4 keywords from the key
    #  schedule. We will store all 60 keywords in the following list:
    key_words = [None for i in range(60)]
    round_constant = BitVector(intVal = 0x01, size=8)
    for i in range(8):
        key_words[i] = key_bv[i*32 : i*32 + 32]
    for i in range(8,60):
        if i%8 == 0:
            kwd, round_constant = gee(key_words[i-1], round_constant, subBytesTable)
            key_words[i] = key_words[i-8] ^ kwd
        elif (i - (i//8)*8) < 4:
            key_words[i] = key_words[i-8] ^ key_words[i-1]
        elif (i - (i//8)*8) == 4:
            key_words[i] = BitVector(size = 0)
            for j in range(4):
                key_words[i] += BitVector(intVal = 
                                 subBytesTable[key_words[i-1][8*j:8*j+8].intValue()], size = 8)
            key_words[i] ^= key_words[i-8] 
        elif ((i - (i//8)*8) > 4) and ((i - (i//8)*8) < 8):
            key_words[i] = key_words[i-8] ^ key_words[i-1]
        else:
            sys.exit("error in key scheduling algo for i = %d" % i)
    return key_words

def gee(keyword, round_constant, byte_sub_table):
    '''
    This is the g() function you see in Figure 4 of Lecture 8.
    '''
    rotated_word = keyword.deep_copy()
    rotated_word << 8
    newword = BitVector(size = 0)
    for i in range(4):
        newword += BitVector(intVal = byte_sub_table[rotated_word[8*i:8*i+8].intValue()], size = 8)
    newword[:8] ^= round_constant
    round_constant = round_constant.gf_multiply_modular(BitVector(intVal = 0x02), AES_modulus, 8)
    return newword, round_constant


def encrypt(plaintext, key, ciphertext):
    outfile = open(ciphertext, "w")
    bv = BitVector(filename = plaintext)
    key_bv = BitVector(filename = key)
    read_key = key_bv.read_bits_from_file( 256 )
    key_words = gen_key_schedule_256(read_key)
    
    
    while (bv.more_to_read):
        bitvec = bv.read_bits_from_file(128)
        while (bitvec._getsize() % 128 != 0):
            bitvec.pad_from_right(1)
        statearray = [[0 for x in range(4)] for x in range(4)]
        for i in range(4):
            for j in range(4):
                statearray[j][i] = bitvec[32*i + 8*j:32*i + 8*(j+1)]
        statearray = xor_round_keys(statearray, key_words, 0)
        for round in range(1,14):
            statearray = sub_bytes(statearray)
            statearray = shift_rows(statearray)
            statearray = mix_columns(statearray)
            statearray = xor_round_keys(statearray, key_words, round)
        statearray = sub_bytes(statearray)
        statearray = shift_rows(statearray)
        statearray = xor_round_keys(statearray, key_words, 14)
        final_bv = BitVector(size = 0)
        for i in range(4):
            for j in range(4):
                final_bv = final_bv + statearray[j][i]
        outfile.write(final_bv.get_bitvector_in_hex())

def decrypt(ciphertext, key, plaintext):
    infile = open(ciphertext, "r")
    text = infile.read()
    blocks = int( len(text) / 32)
    outfile = open(plaintext, "w")
    key_bv = BitVector(filename = key)
    read_key = key_bv.read_bits_from_file( 256 )
    key_words = gen_key_schedule_256(read_key)
    for i in range(blocks):
        
        bitvec = BitVector(hexstring = text[i * 32 + 0: i * 32 + 32])
        if bitvec._getsize() > 0:
            statearray = [[0 for x in range(4)] for x in range(4)]
            for i in range(4):
                for j in range(4):
                    statearray[j][i] = bitvec[32*i + 8*j:32*i + 8*(j+1)]
            statearray = xor_round_keys(statearray, key_words, 14)
            for round in range(13,0, -1):
                statearray = inverse_shift_rows(statearray)
                statearray = inverse_sub_bytes(statearray)
                statearray = xor_round_keys(statearray, key_words, round)
                statearray = inverse_mix_columns(statearray)
            statearray = inverse_shift_rows(statearray)
            statearray = inverse_sub_bytes(statearray)
            statearray = xor_round_keys(statearray, key_words, 0)
            final_bv = BitVector(size = 0)
            for i in range(4):
                for j in range(4):
                    final_bv = final_bv + statearray[j][i]
            ascii_final_string = final_bv.get_bitvector_in_ascii()
            outfile.write(ascii_final_string)
        else:
            print("?")
            
            



if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit('''Needs 4 command line arguments, one for '''
            '''the encryption or decrtpyion, one for the input text'''
            '''one for the key, and one for the output text''')
    if sys.argv[1] == "-e":
        encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "-d":
        decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit('''argument one is not of form "-e" or "-d"''')




