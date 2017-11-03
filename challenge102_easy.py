'''
In tabletop role-playing games like Dungeons & Dragons,
people use a system called dice notation to represent a
combination of dice to be rolled to generate a random
number. Dice rolls are of the form AdB (+/-) C, and are
calculated like this:

    Generate A random numbers from 1 to B and add them together.
    Add or subtract the modifier, C.

If A is omitted, its value is 1; if (+/-)C is omitted,
step 2 is skipped. That is, "d8" is equivalent to "1d8+0".

Write a function that takes a string like "10d6-2" or
"d20+7" and generates a random number using this syntax.

Here's a hint on how to parse the strings, if you get stuck:

Split the string over 'd' first; if the left part is empty, A = 1,
otherwise, read it as an integer and assign it to A. Then determine
whether or not the second part contains a '+' or '-', etc.
'''
import re
import random

def roll_dice(code):
    pass
    A = re.findall('^\d+|^\d', code)
    try:
        A = int(A[0])
    except:
        A = 1

    B = re.findall('d(\d+|\d)', code)
    B = int(B[0])
    C = re.findall('([+|-]\d+|\d)', code)
    C = int(C[-1])

    sum_rand = 0
    accum = 0
    while accum < A:
        random_number = random.randint(1, B)
        sum_rand += random_number
        accum += 1
    sum_rand += C

    return (sum_rand)


if __name__ == '__main__':

    roll = '10d6-2'
    ans = roll_dice(roll)
    print(ans)