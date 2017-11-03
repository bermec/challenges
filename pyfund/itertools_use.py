from itertools import islice, count
from generator_comprehensions import  isprime

#prime_slice = islice(all_primes, 1000)
#print(prime_slice)

thousand_primes = islice((x for x in count() if isprime(x)), 1000)
thousand_primes = list(thousand_primes)
print(thousand_primes)
print(sum(thousand_primes))

#--  any, all  --------------------------

# true if any are True
print(any([False, False, True]))

# true if all are True
print(all([False, False, True]))

print(any(isprime(x) for x in range(1328,1361)))

print(all(name == name.title() for name in ['London', 'New York', 'Sydney']))




