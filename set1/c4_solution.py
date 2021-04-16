# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.
# (Your code from #3 should help.) 


from c3_xor_decrypt import xor_decrypt

with open("input/4.txt") as file:
    scores_and_strings = {}
    for line in file:
        decrypt, score, key = xor_decrypt(line.strip('\n')) # strip trailing newline
        scores_and_strings[score] = [decrypt.decode(errors="ignore"), line]

best_score = sorted(scores_and_strings)[-1] # sort by keys, then get highest key
best = scores_and_strings[best_score] # index by that key to get values
print(f"The key used was {key} - which is the character {bytes([key]).decode()}")
print(f"the best line had a score of {best_score}")
print(f"The xored lines were {best[1]}")
print(f"And, when decrypted, it was {best[0]}")

