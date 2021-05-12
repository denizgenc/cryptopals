#!/usr/bin/env python3
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
from c2_fixed_xor import fixed_xor

def frequency_score_intricate(candidate):
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
    # TODO: Use a frequency table that includes spaces (and potentially other punctutation)
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

def xor_decrypt_intricate(encrypted):
    """
    Takes a bytes object called encrypted and tries to XOR it against every possible
    byte.
    Returns a bytes object called the best_guess, and an integer representing its
    best score called best_score. The lower the best_score, the better.
    For challenge 6 I also made it return an integer that represents the key, called
    best_key
    """
    best_score = 100 # some high number
    best_guess = None
    best_key = 0
    for i in range(256):
        bytestring = bytes([i for _ in range(len(encrypted))])
        # the above makes a string of repeating chars the same size as the string
        # we're decoding so that we can feed them both into the imported fixed_xor
        # zfill zero pads a string so that we get 01010101 instead of 1111
        xored = fixed_xor(encrypted, bytestring)

        current_score = frequency_score_intricate(xored)
        if current_score < best_score:
            best_score = current_score
            best_guess = xored
            best_key = i

    return best_guess, best_score, best_key

def frequency_score_simple(candidate):
    """
    Scores a bytes object according to how many times it features the following
    characters: e, t, a, o, i and space
    Ripped off from mpizzzle's solution to this problem.
    """

    frequents = bytes("etaoi ", 'utf-8')
    count = 0
    for char in frequents:
        count += candidate.count(char)# + candidate.count(char - 32)
        # character plus uppercase characters (might be a mistake)
        # Yes, it was a mistake.

    return count

def xor_decrypt_simple(encrypted):
    """
    Takes a bytes object called encrypted and tries to XOR it against every possible
    byte.
    Returns a bytes object called the best_guess, and an integer representing its
    best score called best_score. The higher the best_score, the better.
    For challenge 6 I also made it return an integer that represents the key, called
    best_key
    """
    best_score = 0
    best_guess = None
    best_key = 0
    for i in range(256):
        bytestring = bytes([i for _ in range(len(encrypted))])
        xored = fixed_xor(encrypted, bytestring)

        current_score = frequency_score_simple(xored)
        if current_score > best_score:
            best_score = current_score
            best_guess = xored
            best_key = i

    return best_guess, best_score, best_key

def xor_decrypt(encrypted):
    """
    Alias for one of the above functions, here to maintain the interface that I was
    using in other solutions (such as challenge 4 and 6)
    """
    return xor_decrypt_simple(encrypted)

if __name__ == "__main__":
    hex_string = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    decrypted, score, _ = xor_decrypt_intricate(hex_string)
    # decrypted, score, _ = xor_decrypt_simple(hex_string)

    print(decrypted.decode())
    print(f"The score is {score}")
