# Each base64 digit represents exactly 6 bits of data. Three 8-bit bytes
# (i.e., a total of 24 bits) can therefore be represented
# by four 6-bit base64 encodings.
import string

base64str = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def hexto64(hexstring):
    # TODO: handle hex strings with an odd number of elements
    bytelist = []
    for index in range(0, len(hexstring), 2):
        num = int(hexstring[index:index+2], 16) # convert groups of 2 hex chars to ints
        bytelist.append(format(num, "08b"))
        # https://docs.python.org/3/library/string.html#format-specification-mini-language

    bits = "".join(bytelist)
    b64list = [] # This will hold the b64 characters we'll join and return
    for bit in range(0, len(bits), 6):
        num = int(bits[bit:bit+6], 2)
        b64list.append(base64str[num])

    return "".join(b64list)

# Baby version - this is actually better than my hacky method
# import base64
# def hexto64(hexstring):
    # byteslist = bytearray.fromhex(hexstring)
    # return base64.b64encode(byteslist)
