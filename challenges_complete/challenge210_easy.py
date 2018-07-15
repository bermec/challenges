''' 210
In this modern fast paced time of the internet it is a busy place for hardworking
unsigned integers (lets just call them ints) Believe it or not these ints love to
date and hook up. But they don't always get along.

Computer scientists have discovered 32 levels of compatibility. By comparing the
binary value of ints we can develop a percentage of compatibility. (these unsigned
integers need 32 bits to store in memory)

For today's challenge you will be given 2 unsigned ints who might be a match.
You will compute a percentage of compatibility by comparing the binary value of each
unsigned ints to each other. For every bit (1 or 0) in common they generate 1 match point.
The max will be 32 the lowest will be 0. You then display the percentage of compatibility.

Also as a service to the unsigned ints you will list the avoid number. This is the
number that is the pure opposite of that number (in binary)
Finding Compatibility:

So for my example I am using 8 bit integers. You must do this for all 32 bits of an integer.
But I am using 8 bit examples to keep it simple.

We are gonna compare 1 and 2

 1 in binary is 0000 0001
 2 in binary is 0000 0010

If you compare each bit place with each number you find that they have 6 bits in common.
(From left to right -- the first 6 bits are all 0 and so the same bit and so that is 6 match points)

the last 2 bits are not the same. They are different.

Therefore 1 and 2 have 6 out of 8 match points. For a compatibility score of 75%

The most compatible numbers will be the same number as all the bits match perfectly.
(We are all most compatible with ourselves the most)

So taking 1 in binary (0000 0001) the complete opposite number would have to be
(1111 1110) or 254. 1 and 254 should not be in the same data structure together ever.
Input:

 2 unsigned Integers x and y

Output

 % of compatibility
 x should avoid (x's opposite)
 y should avoid (y's opposite)

Example:

This is an 8 bit example - for your challenge you will be using 32 bit unsigned ints.

100 42

 100 in binary is 0110 0100
  42 in binary is 0010 1010

Comparing the bits we see that they have 4 match points. 50% compatible.

 the opposite of 100 in binary is 1001 1011 or (155)
 the opposite of 42 in binary is 1101 0101 or (213)

So our output should be

 50% Compatibility
 100 should avoid 155
 42 should avoid 213

Okay so not a great match but at intHarmony.com but we have done our job.
Challenge Inputs:

 20 65515
 32000 101
 42000 42
 13 12345
 9999 9999
 8008 37331
 54311 2
 31200 34335
'''


def dec2bin(num):
    ''' int -> string
    decimal to binary
    converter'''
    store = ''
    divisor = 0
    acc = 1

    # calc divisors required
    for x in range(0, num):
        divisor = 2 ** x
        if divisor == num:
            divisor = 2 ** x
            break
        elif divisor > num:
            divisor = 2 ** (x - 1)
            break
        else:
            continue
    # convert to binary
    while num > -1:
        try:
            ans = num // divisor
        except ZeroDivisionError:
            break
        store += str((int(ans)))
        num = num % divisor
        divisor /= 2
        divisor = int(divisor)

    # pad out wth zeros
    result = ''
    if store == '':
        result = result.zfill(32)
    elif len(store) <= 4:
        for x in range(0, len(store)):
            result += store[x]
        result = result.zfill(32)
    else:
        for x in range(0, len(store)):
            result += store[x]
        result = result.zfill(32)
    return result


def int_harmony(a, b):
    '''str' str -> int
    Award points, output percentage
    '''
    points = 0
    man = dec2bin(a)
    wife = dec2bin(b)

    for x in range(0, 32):
        if man[x] == wife[x]:
            points += 1
    ans = percent(points)
    return int(ans)


def percent(num):
    pcent = num / 32 * 100
    return pcent


def bintodec(strng):
    # flip-flop the bits
    num = 0
    new_strng = ''
    for x in range(0, 32):
        if strng[x] == '0':
            new_strng += '1'
        else:
            new_strng += '0'
    # convert to decimal
    num = 0
    power = 31
    for y in range(0, 32):
        mult = new_strng[y]
        num += int(mult) * (2 ** power)
        power -= 1
    return num


if __name__ == '__main__':
    first = 20
    second = 65515
    first_binary = dec2bin(first)
    second_binary = dec2bin(second)
    ans = int_harmony(first, second)
    print('{0}{1}{2}{3}{4}{5}{6}{3}{7}{5}{8}'.format(ans, '%', ' compatibility', '\n', first, ' should avoid ',
                                                     bintodec(first_binary), second, bintodec(second_binary)))

