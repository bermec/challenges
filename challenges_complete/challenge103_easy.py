'''
Back in the 90s (and early 00s) people thought it was a cool idea to
\/\/|2][73 |_1|<3 7H15 to bypass text filters on BBSes. They called it
Leet (or 1337), and it quickly became popular all over the internet.
The habit has died out, but it's still quite interesting to see the
various replacements people came up with when transforming characters.

Your job's to write a program that translates normal text into Leet,
either by hardcoding a number of translations (e.g. A becomes either
4 or /-\, randomly) or allowing the user to specify a random
translation table as an input file, like this:

A    4 /-\
B    |3 [3 8
C    ( {
(etc.)

Each line in the table contains a single character, followed by whitespace,
followed by a space-separated list of possible replacements. Characters
should have some non-zero chance of not being replaced at all.
Intermediate

Add a --count option to your program that counts the number of possible
outcomes your program could output for a given input. Using the entire
translation table from Wikipedia, how many possible results are there
for ./leet --count "DAILYPROG"? (Note that each character can also remain unchanged.)

Also, write a translation table to convert ASCII characters to hex codes
(20 to 7E), i.e. "DAILY" -> "4441494C59".
Difficult

Add a --decode option to your program, that tries to reverse the process,
again by picking any possibility randomly: /\/\/ could decode to
M/, or NV, or A/V, etc.

Extend the --count option to work with --decode: how many interpretations
are there for a given input?
'''

LEET_TABLE = {
    'A': ('@', '4', '^', '/\\', '/-\\'),
    'B': ('8', '6', '13', '|3', '/3', 'P>', '|:'),
    'C': ('<', '[', '(', '{'),
    'D': (')', '|)', '[)', '?', '|>', 'o|'),
    'E': ('3', '&', '[-'),
    'F': ('|=', '/=', '|#', 'ph'),
    'G': ('6', '9', '&', 'C-', '(_+'),
    'H': ('#', '}{', '|-|', ']-[', '[-]', ')-(', '(-)', '/-/'),
    'I': ('1', '!', '|', ']'),
    'J': (']', '_|', '_/', '</', '(/'),
    'K': ('X', '|<', '|{', '|('),
    'L': ('|', '1', '|_', '1_'),
    'M': ('|v|', '|\\/|', '/\\/\\', '(v)', '/|\\', '//.', '^^'),
    'N': ('|\\|', '/\\/', '/V', '^/'),
    'O': ('0', '()', '[]'),
    'P': ('|*', '|o', '|"', '|>', '9', '|7', '|^(o)'),
    'Q': ('9', '0_', '()_', '(_,)', '<|'),
    'R': ('2', '/2', '12', 'I2', 'l2', '|^', '|?', 'lz'),
    'S': ('5', '$', 'z', 'es'),
    'T': ('7', '+', '-|-', "']['"),
    'U': ('|_|', '(_)', 'L|', 'v'),
    'V': ('\\/', '^'),
    'W': ('VV', '\\/\\/', "\\\\'", "'//", '\\|/', '\\^/', '(n)'),
    'X': ('%', '*', '><', '}{', ')('),
    'Y': ('J', "'/"),
    'Z': ('2', '7_', '~/_', '>_', '%'),
    ' ': ('  ',)
}

import random

word = 'dailyprogrammer'
leet_output = ''

for char in word:
    char = char.upper()
    leet_tuple = LEET_TABLE[char]
    num = random.randrange(len(leet_tuple))
    leet = leet_tuple[num]
    leet_output += leet +' '

print(leet_output)