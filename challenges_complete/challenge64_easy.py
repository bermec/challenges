''' The divisors of a number are those numbers that divide it evenly;
for example, the divisors of 60 are 1, 2, 3, 4, 5, 6, 10, 12, 15,
20, 30, and 60. The sum of the divisors of 60 is 168, and the
number of divisors of 60 is 12.

The totatives of a number are those numbers less than the given number
and coprime to it; two numbers are coprime if they have no common factors
other than 1. The number of totatives of a given number is
called its totient. For example, the totatives of 30 are
1, 7, 11, 13, 17, 19, 23, and 29, and the totient of 30 is 8.

Your task is to write a small library of five functions that
compute the divisors of a number, the sum and number of its
divisors, the totatives of a number, and its totient.
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
    for x in range (3,int (n**0.5)+1, 2):

            if n % x == 0:
                n = n+ 1
                return False
    return True


def divisors(n):
    lst = []
    for x in range(1, n + 1):
        if n % x == 0:
            lst.append(x)
    return lst

def sum_divisors(lst):
    return sum(lst)

def num_divisors(lst):
    return len(lst)

def coprime(n):
    lst = []
    for x in range(1, n + 1):
        if x == 1:
            lst.append(x)
        if isprime(x) and n % x != 0:
           lst.append(x)
    return lst


def totients(lst):
    return len(lst)


if __name__ == '__main__':
    num = 30
    ans = divisors(num)
    print('Divisors of ' + str(num) + ': ', ans)
    ans2 = sum_divisors(ans)
    print('Sum of the divisors: ', ans2)
    ans3 = num_divisors(ans)
    print('Number of divisors: ', ans3)
    ans4 = coprime(num)
    print('Totatives of the number: ', ans4)
    ans5 = totients(ans4)
    print('Totient of the number: ', ans5)