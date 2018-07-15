''' As we all know, when computers do calculations or store numbers,
they don't use decimal notation like we do, they use binary notation.
So for instance, when a computer stores the number 13, it doesn't
store "1" and "3", it stores "1101", which is 13 in binary.

But more than that, when we instruct it to store an integer,
we usually tell it to store it in a certain datatype with a
certain length. For (relatively small) integers, that length is
usually as 32 bits, or four bytes (also called "one word" on 32-bit
processors). So 13 isn't really stored as "1101",
it's stored as "00000000000000000000000000001101".

If we were to reverse that bit pattern, we would get
"10110000000000000000000000000000", which written in
decimal becomes "2952790016".

Write a program that can do this "32-bit reverse" operation,
so when given the number 13, it will return 2952790016.

Note: just to be clear, for all numbers in this problem,
we are using unsigned 32 bit integers.
'''
def num_bases(num, base):
    strng = ''
    while num != 0:
        out = num % base
        strng += str(out)
        num = num // base
    return (strng[::-1])


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

def pad(n):
    return n.rjust(32, '0')

def reverseString(nstring):
    return int(nstring[::-1])


if __name__ =='__main__':

    ans = bin2dec(str( reverseString(pad(num_bases(13, 2)))))
    print(ans)
