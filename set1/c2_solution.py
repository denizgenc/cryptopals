from c2_fixed_xor import fixed_xor

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
answer = fixed_xor(string1,string2).hex() # convert to hex string
check = "746865206b696420646f6e277420706c6179"

print("Did I get it right?", answer == check)
