'''
As all of us who have read "Harry Potter and the Chamber of Secrets" knows,
the reason He-Who-Must-Not-Be-Named chose his creepy moniker is that "I Am
Lord Voldemort" is an anagram for his birthname, "Tom Marvolo Riddle".

I've never been good at these kinds of word-games (like anagrams),
I always find it hard to figure out that stuff manually. I find it much
more enjoyable to write computer programs to solve these problems for me.
In the spirit of that, today's problem is to find simple one-word anagrams
for other words.

Write a program that given a word will find all one-word anagrams for that
word. So, for instance, if you put in "LEPROUS", it should return "PELORUS"
and "SPORULE". As a dictionary, use this file, which is a 1.8 mb text-file
with one word listed on each line, each word listed in lower-case. In this
problem description, I've used upper-case for all words and their anagrams,
but that is entirely optional, it's perfectly all right to use lower-case i
f you want to.

Using your program, find all the one-word anagrams for "TRIANGLE".

(by the way, in case anyone is curious: a "PELORUS" is "a sighting device on a
ship for taking the relative bearings of a distant object", which I imagine
basically is a telescope bolted onto a compass, and a "SPORULE" is "a small spore")

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
                perm_acc += 1
                perm = ''.join(perm)

            acc = len(ana_set)
            if acc <= accum - 1:
                ana_set = set()
                continue
            ana_dict[line] = ana_set
            ana_set = set()
            if acc > accum:
                accum = acc
                acc = 0
    print('done')
    first = OrderedDict(sorted(ana_dict.items(), key=itemgetter(1)))
    first = list(first.items())
    print(first[-1],first[-2], time.time() - tt)
