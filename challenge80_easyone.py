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

def word_prep(n):
    # build set of words and compare
    results = set()
    total = []
    candidate = 0
    check_set = set()
    for key, value in dict_of_words.items():
        candidate = value

        for key, value in dict_of_words.items():
            if value == candidate and key not in check_set:
                results.add((key))
                check_set.add(key)
        if len(results) > 0:
            total.append(results)
        results = set()
    return total


def word_dict():
    '''build dict of words word:ord()value'''
    accum = 1
    dict_of_words = {}
    with open('enable1.txt') as f:
        for line in f:
            line = line.strip()
            for letter in line:
                accum *= ord(letter)
            dict_of_words[line] = accum
            accum = 1
    return dict_of_words


if __name__ == '__main__':
    # create dictionary of text file
    dict_of_words = word_dict()
    # COUNT OCCURRENCES OF EACH ord()VALUE
    # d: list of values and occurences
    d = {}
    for key, value in dict_of_words.items():
        d[value] = d.get(value, 0) + 1

    # sort keys to find largest and second largest
    sorted_dict = sorted(d, key=d.get, reverse=True)
    sorted_first = (sorted_dict[0])
    sorted_second =(sorted_dict[1])

    # map keys to value and print total
    first_list = []
    second_list = []
    for key, value in dict_of_words.items():
        if value == sorted_first:
            first_list.append(key)
    print(first_list, len(first_list))

    for key, value in dict_of_words.items():
        if value == sorted_second:
            second_list.append(key)
    print(second_list, len(second_list))







