def repeating_key(plaintext, key, encoding='utf-8'):
    """Encrypts the string "plaintext", by repeatedly XORing it against the key
    "key", returning a hex string "ciphertext".

    It assumes that "plaintext" and "key" are UTF-8 encoded strings, and will
    decode it as such. You can change this with the "encoding" parameter.
    """
    plaintext_bytes = bytes(plaintext, encoding)
    key_bytes = bytes(key, encoding)
    ciphertext_ints = []

    for index, byte in enumerate(plaintext_bytes):
        ciphertext_ints.append(byte ^ key_bytes[index % len(key_bytes)])
                                    # use modulo to keep looping over key

    ciphertext_bytes = bytes(ciphertext_ints)

    return ciphertext_bytes.hex()

