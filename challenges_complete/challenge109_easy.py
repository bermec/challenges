'''
Write a function, where given a string, return true if it only
contains the digits from 0 (zero) to 9 (nine). Else, return false.

Formal Inputs & Outputs:

Input Description:

string data - a given string that may or may not contains digits;
will never be empty

Output Description:

Return True or False - true if the given string only contains
digits, false otherwise

Sample Inputs & Outputs:

"123" should return true. "123.123" should return a false.
"abc" should return a false.

Notes:

This is a trivial programming exercise, but a real challenge would
be to optimize this function for your language and/or environment.
As a recommended reading, look into how fast string-searching works.
'''

import re

def integers(s):
    ints = re.findall('(?<![.\d])\d+(?!\d*\.)', s)
    if ints == []:
        return False
    else:
        return True

if __name__ == '__main__':

    candidates = ['567', '567.89', 'qwerty']
    for candidate in candidates:
        ans = integers(candidate)
        print('{0}{1}{2}{3}'.format('ans: ', candidate, ' ', ans))


