'''
Description:

Today we will be making some simple 8x8 bitmap pictures. You will be given 8 hex values
that can be 0-255 in decimal value (so 1 byte). Each value represents a row. So 8 rows
of 8 bits so a 8x8 bitmap picture.
Input:

8 Hex values.
example:

18 3C 7E 7E 18 18 18 18
Output:

A 8x8 picture that represents the values you read in.

For example say you got the hex value FF. This is 1111 1111 . "1" means the bitmap at that
location is on and print something. "0" means nothing is printed so put a space. 1111 1111
would output this row:

xxxxxxxx

if the next hex value is 81 it would be 1000 0001 in binary and so the 2nd row would output
(with the first row)

xxxxxxxx
x      x

Example output based on example input:

   xx
  xxxx
 xxxxxx
 xxxxxx
   xx
   xx
   xx
   xx

Challenge input:

Here are 4 pictures to process and display:

FF 81 BD A5 A5 BD 81 FF
AA 55 AA 55 AA 55 AA 55
3E 7F FC F8 F8 FC 7F 3E
93 93 93 F3 F3 93 93 93

Output Character:

I used "x" but feel free to use any ASCII value you want. Heck if you want to display
it using graphics, feel free to be creative here.

'''
import re

def hex_to_str(base16):
    scale = 16
    num_of_bits = 8

    my_hexdata = base16
    strng = ''
    bin_out =  bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

    for digit in bin_out:
        if digit == '1':
            strng += '='
        else:
            strng += ' '
    return strng

if __name__ == '__main__':

    base16 = '18 3C 7E 7E 18 18 18 18'
    base16 = re.findall('\d[A-Z]|[A-Z]\d|\d+|[A-Z]+', base16)
    for num in base16:
        ans = hex_to_str(num)
        print(ans)

    print()

    hex_matrix = '''FF 81 BD A5 A5 BD 81 FF
    AA 55 AA 55 AA 55 AA 55
    3E 7F FC F8 F8 FC 7F 3E
    93 93 93 F3 F3 93 93 93'''
    hex_matrix = hex_matrix.splitlines()
    for line in hex_matrix:
        base16 = re.findall('\d[A-Z]|[A-Z]\d|\d+|[A-Z]+', line)
        for num in base16:
            ans = hex_to_str(num)
            print(ans)