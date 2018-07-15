"""
A set of mathematical helper functions
"""
import math

# Check for an even number
def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Check  for a modulus ( 7.777 etc )
def isodd(num):
    if float(num) % 2 == 0:
        return False
    else:
        return True

#Multiplier for the prime number multiplication.
def multiplylist(numlist):
    total = 1
    for pnum in numlist:
        total = total * pnum
    return total

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

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def primes(n):
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def gen_x(x,generator):
    """
    Generate "x" amount of items from "generator"
    """
    z = 0
    result = []
    for i in generator():
        result.append(i)
        z += 1
        if z == x:
            break
    return result

def divisors(n):
    """
    Find all divisors of n by trial division
    """
    divisors = set([1])
    for i in range(1, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n/i)
    return divisors

def stufftoint(stuff):
    return list(map(int, stuff))

#fibonacci generator (to 1000 adjustable)
def fibonacci_gen(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_to_dec(num):
    ''' (str) -> number
    base fibonacci to base 10'''
    output = 0
    f = fibonacci_gen()
    fib = next(f)
    for x in range(len(num) - 1, -1, -1):
        fib = next(f)
        fib_num = num[x]
        if fib_num == str(1):
            output += fib
    return output

def listadd(l):
    result = list(l)            # Make a duplicate of d called result
    for key, value in enumerate(l):        # loop through d
        result[key] += 1        # Add one to result[key]
    return result

def count_chk(ltrs, count, prim, divcount, trigger):
    """
    Computes the number of divisors
    """
    ltrsnew = listadd(ltrs)
    divcount = multiplylist(ltrsnew)
    if divcount > trigger:
        return (ltrs, divcount)
    return (ltrs, divcount)

def int_gen ():
    i = 0
    while True:
        yield i
        i = i + 1


class TriangleNum():
    """
        Thread-Safe Triangular number generator
    """
    def __init__(self):
        self.currentTri = 0 # Starting values
        self.step = 1

    def __iter__(self):
        return self  # Simplest iterator

    def next(self):
        try:
            self.currentTri+=self.step # Generate a triangular number
            self.step+=1 # update the step
            return self.currentTri # return the triangular number
        except:
            pass

def gcd(a, b):
    ''' greatest common denominator of a, b'''
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        d += 1
    while a != b:
        if a % 2 == 0:
            a /= 2
        elif b% 2 == 0:
            b /= 2
        elif a > b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2
    g = a
    gcd = g * (2 ** d)
    return gcd


def simplify(a, b):
    ''' simplify a fraction'''
    ''' divide num, denom by gcd'''
    gcf = gcd(a, b)
    num = a / gcf
    denom = b / gcf
    return (num, denom)


def bin2dec(n):
    store = 0
    x = 0
    # y = index of n
    for y in range(len(n) - 1, -1, -1):
        m = n[y]
        m = int(m)
        store += m * (2 ** x)
        x += 1
    return  store


def dec2bin(n):
    numstring = ''
    if n % 2 == 0:
        numstring += str(0)
    else:
        numstring += str(1)
    while n > 1:
        n = n // 2

        if n % 2 == 0:
            numstring += str(0)
        else:
            numstring += str(1)
    return numstring[::-1]


