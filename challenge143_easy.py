'''

Braille is a writing system based on a series of raised / lowered bumps on a material,
for the purpose of being read through touch rather than sight. It's an incredibly
powerful reading & writing system for those who are blind / visually impaired.
Though the letter system has up to 64 unique glyph, 26 are used in English Braille for
letters. The rest are used for numbers, words, accents, ligatures, etc.

Your goal is to read in a string of Braille characters (using standard English Braille
defined here) and print off the word in standard English letters. You only have to
support the 26 English letters.
Formal Inputs & Outputs
Input Description

Input will consistent of an array of 2x6 space-delimited Braille characters. This array is
always on the same line, so regardless of how long the text is, it will always be on
3-rows of text. A lowered bump is a dot character '.', while a raised bump is an upper-case
'O' character.
Output Description

Print the transcribed Braille.
Sample Inputs & Outputs
Sample Input

O. O. O. O. O. .O O. O. O. OO
OO .O O. O. .O OO .O OO O. .O
.. .. O. O. O. .O O. O. O. ..

Sample Output

helloworld
'''


'''Convert to dict'''
braille = { 'O.....':'a', 'O.O...':'b', 'OO....':'c', 'O..OO.':'d', 'O...O.':'e', 'OO.O..':'f', 'OO.OO.':'g',
            'OO..O.':'h', '.O.O..':'i', '.O.OO.':'j', 'O.O..O':'k', 'OOO...':'l', 'O.OO..':'m', 'O.OOO.':'n',
            'O.O.O.':'o', 'OOOO..':'p', 'OOOOO.':'q', 'OOO.O.':'r', '.OO.O.':'s', '.OOOO.':'t', 'O...OO':'u',
            'O.O.OO':'v', '.O.OOO':'w', 'OO..OO':'x', 'OO.OOO':'y', 'O..OOO':'z'}

#-- read braille ---------------

sample = '''O. O. O. O. O. .O O. O. O. OO
OO .O O. O. .O OO .O OO O. .O
.. .. O. O. O. .O O. O. O. ..'''

# convert sample to list of lists
lst = []
for line in sample.splitlines():
    line = line.strip()
    line = line.strip('\n')
    lst.append(line)

# remove spaces
for x in range(0, len(lst)):
    temp = ''
    for element in lst[x]:
        if element != ' ':
            temp += element
        lst[x] = temp

# zip list of strings to zip object
zipped = zip(*lst)

# convert to list of tuples
zipped = list(zipped)

# flatten
zipped = list(sum(zipped,()))

# split into individual letters
for x in range(0, len(zipped), 6):
    letter = zipped[x: x+6]
    letter = ''.join(letter)
    if letter in braille:
        print(braille[letter], end='')
