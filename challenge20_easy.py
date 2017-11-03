''' create a program that will find all prime numbers below 2000
'''

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

    for x in range (3,int (n ** 0.5) + 1, 2):

            if n % x == 0:

                return False
                #n = n+ 1
    return True

if __name__ =='__main__':

    lst = []
    for x in range (1999, 1, -1):
        if isprime(x):
            lst.append(x)

    print(lst)