# Each base64 digit represents exactly 6 bits of data. Three 8-bit bytes
# (i.e., a total of 24 bits) can therefore be represented
# by four 6-bit base64 encodings.
import string

# I'm going to generate a list of all the 4096 combinations of b64 characters
# because I am retarded and it's also 6:30 am
base64str = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
base64list = []
for i in base64str:
    for j in base64str:
        base64list.append(i+j)

def hexto64(hexstring):
    charlist = []
    for index in range(0, len(hexstring), 3):
        num = int(hexstring[index:index+3],16) # convert groups of 3 hex chars to ints
        charlist.append(base64list[num])
    
    return "".join(charlist)

hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
output = hexto64(hexstring)
check = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print(output)
print("Am I right? ", output == check)
