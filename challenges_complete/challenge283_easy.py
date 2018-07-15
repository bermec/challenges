'''
An anagram is a form of word play, where you take a word (or set of words)
and form a different word (or different set of words) that use the same letters,
just rearranged. All words must be valid spelling, and shuffling words around
doesn't count.

Some serious word play aficionados find that some anagrams can contain meaning,
like "Clint Eastwood" and "Old West Action", or "silent" and "listen".

Someone once said, "All the life's wisdom can be found in anagrams. Anagrams
never lie." How they don't lie is beyond me, but there you go.

Punctuation, spaces, and capitalization don't matter, just treat the letters
as you would scrabble tiles.
Input Description

You'll be given two words or sets of words separated by a question mark.
Your task is to replace the question mark with information about the
validity of the anagram. Example:

"Clint Eastwood" ? "Old West Action"
"parliament" ? "partial man"

Output Description

You should replace the question mark with some marker about the
validity of the anagram proposed. Example:

"Clint Eastwood" is an anagram of "Old West Action"
"parliament" is NOT an anagram of "partial man"

Challenge Input

"wisdom" ? "mid sow"
"Seth Rogan" ? "Gathers No"
"Reddit" ? "Eat Dirt"
"Schoolmaster" ? "The classroom"
"Astronomers" ? "Moon starer"
"Vacation Times" ? "I'm Not as Active"
"Dormitory" ? "Dirty Rooms"

Challenge Output

"wisdom" is an anagram of "mid sow"
"Seth Rogan" is an anagram of "Gathers No"
"Reddit" is NOT an anagram of "Eat Dirt"
"Schoolmaster" is an anagram of "The classroom"
"Astronomers" is NOT an anagram of "Moon starer"
"Vacation Times" is an anagram of "I'm Not as Active"
"Dormitory" is NOT an anagram of "Dirty Rooms"

'''
import re

anagram_true = ' is an anagram of '
anagram_false = ' is NOT an anagram of '

first = []
second = []
with open('anagram_test_cases.txt') as f:
    for line in f:
        line = line.lower()
        line_front = re.findall("^(.*)\?", line)
        line_f = line_front[0]
        line_f.split()
        for element in line_f:
            if element.isalpha():
                first.append(element)
        line_rear = re.findall('(?<=\?).*', line)
        line_r = line_rear[0]
        line_r.split()
        for element in line_r:
            if element.isalpha():
                second.append(element)
        first.sort()
        second.sort()
        if first == second:
            print('{0}{1}{2}'.format(line_f, anagram_true, line_r))
        else:
            print('{0}{1}{2}'.format(line_f, anagram_false, line_r))
        first = []
        second = []

