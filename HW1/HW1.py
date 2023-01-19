import cryptBreak
from BitVector import *
import io

def main():
    for someRandomInteger in range(4040, 4100):
        key_bv = BitVector(intVal=someRandomInteger, size=16)
        decryptedMessage = cryptBreak.cryptBreak('ciphertext.txt', key_bv)
        if 'Sir Lewis' in decryptedMessage:
            print('Encryption Broken!')
            print(decryptedMessage)
            #KEYFILEOUT = open('key.txt', 'wb')
            #key_bv.write_bits_to_fileobject(KEYFILEOUT)
            fp_write = io.StringIO()
            key_bv.write_bits_to_stream_object(fp_write)
            print(fp_write.getvalue())
            #KEYFILEOUT.close()
            FILEOUT = open('decrypted.txt', 'w')                                            #(d)
            FILEOUT.write(decryptedMessage)                                              #(e)
            FILEOUT.close()
            break
        else:
            print(someRandomInteger)
            #print('Not decrypted yet')

if __name__ == "__main__":
    exit(main())