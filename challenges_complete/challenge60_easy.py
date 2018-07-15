''' A polite number n is an integer that is the sum of
two or more consecutive non-negative integers in at least one way.

Here is an article helping in understanding Polite numbers

Your challenge is to write a function to determine
the ways if a number is polite or not.
'''
def polite(n):
    # 1 is an impolite number 0,1, inelegant but true
    if n == 1:
        return 'false', n
    for x in range (1, n):
        if n == 2 ** x:
            return  'false', n
    if n % 2 == 1:
        return 'true', n
    if n == 2 % 4:
        return  'false', n
    if n // 3 != 0 or n // 5 != 0:
        return  'true', n


if __name__ == '__main__':

    for y in range(1, 20):
        print(polite(y))
