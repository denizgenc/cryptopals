import base64
from c6_distance import hamming_distance
from c6_transpose import transpose
from c3_xor_decrypt import xor_decrypt
from c5_repeating_key import repeating_key

with open("input/6.txt", 'rb') as f: # open in binary mode,
                                     # as base64.decodebytes won't work on str types
    bytes_file = bytes([byte for line in f for byte in base64.decodebytes(line)])

keysize_distances = []
for keysize in range(2, 41):
    chunk_1 = bytes_file[:keysize]
    chunk_2 = bytes_file[keysize:keysize*2]
    distance = hamming_distance(chunk_1, chunk_2)
    normalised_distance = distance / keysize
    keysize_distances.append(normalised_distance)

best_keysizes = [keysize_distances.index(i) + 2 for i in sorted(keysize_distances)[:5]]
                # find the smallest distances, then find its index in the list, then add 2,
                # as that will make it correspond to the keysize that produce the distance

for keysize in best_keysizes:
    print("###########################")
    print(f"KEYSIZE:{keysize}")
    print("###########################")
    transposed = transpose(bytes_file, keysize)
    single_char_keys = []
    for block in transposed:
        decoded, score, key = xor_decrypt(bytes(block).hex())
        print("Decoded:\n", decoded)
        single_char_keys.append(key)
    print(f"The key is {bytes(single_char_keys).decode(encoding='utf-8')}")
    decoded_hex = repeating_key(bytes_file.hex(), bytes(single_char_keys).hex())
    decoded = bytes.fromhex(decoded_hex).decode()
    print("And this is the decoded stuff:")
    print(decoded)
