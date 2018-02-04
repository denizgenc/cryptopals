# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179

def fixed_xor(hexstring1, hexstring2):
    bytelist = []
    for index in range(0, len(hexstring1), 2):
        byte1 = int(hexstring1[index:index+2],16)
        byte2 = int(hexstring2[index:index+2],16)
        xorbyte = byte1 ^ byte2 # https://wiki.python.org/moin/BitwiseOperators
        bytelist.append(format(xorbyte, "x"))
    
    return "".join(bytelist)

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
answer = fixed_xor(string1,string2)
check = "746865206b696420646f6e277420706c6179"

print("Did I get it right?", answer == check)