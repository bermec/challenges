8
''' You're challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of
the strings he wants to generate!

'''

import random

def pwords(m, n):
    strng2 = ''

    acc = 0
    while acc < m:
        #print(acc)
        strng2 += pword(n) + ' '
        acc += 1
    return strng2


def pword(n):
    ref = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!£%&1234567890'
    strg = ''
    while len(strg) < n:
        num = random.randrange(len(ref))
        strg += ref[num]
    return  strg

if __name__ =='__main__':

    length = int(input('Length of password?  '))
    amount = int(input('Number of passwords?  '))
    ans = pwords(amount, length)
    print(ans)