'''
Write a program that outputs the first recurring character in a string.
Formal Inputs & Outputs
Input Description

A string of alphabetical characters. Example:

ABCDEBC

Output description

The first recurring character from the input. From the above example:

B

Challenge Input

IKEUNFUVFV
PXLJOUDJVZGQHLBHGXIW
*l1J?)yn%R[}9~1"=k7]9;0[$

Bonus

Return the index (0 or 1 based, but please specify) where the original
character is found in the string.
'''

#a = 'abba'
a = 'IKEUNFUVFV'
#a = 'PXLJOUDJVZGQHLBHGXIW'
#a = '*l1J?)yn%R[}9~1"=k7]9;0[$'

# to store character and index
store = {}

for x in range(0, len(a)):
    indx = x
    char = a[x]
    # if the character is already in the dictionary
    # print out the character and its index.
    if char in store:
        print(char, store[char])
        exit()
    store[char] = indx


