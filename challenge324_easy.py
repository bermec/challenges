'''
Write a program that outputs the highest number that is lower
or equal than the square root of the given number, with the
given number of decimal fraction digits.

Use this technique, (do not use your language's built in
square root function):
https://medium.com/i-math/how-to-find-square-roots-by-hand-f3f7cadf94bb

input format: 2 numbers: precision-digits Number

sample input

0 7720.17
1 7720.17
2 7720.17

sample output

87
87.8
87.86

challenge inputs

0 12345
8 123456
1 12345678901234567890123456789
'''

import re
import random

def guess(n, r, flag):
    if flag:
        random_num = 50
    else:
        random_num = r

    n = float(n)
    div_num = divide(n, random_num)
    av_num = average(div_num, random_num)
    return av_num, flag


def divide(a, b):
    div = a / b
    return div


def average(a, b):
    av = (a + b) / 2
    return av


if __name__ == '__main__':

    candidates = '''0 7720.17
    1 7720.17
    2 7720.17
    0 12345
    8 123456
    1 12345678901234567890123456789'''

    candidates = candidates.splitlines()
    for strng in candidates:
        precision = re.findall('\s?(\d+)\s', strng)[0]
        candidate = re.findall('(\d+\.?\d+)$', strng)[0]
        precision = int(precision)
        flag = True
        new_guess = 0
        temp = 0
        while True:
            period = '\.'
            digit = '\d'
            ans = guess(candidate, temp, flag)
            flag = False
            if ans[0] == temp:
                if precision == 0:
                    digit = '\d'
                    mult = precision * digit
                    result = re.findall('^\d+' + mult, str(temp))
                    print(result[0])
                else:
                    mult = precision * digit
                    result = re.findall('^\d+' + period + mult, str(temp))
                    print(result[0])

                break
            temp = ans[0]


