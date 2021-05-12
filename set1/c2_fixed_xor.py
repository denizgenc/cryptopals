#!/usr/bin/env python3
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179

def fixed_xor(first, second):
    xored_bytes = [byte1 ^ byte2 for byte1, byte2 in zip(first, second)]
    
    return bytes(xored_bytes)

if __name__ == "__main__":
    bytestring1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    bytestring2 = bytes.fromhex("686974207468652062756c6c277320657965")
    answer = fixed_xor(bytestring1, bytestring2).hex() # convert to hex string
    check = "746865206b696420646f6e277420706c6179"

    print("Did I get it right?", answer == check)
