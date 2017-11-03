'''
Write A function that takes an amount of money, rounds it to the nearest penny and then
tells you the minimum number of coins needed to equal that amount of money. For Example:
"4.17" would print out:

Quarters: 16
Dimes: 1
Nickels: 1
Pennies: 2

Author: nanermaner
Formal Inputs & Outputs
Input Description

Your Function should accept a decimal number (which may or may not have an actual decimal,
in which you can assume it is an integer representing dollars, not cents). Your function
should round this number to the nearest hundredth.
Output Description

Print the minimum number of coins needed. The four coins used should be 25 cent, 10 cent,
5 cent and 1 cent. It should be in the following format:

Quarters: <integer>
Dimes: <integer>
Nickels: <integer>
Pennies: <integer>

Sample Inputs & Outputs
Sample Input

1.23
Sample Output

Quarters: 4
Dimes: 2
Nickels: 0
Pennies: 3

Challenge Input

10.24
0.99
5
00.06


'''

import re
C = 100
Q = 25
N = 10
D = 5


def coinage(n):
    n = str(float(n))
    dollars = re.findall('\d+(?=[\.])', n)
    cents = re.findall('(?<=\.)\d+', n)
    dollars = int(dollars[0])
    cents = int(cents[0])
    dollars_to_cents = dollars * C
    total_cents = dollars_to_cents + cents
    quarters = total_cents // Q
    remainder = total_cents - (quarters * Q)
    nickels = remainder // N
    remainder = remainder - (nickels * N)
    dimes = remainder // D
    remainder = remainder - (dimes * D)
    cents = remainder
    return(quarters, nickels, dimes, cents)



if __name__ == '__main__':
    change = ['10.24', '0.99', '5', '00.06']
    for num in change:
        ans = coinage(num)
        print('Quarters: ', ans[0], '\n', 'Nickels: ', ans[1], '\n', 'Dimes: ', ans[2], '\n', 'Cents: ', ans[3], '\n')