# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.
# (Your code from #3 should help.) 

# I modified the text file by adding a single newline at the end.

from c3_xor_decrypt import xor_decrypt, frequency_score

decrypted_strings = [] # bit of a misnomer, as...

with open('4.txt') as hexes:
    for hexstring in hexes:
        hexstring = hexstring[:-1] # strip \n escape sequence
        decrypted = bytearray.fromhex(xor_decrypt(hexstring))
#        print(decrypted) # debug
        decrypted_strings.append(decrypted)
        # only one of these strings was actually encrypted in the first place
        # the rest of the list will be full of random character jumbles
        # that just so happened to have the lowest score after being run through
        # frequency_score


# The following gives me the wrong answer - let's look for the top 5
# scoring strings instead

# score = 100
# best_guess = ""
# for s in decrypted_strings:
    # s_score = frequency_score(s)
    # if s_score < score:
        # score = s_score
        # best_guess = s

# print(best_guess)

score_list = []
for s in decrypted_strings:
    s_score = frequency_score(s)
    score_list.append([s_score,s]) # list of lists, where each list is a score and the string

sorted_scores = sorted(score_list)
for i in range(20):
    print(sorted_scores[i][1]) # print the strings only
