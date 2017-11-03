'''
Write a function that prints all of the permutatons of the unique characters
of a given string. For example, permute("baz") would print:

baz
bza
abz
azb
zba
zab

Find all the permutations of daily.

Author: skeeto
Formal Inputs & Outputs
Input Description

Your function should accept a single string variable which is guaranteed
to be at least 1 character long.
Output Description

Print all permutations of the given string variable.
Sample Inputs & Outputs
Sample Input

Let the string argument be "ab"
Sample Output

All permutations of "ab" would be ["ab", "ba"]
Challenge Input

Let the string argument be "abbccc"
Challenge Input Solution

abbccc abcbcc abccbc abcccb acbbcc acbcbc acbccb accbbc accbcb acccbb babccc
bacbcc baccbc bacccb bbaccc bbcacc bbccac bbccca bcabcc bcacbc bcaccb bcbacc
bcbcac bcbcca bccabc bccacb bccbac bccbca bcccab bcccba cabbcc cabcbc cabccb
cacbbc cacbcb caccbb cbabcc cbacbc cbaccb cbbacc cbbcac cbbcca cbcabc cbcacb
cbcbac cbcbca cbccab cbccba ccabbc ccabcb ccacbb ccbabc ccbacb ccbbac ccbbca
ccbcab ccbcba cccabb cccbab cccbba
Note

    Bonus 1: Instead of printing, be functional. Return a collection (array, etc.)
    of the permutations.

    Bonus 2: Correctly handle the case when the input contains a character multiple
    times. That is, don't output repeats and ensure the output contains the same
    number of characters as the input. For example, there are three permutations of
    foo: foo, ofo, oof.

    Note that this challenge is a near-duplicate of challenge #12, hence why there
    is the above "bonus" challenges

'''

'''
Note: 
To understand this algorithm try doing it on paper:
Permute "A" --> A
Then permute "AB" --> AB, BA
Then permute "ABC" --> CAB, ACB, ABC, CBA, BCA, BAC

Realise that what your doing each time you lengthen the string by a
character is you're adding the new character to each potential location
in the permutations of the previous string - this is most obvious in the
"ABC" example:
    Add C to each point in AB --> CAB, ACB, ABC
    Add C to each point in BA --> CBA, BCA, BAC
'''


def to_string(lst):
    return ''.join(lst)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

sett = set()
def permute(a, l, r):

    if l == r:
        sett.add(to_string(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
    return sett

if __name__ == '__main__':
    strng = "abbccc"
    n = len(strng)
    a = list(strng)
    ans = permute(a, 0, n-1)
    print(ans)





