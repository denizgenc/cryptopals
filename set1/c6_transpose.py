def transpose(byte_list, size):
    """
    Transposes a bytes object, byte_list, by a certain amount, size.
    Returns a list of lists, transposed, containing the transposed bytes.
    You can imagine this as dividing the byte_list into chunks of a certain size, then putting
    each first character of the chunk into its own list, then each 2nd character, and so on.
    """
    transposed = []
    for modulo in range(size):
        transposed.append([byte for index, byte in enumerate(byte_list) if index % size == modulo])

    return transposed
