'''
 The number 19 is can be represented in binary as 10011.
 Lets define the operation of "rotating a number" as taking the last binary digit
 of that number and moving it so it becomes the first binary digit, and moving the
 other digits one step forward. I.e. if you rotate 10011, you get 11001 (i.e. 25),
 because the 1 that was in the last position has now moved to the first position.
 If you rotate it again, you get 11100 (i.e. 28).

If you rotate it again, something curious happens: you get 01110, which is the same as 1110
(i.e. 14) since leading zeroes don't count in a binary representation. That is to say,
when you rotate it this time, the zero disappears. If you rotate it once more, you get 0111,
which is the same as 111 (i.e. 7). Again, the zero has disappeared.

After that, the number remains the same regardless of how much you rotate it,
since the binary number representation of 7 only has 1's in it.

This gives us a sequence of numbers. Starting with 19 and then rotating it step by step
until we get a number with only 1's in the binary representation, we get

19 -> 25 -> 28 -> 14 -> 7

Lets call this a "binary rotation sequence" for 19. Here are the binary rotation sequences
for the numbers 69, 205 and 357, with the numbers written first in decimal and then in
binary to show what is going on:

69 -> 98 -> 49 -> 56 -> 28 -> 14 -> 7
1000101 -> 1100010 -> 110001 -> 111000 -> 11100 -> 1110 -> 111

205 -> 230 -> 115 -> 121 -> 124 -> 62 -> 31
11001101 -> 11100110 -> 1110011 -> 1111001 -> 1111100 -> 111110 -> 11111

357 -> 434 -> 217 -> 236 -> 118 -> 59 -> 61 -> 62 -> 31
101100101 -> 110110010 -> 11011001 -> 11101100 -> 1110110 -> 111011 -> 111101 -> 111110 -> 11111

Write a program that given a number will print out the binary rotation sequence for
 that number (you only need to print out the sequence in decimal).

What is the binary rotation sequence for 54321?

'''
dikt = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C',
        '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I',
        '19': 'J', '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O',
        '25': 'P', '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U',
        '31': 'V', '32': 'W', '33': 'X', '34': 'Y', '35': 'Z'}
# covert a base ten number to base 2 - 35
def num_bases(num, base):
    global dikt
    strng = ''
    while num != 0:
        out = num % base
        strng += dikt[str(out)]
        num = num // base
    return (strng[::-1])

# binary to decimal
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

def binary_rotation(n):
    lst = []
    lst.append(bin2dec(str(n)))
    n = str(n)
    while '0' in n:
        x = 0
        n = str(n)
        x = n[-1]
        y = n[:-1]
        if x == '0':
            n = y
        else:
            n = x + y
        dec = bin2dec(n)
        lst.append(dec)

    return  lst

if __name__ == '__main__':
    ans = binary_rotation(num_bases(54321, 2))
    print(ans)
