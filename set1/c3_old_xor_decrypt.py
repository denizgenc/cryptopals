# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

from c2_fixed_xor import fixed_xor

def frequency_score(candidate):
    """
    Scores a bytes/bytearray object based on the difference of the proportion of
    the characters in that string to the proportion of those characters
    in English.

    Better = closer to 0.

    I have concerns around overfitting with this function. However, limiting the
    `frequency_dict` to ETAOIN SHRDLU causes it to fail challenge 3, so I'm keeping it
    as is.
    """
    # from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html , retrieved
    # on 2021-04-20T23:07+01:00 )
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
        total_count = (candidate.count(char)
                      + candidate.count(bytes([int.from_bytes(char, 'big') - 32])) )
            # Need to count uppercase characters too, which are offset by 32
        proportion = float(total_count) / len(candidate)
        # len(candidate) is why we need to pass the object as a bytes/bytearray
        # if we .decode() into a string, candidate will have length 0.
        # This is because the loop in xor_decrypt XORs the string against every
        # possible byte - so the first character in the string will eventually
        # be EOF, and we will have a zero length candidate.
        # This leads to a division by zero error, of course.
        score += abs(proportion - frequency_dict[char])

    # The following checks for control characters in candidate, and penalises
    # for each one
    # for byte in candidate: # individual elements in a bytearray are ints??
    #     if byte < 32:
    #         score += 10
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

        current_score = frequency_score(xored)
        if current_score < best_score:
            best_score = current_score
            best_guess = xored

    return best_guess, best_score
