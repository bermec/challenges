summed_squares = sum(x*x for x in range(1, 10000))
print(summed_squares)

''' use list(summed_squares) for a list, above is very efficient - uses
minimum memory'''

# using an if clause


def isprime(n):

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes,
    #rejects other even numbers.
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range (3,int (n**0.5)+1, 2):

            if n % x == 0:
                n += 1
                return False
    return True

primes = sum(x for x in range(1001) if isprime(x))
print(primes)