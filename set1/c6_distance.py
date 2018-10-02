def hamming_distance(string_1, string_2, encoding='utf-8'):
    """Returns the Hamming distance between 2 strings of a shared encoding
    (UTF-8 by default).
    """
    bytes_1 = bytearray(string_1, encoding)
    bytes_2 = bytearray(string_2, encoding)
    distance = 0

    for char_1, char_2 in zip(bytes_1, bytes_2):
        xor = char_1 ^ char_2
        distance += f"{xor:b}".count('1')

    # If strings are a different length, all the extra characters have
    # "different" bits, so add them to the distance
    length_difference = abs(len(string_1) - len(string_2))
    distance += (length_difference * 8) # 8 bits per character! Hopefully!

    return distance

test = hamming_distance('this is a test', 'wokka wokka!!!')
print(f"Is test ({test}) equal to 37? {test == 37}")
