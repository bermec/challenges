'''
 (Easy): Trigonometric Triangle Trouble, pt. 1

A triangle on a flat plane is described by its angles and side lengths,
and you don't need to be given all of the angles and side lengths to work
out the rest. In this challenge, you'll be working with right-angled triangles only.

Here's a representation of how this challenge will describe a triangle.
Each side-length is a lower-case letter, and the angle opposite each side
is an upper-case letter. For the purposes of this challenge, the angle C
will always be the right-angle. Your challenge is, using basic trigonometry
and given an appropriate number of values for the angles or side lengths, to
find the rest of the values.
Formal Inputs and Outputs
Input Description

On the console, you will be given a number N. You will then be given N lines,
expressing some details of a triangle in the format below, where all angles are
in degrees; the input data will always give enough information and will describe
a valid triangle. Note that, depending on your language of choice, a conversion
from degrees to radians may be needed to use trigonometric functions such as
sin, cos and tan.

Output Description

You must print out all of the details of the triangle in the same format as above.
Sample Inputs & Outputs
Sample Input

3
a=3
b=4
C=90

Sample Output

a=3
b=4
c=5
A=36.87
B=53.13
C=90

Tips & Notes

There are 4 useful trigonometric identities you may find very useful.

    Pythagoreas' Theorem, where h is the side length opposite the
    right-angle and r and s are any 2 other sides.

    3 Trigonometric Ratios

'''
import math


def sine(b, c):
    ''' Compute the sine of the
    right-angled triangle'''

    return (round(math.degrees(math.acos(b/c)), 2))


def cosine():
    ''' Cosine can be found to be
    180 - (sine + 90)'''

    return round(180 - (sine(b, c) + 90), 2)


if __name__ == '__main__':

    a = 3
    b = 4
    c = 5

    A = sine(b, c)
    B = cosine()
    C = 90
    print('a={0}\nb={1}\nc={2}\nA={3}\nB={4}\nC={5}'.format(a, b, c, A, B, C))



