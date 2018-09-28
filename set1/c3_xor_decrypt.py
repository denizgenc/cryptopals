# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

from c2_fixed_xor import fixed_xor

def frequency_score(deciphered):
    """
    Scores a bytes/bytearray object based on the difference of the proportion of
    the characters in that string to the proportion of those characters
    in English.
    Better = closer to 0.
    """
    frequency_dict = {b'e': 12.02, b't': 9.10, b'a': 8.12, b'o': 7.68,
                      b'i': 7.31, b'n': 6.95, b's': 6.28, b'r': 6.02,
                      b'h': 5.92, b'd': 4.32, b'l': 3.98, b'u': 2.88,
                      b'c': 2.71, b'm': 2.61, b'f': 2.3, b'y': 2.11, b'w': 2.09,
                      b'g': 2.03, b'p': 1.82, b'b': 1.49, b'v': 1.11,
                      b'k': 0.69, b'x': 0.17, b'q': 0.11, b'j': 0.1, b'z': 0.07}
    # bytes/bytearray.count() does not work on strings, so we need to have these
    # as bytes objects too.

    score = 0
    for char in frequency_dict.keys():
        proportion = float(deciphered.count(char)) / len(deciphered)
        # len(deciphered) is why we need to pass the object as a bytes/bytearray
        # if we .decode() into a string, deciphered will have length 0.
        # This is because the loop in xor_decrypt XORs the string against every
        # possible byte - so the first character in the string will eventually
        # be EOF, and we will have a zero length deciphered.
        # This leads to a division by zero error, of course.
        score += abs(proportion - frequency_dict[char])

    return score

def xor_decrypt(encrypted):
    best_score = 100 # some high number
    best_guess = None
    for i in range(256):
        charstring = format(i, "x").zfill(2) * (len(encrypted)//2)
        # the above makes a string of repeating chars the same size as the string
        # we're decoding so that we can feed them both into the imported fixed_xor
        # zfill zero pads a string so that we get 01010101 instead of 1111
        xored = fixed_xor(encrypted, charstring)

        hextostring = bytearray.fromhex(xored)
        current_score = frequency_score(hextostring)
        if current_score < best_score:
            best_score = current_score
            best_guess = xored

    return best_guess
