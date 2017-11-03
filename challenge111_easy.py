'''
Write a function that, given a string, removes from the string any * character,
 or any character that's one to the left or one to the right of a * character.
Examples:

"adf*lp" --> "adp"
"a*o" --> ""
"*dech*" --> "ec"
"de**po" --> "do"
"sa*n*ti" --> "si"
"abc" --> "abc"
'''

import re

def strip_out(s):
    ans = re.sub(r'(\w\*\w)|(\*\w)|(\w\*)', "", s)
    return ans

if __name__ == '__main__':

    candidates = ['adf*lp', 'a*o', '*dech*', 'de*po', 'sa*n*ti', 'abc']
    for candidate in candidates:
        ans = strip_out(candidate)
        print('{0}{1}{2}{3}'.format('ans: ', candidate, ' ', ans))
