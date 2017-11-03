'''
An emirp ("prime" spelled backwards)
is a prime whose (base 10) reversal is also prime,
but which is not a palindromic prime. The first few are
13, 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, ..
Your task is to implement a function which prints out
the emirps below a number(input) given by the user.

'''
def emirps(n):
    emirps_lst = []
    for x in range(n, 0, -1):
        if isprime(x) and not palindrome(x) and isprime(reverse_num(x)):
            emirps_lst.append(x)
    return emirps_lst

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

def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return n

def reverse_num(n):
    n = str(n)
    n = n[::-1]
    return int(n)

if __name__ == '__main__':
    ans = emirps(64)
    print(ans)