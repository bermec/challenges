'''

Write a program that given a word will find all one-word anagrams for that
word. So, for instance, if you put in "LEPROUS", it should return "PELORUS"
and "SPORULE". As a dictionary, use this file, which is a 1.8 mb text-file
with one word listed on each line, each word listed in lower-case. In this
problem description, I've used upper-case for all words and their anagrams,
but that is entirely optional, it's perfectly all right to use lower-case i
f you want to.

Using your program, find all the one-word anagrams for "TRIANGLE".

Bonus: if you looked up the anagrams for "PAGERS", you'd find that there was
actually quite a few of them: "GAPERS", "GASPER", "GRAPES", "PARGES" and "SPARGE".
Those five words plus "PAGERS" make a six-word "anagram family".

Here's another example of an anagram family, this time with five words: "AMBLERS",
"BLAMERS", "LAMBERS", "MARBLES" and "RAMBLES".

What is the largest anagram family in the dictionary I supplied? What is the
second largest?

'''
'''
word = 'PAGERS'
temp = word
word = word.lower()
anagram_word = (sorted(word))
anagram_word = ''.join(word)
#print(temp)
'''
from operator import itemgetter
from collections import OrderedDict
from itertools import permutations
import time

def open_txt(f):
    ''' text -> sorted text.
    Read file and sort contents'''
    ana_dict = {}
    txt_set = set()
    flag = True

    while flag:
        line = f.readline()
        line = line.strip()
        txt_set.add(line)
        if line == '':
            flag = False
    return txt_set


if __name__ == '__main__':

    tt = time.time()
    with open('enable11.txt') as f:
        text_set = open_txt(f)

    ana_dict = {}
    ana_set = set()
    accum = 2
    acc = 0
    with open('enable11.txt') as f:
        acc = 0
        for line in f:
            line = line.strip()
            for perm in permutations(line):
                perm = ''.join(perm)
                if perm in text_set:
                    ana_set.add(perm)
            acc = len(ana_set)
            if acc <= accum - 1:

                continue
            ana_dict[line] = acc
            ana_set = set()
            if acc > accum:
                accum = acc
                acc = 0
    print('done')
    first = OrderedDict(sorted(ana_dict.items(), key=itemgetter(1)))
    first = list(first.items())
    print(first[-1],first[-2], time.time() - tt)
