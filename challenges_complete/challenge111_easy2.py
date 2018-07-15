'''
Write a function that, given a string, removes from the string any * character, or any character that's one to the left or one to the right of a * character. Examples:

"adf*lp" --> "adp"
"a*o" --> ""
"*dech*" --> "ec"
"de**po" --> "do"
"sa*n*ti" --> "si"
"abc" --> "abc"
'''

import re

def integers(s):
    ints = re.findall('(?<![*])[a-zA-Z]+(?![*])', s)
    if ints == []:
        return False
    else:
        return ints

if __name__ == '__main__':

    candidates = ['abc*rty']
    for candidate in candidates:
        ans = integers(candidate)
        print('{0}{1}{2}{3}'.format('ans: ', candidate, ' ', ans))
