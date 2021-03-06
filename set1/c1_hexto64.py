#!/usr/bin/env python3
# Each base64 digit represents exactly 6 bits of data. Three 8-bit bytes
# (i.e., a total of 24 bits) can therefore be represented
# by four 6-bit base64 encodings.
import string

base64str = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def hexto64(hexstring):
    nibble_list = []
    for char in hexstring:
        num = int(char, 16) # convert hex char to a number
        nibble_list.append(format(num, "04b"))
        # https://docs.python.org/3/library/string.html#format-specification-mini-language

    bits = "".join(nibble_list)
    b64list = [] # This will hold the b64 characters we'll join and return
    for bit in range(0, len(bits), 6):
        num = int(bits[bit:bit+6], 2)
        b64list.append(base64str[num])

    # TODO: Handle when you have left over hex characters (underscore padding)

    return "".join(b64list)

# Baby version - this is actually better than my hacky method
# import base64
# def hexto64(hexstring):
    # byteslist = bytearray.fromhex(hexstring)
    # return base64.b64encode(byteslist)

if __name__ == "__main__":
    hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output = hexto64(hexstring)
    check = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print(output)
    print("Am I right? ", output == check)
