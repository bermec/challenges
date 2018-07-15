'''
Welcome to this week's Theme Week. We're going to be creating our very own basic compression format
for short novels or writing. This format will probably not be practical for actual use, but may
serve as a rudimentary introduction to how data compression works. As a side task, it is advised to
use structured programming techniques, so your program is easy to extend, modify and maintain later
on (ie. later this week.) To keep in line with our Easy-Intermediate-Hard trend, our first step will
be to write the decompresser.

The basic idea of this compression scheme will be the dictionary system. Words used in the data will
be put into a dictionary, so instead of repeating phrases over and over again, you can just repeat a
number instead, thus saving space. Also, because this system is based around written text, it will be
specifically designed to handle sentences and punctuation, and will not be geared to handle binary data.
Formal Inputs and Outputs
Input Description

The first section of the input we are going to receive will be the dictionary. This dictionary is just
a list of words present in the text we're decompressing. The first line of input will be a number N
representing how many entries the dictionary has. Following from that will be a list of N words, on
separate lines. This will be our simple dictionary. After this will be the data.
Data Format

The pre-compressed data will be split up into human-readable 'chunks', representing one little segment
of the output. In a practical compression system, they will be represented by a few bytes rather than
text, but doing it this way makes it easier to write. Our chunks will follow 7 simple rules:

    If the chunk is just a number (eg. 37), word number 37 from the dictionary (zero-indexed, so 0 is
    the 1st word) is printed lower-case.

    If the chunk is a number followed by a caret (eg. 37^), then word 37 from the dictionary will be
    printed lower-case, with the first letter capitalised.

    If the chunk is a number followed by an exclamation point (eg. 37!), then word 37 from the dictionary
    will be printed upper-case.

    If it's a hyphen (-), then instead of putting a space in-between the previous and next words, put a
    hyphen instead.

    If it's any of the following symbols: . , ? ! ; :, then put that symbol at the end of the previous
    outputted word.

    If it's a letter R (upper or lower), print a new line.

    If it's a letter E (upper or lower), the end of input has been reached.

Remember, this is just for basic text, so not all possible inputs can be compressed. Ignore any other
whitespace, like tabs or newlines, in the input.

Note: All words will be in the Latin alphabet.
Example Data

Therefore, if our dictionary consists of the following:

is
my
hello
name
stan

And we are given the following chunks:

2! ! R 1^ 3 0 4^ . E

Then the output text is:

HELLO!
My name is Stan.

Words are always separated by spaces unless they're hyphenated.
Output Description

Print the resultant decompressed data from your decompression algorithm, using the rules described above.
Challenge
Challenge Input

20
i
do
house
with
mouse
in
not
like
them
ham
a
anywhere
green
eggs
and
here
or
there
sam
am
0^ 1 6 7 8 5 10 2 . R
0^ 1 6 7 8 3 10 4 . R
0^ 1 6 7 8 15 16 17 . R
0^ 1 6 7 8 11 . R
0^ 1 6 7 12 13 14 9 . R
0^ 1 6 7 8 , 18^ - 0^ - 19 . R E

(Line breaks added in data for clarity and ease of testing.)
Expected Challenge Output

I do not like them in a house.
I do not like them with a mouse.
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

'''

sample = '''i
do
house
with
mouse
in
not
like
them
ham
a
anywhere
green
eggs
and
here
or
there
sam
am'''

compressed = '''0^ 1 6 7 8 5 10 2 . R
0^ 1 6 7 8 3 10 4 . R
0^ 1 6 7 8 15 16 17 . R
0^ 1 6 7 8 11 . R
0^ 1 6 7 12 13 14 9 . R
0^ 1 6 7 8 , 18^ - 0^ - 19 . R E'''


import re

# convert sample into a list
samples = sample.splitlines()

def codes(a, b, flag):

    if a is None:
        pass
    elif a.isdigit():
        a = int(a)
        word = samples[a]
    if b is None:
        return word
    elif b == '^':
        return ' ' + word.capitalize()
    elif b == '!':
        return word.upper()
    elif b == '-':
        flag = True
        return ('-', flag)
    elif b == 'R':
        return ('\n', flag)
    elif b == 'E':
        return ('\r', flag)
    elif b == '.':
        return ('.', flag)
    elif b == ',':
        return (',', flag)

    else:
        return (samples[a], flag)


if __name__ == '__main__':
    output = ''
    flag = False
    # convert compressed into a list
    compressed = compressed.splitlines()
    for line in compressed:
        line = line.split()
        for element in line:
            digi_extract = re.findall('\d+', element)
            non_digi = re.findall('\W|[a-zA-Z]', element)
            result = []

            if len(digi_extract) == 0:
                result.append(None)
            else:
                result.append(digi_extract[0])
            words = result[0]

            try:
                result.append(non_digi[0])
            except IndexError:
                result.append('')
            if len(result) > 1:
                code1 = result[1]
            else:
                code1 = None
            ans = codes(words, code1, flag)
            if ans[1]:
                output += ans[0]
            else:
                output += ans[0] + ' '
                flag = False
    print('output: ', output)



