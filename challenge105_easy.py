'''
Given a wordlist of your choosing, make a program to unscramble scrambled
words from that list. For sanity and brevity, disregard any words which
have ambiguous unscramlings, such as "dgo" unscrambling to both "dog" and "god."

Input:

A file which contains scrambled words and a wordlist to match it against

Output:

The unscrambled words which match the scrambled ones

'''


import random

wordlist = 'the quick brown fox jumped over that moon'

with open('scramble.txt', 'a')as f:
    # clear contents
    f.seek(0)
    f.truncate()
    wordlist = wordlist.split()
    # jumble the wordlist and write
    for word in wordlist:
        jumble = ""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]

        f.write(jumble + ' ')

# sort wordlist and make a dictionary
sorted_worddict = {}
for word in wordlist:
    sorted_word = sorted(word)
    sorted_word = ''.join(sorted_word)
    sorted_worddict[sorted_word] = word

# read from file and check against dictionary
output = ''
with open('scramble.txt', 'r') as f:
    for line in f:
        line = line.split()
        for read_word in line:
            read_word = sorted(read_word)
            read_word=''.join(read_word)
            target = sorted_worddict.get(read_word)
            output += target + ' '

print(output)