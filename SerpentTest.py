from CryptoPlus.Cipher import python_Serpent
import time

key = '000102030405060708090A0B0C0D0E0F'.decode('hex')
IV = '00000000000000000000000000000000'.decode('hex')
plaintext = ('33B3DC87EDDD9B0F6A1F407D14919365'*32*1000).decode('hex')

cipher_init_time = time.time()

cipher = python_Serpent.new(key, python_Serpent.MODE_CBC, IV)
cipher_text = cipher.encrypt(plaintext)

cipher_finish_time = time.time()

cipher_time = cipher_finish_time - cipher_init_time

print '\nTiempo de cifrado -> ' + str(cipher_time)

decipher_init_time = time.time()

decipher = python_Serpent.new(key, python_Serpent.MODE_CBC, IV)
decipher_text = decipher.decrypt(cipher_text).encode('hex').upper()

decipher_finish_time = time.time()

decipher_time = decipher_finish_time - decipher_init_time


print 'Tiempo de descifrado -> ' + str(decipher_time)
