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
from itertools import permutations

def word_prep(n):
    #prepare word (lower case)
    word = n.lower()
    #build permutations of the word
    permed = perm(word)
    # build set of words and compare
    ans = compare(set_of_words, permed)
    return ans


def perm(name):
    the_family = set()
    for perm in permutations(name):
        perm = ''.join(perm)
        the_family.add(perm)
    return the_family


def word_set(a_set):
    set_of_words = set()
    family_set = set()
    with open('enable1.txt') as f:
        for line in f:
            line = line.strip()
            set_of_words.add(line)
    return set_of_word

def compare(words, group):
    for word in group:
        if word in set_of_words:
            family_set.add(word)

    return family_set


if __name__ =='__main__':
    set_of_words = word_set()
    name = 'APPLES'
    ans = word_prep(name)
    print(ans)