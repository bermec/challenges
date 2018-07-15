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

def Kaprekar(a, b):
    output = []
    for n in range(a, b):
        square = n ** 2
        str_square = str(square)
        half = len(str_square) // 2
        # check for single digit error
        try:
            front_half = int(str_square[0:half])
        except ValueError:
            continue
        rear_half = int(str_square[half:])
        if rear_half + front_half == n:
            output.append(n)
        else:
            # right strip zeros and check again
            str_front_half = str(front_half)
            front_half = str_front_half.rstrip('0')
            front_half = int(front_half)
            if rear_half + front_half == n:
                output.append(n)
    return output

if __name__ == '__main__':

    ans = Kaprekar(1, 50)
    print(ans)
    ans = Kaprekar(2, 100)
    print(ans)
    ans = Kaprekar(101, 9000)
    print(ans)