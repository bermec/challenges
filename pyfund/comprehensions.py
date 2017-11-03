''' list comprehension'''

# [expr(item) for item in word]
words = 'Why sometimes I have believed as many as six ' \
        'impossible things before breakfast'

words = words .split()

comp = [len(word) for word in words]
print(comp)

''' set '''
from math import factorial

f = [len(str(factorial(x))) for x in range(20)]
print('list:', f)

# note duplicates above

f = {len(str(factorial(x))) for x in range(20)}
print('set: ', f)

''' dictionary '''

from pprint import pprint as pp

country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Maracco': 'Rabat',
                      'Stockholm': 'Sweden'}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

pp(capital_to_country)

# on the limit!

import os
import glob

file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)

# filtering

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i ==0:
            return  False
        return True

primes = [x for x in range(101) if is_prime(x)]
print(primes)

prime_square_divisors = {x * x: (1, x, x * x) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)

