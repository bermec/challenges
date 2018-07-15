'''
In this challenge, we propose a simple image file format for binary
(2 color) black-and-white images.
Rather than describing the image as a sequence of bits in a row,
instead we describe it in a little bit of a non-standard way.

Imagine a grid of white squares. On this grid, a single man carrying
a large black stamp stands on the square at 0,0. You can tell him 5
commands: walk N,S,E,W, and stamP. This will cause him to wander
around the grid, and when he receives a stamp command, he will
change the white square there to black. By giving him the sequencer
of commands of how to move, you can render an arbitrary b+w image.

The input file will have two integers describing the size of the grid.
Then, it will contain a sequence of characters. These characters
escribe the command sequence to execute to create the image. The
program should output the image in some way. For example, it might
print it to a png file or print it in ascii art to the screen.

As an example, the input file

5 5 PESPESPESPESPNNNNPWSPWSPWSPWSP

would output a 5x5 grid with an X in it.

SUPER BONUS: implement a program that can convert an arbitrary
image to the walkaround rasterizer format.
                                               '''
N = 5
lsts = []
temp = []
# construct a blank matrix
for x in range(0, N):
    for y in range(0, N):
        temp.append(' ')
    lsts.append(temp)
    temp = []

m = 0
n = 0

strng = 'EEsEESWsWWsWSEsEEsESWsWWsWSsEsEsEsEsE'

for letter in strng:
    if letter == 'N':
        m -= 1
    elif letter == 'S':
        m += 1
    elif letter == 'E':
        n += 1
    elif letter == 'W':
        n -= 1
    else:
        if letter == 's':
            lsts[m][n] = '#'
# print resultant pattern
result = ''
for lst in lsts:
    for element in lst:
        result += element
    print(result, end='')
    result = ''
    print(result)