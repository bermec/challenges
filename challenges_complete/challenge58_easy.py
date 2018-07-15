''' As computer programmers are well aware, it can be very useful to
write numbers using numerical bases other than the familiar
base 10 notation we use in everyday life. In computer programming,
base 2 and base 16 are especially handy. In base 2,
the number 1234 becomes 10011010010 and in base 16 it becomes 4D2.

Because there are only 10 regular digits, when numbers are written in base 16,
the first few letters of the alphabet are added to represent the remaining
required digits, so 'A' stands in for 10, 'B' for 11, 'C' for 12,
'D' for 13, 'E' for 14 and 'F' for 15.

Of course, this trick of adding letters to stand in for numbers
allows us to represent higher bases than 16; if you can use all
letters of the alphabet, you can represent bases up to base 36
(because there are ten regular digits and 26 "letter-digits").
So for instance, 12345678 becomes 1L2FHE in base 23 and 4IDHAA in base 19.

Write a program that will take a number and convert it to any
base between 2 and 36. Have the program print out 19959694 in
base 35 and 376609378180550 in base 29.

NOTE: Many languages have this built in as a library function.
For instance, in Java, the function Integer.toString(i, radix)
does exactly this. However, the entire point of this challenge
is to write the program yourself, so you are not allowed to use
any library functions like this.

BONUS: A number is said to be "palindromic in base N" if, when
written in base N the number is the same backwards and forwards. So,
for instance, the number 16708 is palindromic in base 27,
because in base 27 the number is written as MOM, obviously a palindrome.
The number 12321 is a palindrome in in base 10, because 12321 written
backwards is 12321. Some numbers are palindromic in several bases, the
number 15167 for instance is palindromic in bases 9, 27, 28, 35 and 36.

In what bases is the number 10858 palindromic?
'''

dikt = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C',
        '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I',
        '19': 'J', '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O',
        '25': 'P', '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U',
        '31': 'V', '32': 'W', '33': 'X', '34': 'Y', '35': 'Z'}

def num_bases(num, base):
    global dikt
    strng = ''
    while num != 0:
        out = num % base
        strng += dikt[str(out)]
        num = num // base
    return (strng[::-1])

def palindrome(strng):
    if strng == strng[::-1]:
        return True
    return  False

if __name__ == '__main__':
    print(num_bases(19959694, 35))
    print(num_bases(376609378180550, 29))

    palins = ''
    num = 10858
    for x in range(2, 36):
        check = num_bases(num, x)
        if palindrome(check):
            palins += str(check) + ' '

    print('Palindromes of 10858: ', palins)