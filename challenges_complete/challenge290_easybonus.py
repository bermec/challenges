'''
In mathematics, a Kaprekar number for a given base is a non-negative integer,
the representation of whose square in that base can be split into equal two parts
that add up to the original number again. For instance, 45 is a Kaprekar number,
because 45**2 = 2025 and 20+25 = 45. The Kaprekar numbers are named after D. R. Kaprekar.

I was introduced to this after the recent Kaprekar constant challenge.

For the main challenge we'll only focus on base 10 numbers. For a bonus,
see if you can make it work in arbitrary bases.
Input Description

Your program will receive two integers per line telling you the start and
end of the range to scan, inclusively. Example:

1 50

Output Description

Your program should emit the Kaprekar numbers in that range. From our example:

45

Challenge Input

2 100
101 9000

Challenge Output

Updated the output as per this comment

9 45 55 99
297 703 999 2223 2728 4879 4950 5050 5292 7272 7777

'''


def hexAdd(a, b):
    '''int, int -> int
    hex addition'''
    x = int(a, 16)
    y = int(b, 16)
    z = x + y
    return hex(z)


def Kaprekar(a, b):
    '''int, int -> list'''
    output = []
    for n in range(a, b):
        # convert n to hex
        hex_n = hex(n)
        # squared n in base 10
        square = n ** 2
        # squares n in hex
        hex_sqr = hex(square)[2:]
        # for string slicing
        # if a single digit, pass bar '1'
        if len(hex_sqr) == 1 and hex_sqr == '1':
            output.append(hex_sqr)
            continue
        elif len(hex_sqr) == 1:
            continue
        half = len(hex_sqr) // 2
        front_half = (hex_sqr[0:half])
        rear_half = (hex_sqr[half:])
        # check result
        if hexAdd(rear_half, front_half) == hex_n:
            output.append(hex_n[2:])
    return output


if __name__ == '__main__':
    ans = Kaprekar(1, 1000)
    print(ans)


