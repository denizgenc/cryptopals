# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

from c2_fixed_xor import fixed_xor

def frequency_score(deciphered):
    """
    Scores a bytearray according to how many times it features the following
    characters: e, t, a, o, i and space
    Ripped off from mpizzzle's solution to this problem.
    """

    frequents = bytearray("etaoi ", 'utf-8')
    count = 0
    for char in frequents:
        count += deciphered.count(char) + deciphered.count(char - 32)
        # character plus uppercase characters (might be a mistake)

    return count

def xor_decrypt(encrypted):
    best_score = 0
    best_guess = None
    for i in range(256):
        charstring = format(i, "x").zfill(2) * (len(encrypted)//2)
        # the above makes a string of repeating chars the same size as the string
        # we're decoding so that we can feed them both into the imported fixed_xor
        # zfill zero pads a string so that we get 01010101 instead of 1111
        xored = fixed_xor(encrypted, charstring)

        current_score = frequency_score(xored)
        if current_score > best_score:
            best_score = current_score
            best_guess = xored

    return best_guess, best_score
