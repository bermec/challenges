'''
In number theory, a deficient or deficient number is a number n
for which the sum of divisors sigma(n)<2n, or, equivalently,
the sum of proper divisors (or aliquot sum) s(n)<n. The value
2n - sigma(n) (or n - s(n)) is called the number's deficiency.
In contrast, an abundant number or excessive number is a number
for which the sum of its proper divisors is greater than the number itself

As an example, consider the number 21. Its divisors are 1, 3, 7 and 21,
and their sum is 32. Because 32 is less than 2 x 21, the number 21 is deficient.
Its deficiency is 2 x 21 - 32 = 10.

The integer 12 is the first abundant number. Its proper divisors are
1, 2, 3, 4 and 6 for a total of 16. The amount by which the sum exceeds
the number is the abundance. The number 12 has an abundance of 4, for example.
The integer 12 is the first abundant number. Its divisors are 1, 2, 3, 4, 6, and 12,
and their sum is 28. Because 28 is greater than 2 x 12, the number 12 is abundant.
It's abundant by is 28 - 24 = 4. (Thanks /u/Rev0lt_ for the correction.)
Input Description

You'll be given an integer, one per line. Example:

18
21
9

Output Description

Your program should emit if the number if deficient, abundant
(and its abundance), or neither. Example:

18 abundant by 3
21 deficient
9 ~~neither~~ deficient

Challenge Input

111
112
220
69
134
85

Challenge Output

111 ~~neither~~ deficient
112 abundant by 24
220 abundant by 64
69 deficient
134 deficient
85 deficient
'''
''' Couldn't make any sense of the 'neither' report, if you did send me a message'''

def get_factors(n):
    factors = []
    for x in range(1, n):
        if n % x == 0:
            factors.append(x)
    return factors

def sum_factors(n):
    return sum(get_factors(n))

if __name__ == '__main__':
    lst ="""18
    21
    9"""
    lst2 ="""111
    112
    220
    69
    134
    85"""
    for n in range(1, 10001):
        diff = sum_factors(n) - n
        if diff == 0:
            print(n, ' neither')
