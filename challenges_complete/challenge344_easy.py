'''
In mathematics, the Baum–Sweet sequence is an infinite automatic
sequence of 0s and 1s defined by the rule:

    b_n = 1 if the binary representation of n contains no block
of consecutive 0s of odd length; b_n = 0 otherwise;

for n >= 0.

For example, b_4 = 1 because the binary representation of 4 is 100,
which only contains one block of consecutive 0s of length 2;
whereas b_5 = 0 because the binary representation of 5 is 101,
which contains a block of consecutive 0s of length 1. When n is
19611206, b_n is 0 because:

19611206 = 1001010110011111001000110 base 2
            00 0 0  00     00 000  0 runs of 0s
               ^ ^            ^^^    odd length sequences

Because we find an odd length sequence of 0s, b_n is 0.
Challenge Description

Your challenge today is to write a program that generates the
Baum-Sweet sequence from 0 to some number n. For example,
given "20" your program would emit:

1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0


'''


def dec2bin(n):
    """ number -> str
    convert base 10 to base 2 """
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

    numstring[::-1]
    return numstring


if __name__ == '__main__':
    import re

    for x in range(0, 21):
        ans = dec2bin(x)

        b_s = re.findall('[0]+', ans)
        temp = ''
        if b_s == []:
            temp += '1'
        else:
            for extract in b_s:
                len_extract = len(extract) % 2
                if len_extract == 1:
                    temp += '0'
                    break
                else:
                    temp += '1'

        if '1' in temp:
            output = 1
        else:
            output = 0
        print(str(x) + ': ', output)