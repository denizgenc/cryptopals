# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

from c2_fixed_xor import fixed_xor

def frequency_score(deciphered):
    """
    Scores a string based on the difference of the proportion of the characters
    in that string to the proportion of those characters in English.
    Better = closer to 0.
    """
    frequency_dict = {'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31,
    'n': 6.95, 's': 6.28, 'r': 6.02, 'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88,
    'c': 2.71, 'm': 2.61, 'f': 2.3, 'y': 2.11, 'w': 2.09, 'g': 2.03, 'p': 1.82,
    'b': 1.49, 'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11, 'j': 0.1, 'z': 0.07}
    
    score = 0
    for char in frequency_dict.keys():
        proportion_in_deciphered = float(deciphered.count(char)) / len(deciphered)
        score += abs(proportion_in_deciphered - frequency_dict[char])
        
    return score

def xor_decrypt(encrypted):
    best_score = 100 # some high number
    best_guess = ""
    for i in range(0,256):
        charstring = format(i, "x").zfill(2) * (len(encrypted)/2)
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
