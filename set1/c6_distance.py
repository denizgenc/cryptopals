def hamming_distance(bytes_1, bytes_2):
    """Returns the Hamming distance between 2 bytes objects."""
    distance = 0

    for char_1, char_2 in zip(bytes_1, bytes_2):
        xor = char_1 ^ char_2
        distance += f"{xor:b}".count('1')

    # If bytes objects are a different length, all the extra characters have
    # "different" bits, so add them to the distance
    length_difference = abs(len(bytes_1) - len(bytes_1))
    distance += (length_difference * 8) # 8 bits per byte

    return distance

