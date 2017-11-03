''' Write a small program that can take a string:

"hi!"

and print all the possible permutations of the string:

"hi!"

"ih!"

"!hi"

"h!i"

"i!h"

etc...

thanks to hewts for this challenge!

'''
from itertools import  permutations

a = 'hi!'
string = ''
for  n in permutations(a, len(a)):
    for char in n:
        string += char
    print(string)
    string = ''