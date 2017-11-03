'''
ISBN's (International Standard Book Numbers) are identifiers for books. Given the correct sequence of digits,
one book can be identified out of millions of others thanks to this ISBN. But when is an ISBN not just a random slurry
of digits? That's for you to find out.
Rules

Given the following constraints of the ISBN number, you should write a function that can return True if a number
is a valid ISBN and False otherwise.

An ISBN is a ten digit code which identifies a book. The first nine digits represent the book and the last digit
is used to make sure the ISBN is correct.

To verify an ISBN you :-

    obtain the sum of 10 times the first digit, 9 times the second digit, 8 times the third digit...
    all the way till you add 1 times the last digit. If the sum leaves no remainder when divided by 11
    the code is a valid ISBN.

For example :

0-7475-3269-9 is Valid because

(10 * 0) + (9 * 7) + (8 * 4) + (7 * 7) + (6 * 5) + (5 * 3) + (4 * 2) +
(3 * 6) + (2 * 9) + (1 * 9) = 242 which can be divided by 11 and have no remainder.

For the cases where the last digit has to equal to ten, the last digit is written as X. For example 156881111X.
'''

import random

def is_isbn(num):
    start_num = 10
    accum = 0

    # navigate the isbn number
    for x in num:
        # if it is a number
        if int(x.isdigit()):
            # add to total after multiplication
            accum += (int(x) * start_num)
            start_num -= 1
        else:
            if x == 'X':
                accum += 10
    if accum%11 == 0:
        return ('True')
    else:
        return ('False')


def isbnCompiler():
    dash = '-'
    firstnum = str(random.randint(0, 1))
    secondnum = str(random.randint(1, 99999))
    secondnum = secondnum.rjust(5, '0')
    thirdnum = str(random.randint(1, 999))
    thirdnum = thirdnum.rjust(3, '0')

    firstnum_a = list(firstnum)
    secondnum_a = list(secondnum)
    thirdnum_a = list(thirdnum)
    list_for_summing = firstnum_a + secondnum_a + thirdnum_a

    accum = 0
    start_num = 10

    for x in list_for_summing:
        if x.isdigit:
            x = int(x)
            accum += (int(x) * start_num)
            start_num -= 1

    lastnum = 11 - accum%11
    if lastnum == 10:
        lastnum = 'X'
    elif lastnum == 11:
        lastnum = 0

    isbn = str(firstnum) + dash + str(secondnum) + dash + str(thirdnum) + dash + str(lastnum)
    # check number is legal
    if is_isbn(isbn):
        return isbn


if __name__ == '__main__':

    ans = is_isbn('0-7475-3269-9')
    print(ans)
    ans = is_isbn('1-5688-1111-X')
    print(ans)

    ans = isbnCompiler()
    print(ans)



