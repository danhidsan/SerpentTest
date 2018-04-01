from CryptoPlus.Cipher import python_Serpent

key = '000102030405060708090A0B0C0D0E0F'.decode('hex')
IV = '00000000000000000000000000000000'.decode('hex')
plaintext = ('33B3DC87EDDD9B0F6A1F407D14919365'*3).decode('hex')
cipher = python_Serpent.new(key, python_Serpent.MODE_CBC, IV)
cipher_text = cipher.encrypt(plaintext)
decipher = python_Serpent.new(key, python_Serpent.MODE_CBC, IV)
decipher_text = decipher.decrypt(cipher_text).encode('hex').upper()

print cipher_text
print decipher_text
