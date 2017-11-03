'''
How many words contained in this dictionary have their letters in alphabetical order?
So, for instance the letters in "ghost" and "bee" is in alphabetical order,
but the letters in "cab" are not. (enable1.txt) 638
'''

accum = -1
flag = True
file = 'enable1.txt'
with open(file, 'r') as f:
    for word in f:
        if flag:
            accum += 1
        word = word.strip('\n')
        for letter in range(1, len(word)):
            test = ord(word[letter])
            test2 = ord(word[letter - 1])
            if test >= test2:
                flag = True
                continue
            else:
                flag = False
                break
print(accum)
