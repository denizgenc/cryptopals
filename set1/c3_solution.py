from c3_xor_decrypt import xor_decrypt

decrypted = xor_decrypt("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

print(decrypted)
print(bytearray.fromhex(decrypted))