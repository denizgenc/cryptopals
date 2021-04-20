# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

from c2_fixed_xor import fixed_xor

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

def xor_decrypt(encrypted):
    """
    Takes a hex string called encrypted and tries to XOR it against every possible
    byte.
    Returns a bytes object called the best_guess, and an integer representing its
    best score called best_score.
    For challenge 6 I also made it return an integer that represents the key, called
    best_key
    """
    best_score = 0
    best_guess = None
    best_key = 0
    for i in range(256):
        charstring = format(i, "x").zfill(2) * (len(encrypted)//2)
        # the above makes a string of repeating chars the same size as the string
        # we're decoding so that we can feed them both into the imported fixed_xor
        # zfill zero pads a string so that we get 01010101 instead of 1111
        xored = fixed_xor(encrypted, charstring)

        current_score = frequency_score_simple(xored)
        if current_score > best_score:
            best_score = current_score
            best_guess = xored
            best_key = i

    return best_guess, best_score, best_key
