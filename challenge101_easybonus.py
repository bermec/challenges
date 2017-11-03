'''
This challenge comes to us from user skeeto

Write a program to count the number years in an inclusive
range of years that have no repeated digits.

For example, 2012 has a repeated digit (2) while 2013 does not.
Given the range [1980, 1987], your program would return 7
(1980, 1982, 1983, 1984, 1985, 1986, 1987).

Bonus: Compute the longest run of years of repeated digits
and the longest run of years of non-repeated digits for [1000, 2013].

'''

def no_repeat(n, n2):

    accum = 0
    accum2 = 0
    longest_seq = 0
    longest_seq2 = 0
    sett = set()
    for x in range(n, n2 + 1):
        x = str(x)
        for digit in x:
            sett.add(int(digit))

        if len(str(n)) == len(sett):
            accum2 = 0
            accum += 1
            if accum > longest_seq:
                longest_seq = accum
            sett = set()
        else:
            accum= 0
            accum2 += 1
            if accum2 > longest_seq2:
                longest_seq2 = accum2
            sett = set()
    return (longest_seq, longest_seq2)


if __name__ == '__main__':
    num = 1000
    num2 = 2013
    ans = no_repeat(num, num2)
    print('{0}{1}{2}{3}'.format('repeated digits: ', ans[0],'  non-repeated digits: ', ans[1]))

