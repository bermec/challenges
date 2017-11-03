'''
The Greatest Common Divisor of a given set of integers is the greatest integer
that can divide these integers without any remainder. From Wikipedia, take a
look at this example: for the integers 8 and 12, the highest integer that
divides them without remainder is 4.

Your goal is to write a program that takes two integers, and returns the
greatest common divisor. You may pick any algorithm or approach you prefer,
though a good starting point is Euclid's algorithm.

Author: nint22
Formal Inputs & Outputs
Input Description

You will be given two space-delimited integers on the standard console input.
Output Description

Simply print the GCD value for the two given integers. If no GCD exists, print one ('1').
Sample Inputs & Outputs
Sample Input

32 12
142341 512345
65535 4294967295

Sample Output

4
1
65535

On a learning curve here so I'll take the long route  :)
'''

import math
import re

def divisors(n):
    """
    Find all divisors of n by trial division
    """
    divisors = []
    for i in range(1, math.ceil(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
    return divisors


if __name__ == '__main__':

    candidates = '''32 12
142341 512345
65535 4294967295'''

    candidates = candidates.split('\n')

    for line in candidates:
        line = line.strip()
        a = re.findall('^(\d+)\s', line)
        b = re.findall('\d+\s(\d+)', line)
        list_a = divisors(int(a[0]))
        list_b = divisors(int(b[0]))

        comparison_dict = {}

        for num in list_a:
            comparison_dict[num] = comparison_dict.setdefault(num, 0) + 1
        for num in list_b:
            comparison_dict[num] = comparison_dict.setdefault(num, 0) + 1

        max_key_val = []
        max_key_val = [key for key, val in comparison_dict.items() if val == max(comparison_dict.values())]

        print(max(max_key_val))



