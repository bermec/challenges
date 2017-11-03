'''
A portable bitmap is one of the oldest image formats around and grants access to very simple image creation and sharing. Today, you will be creating an image of this format.

A simple PBM program can be seen here (Note that we'll be
creating the simplest version, a PBM, not PPM or PGM.)

But basically the program consists of the following:

    A 2byte string (usually 'P1') denoting the file format
    for that PBM

    2 integers denoting the Width and Height of our image
    file respectively

    And finally, our pixel data - Whether a pixel is 1 - Black or 0 - White.

Formal Inputs & Outputs
Input description

On standard console input you should be prompted to enter a
small piece of text ("programming", "proggit", "hello world" etc...)
Output description

The output will be a .PBM file consiting of an image which
contains the text you have entered
'''

code = '''
'''


candidates = 'PYTHONISTA'
wordlist = []


lst = sum(wordlist, [])

cols = len(candidates)
lenl = int(len(lst))
split = [lst[i:i + int(lenl / cols)] for i in range(0, lenl, int(lenl / cols))]

for row in zip(*split):
    print("".join(str.ljust(i, 12) for i in row))
