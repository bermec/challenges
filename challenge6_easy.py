''' You're challenge for today is to create a program that can calculate pi
accurately to at least 30 decimal places.

Try not to cheat :)

Using the Gregory/Leibniz formula.

'''
from decimal import *

pi = Decimal(4)
n = Decimal(4)
sign = Decimal(1)

for x in range(3, 24000000, 2):

    pi = pi - n / x * sign
    sign *= -1


getcontext().prec = 30
pi = Decimal(pi)


print(pi)