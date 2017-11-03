''' Welcome to cipher day!

write a program that can encrypt texts with an alphabetical caesar cipher.
This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!

Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW

The encryption can also be represented using modular arithmetic
by first transforming the letters into numbers, according to the scheme,
A = 0, B = 1,..., Z = 25.[1] Encryption of a letter x by a shift n
can be described mathematically as,[2]

    E_n(x) = (x + n) \mod {26}.

Decryption is performed similarly,

    D_n(x) = (x - n) \mod {26}.

'''

''''
Decrypt
ABCDEFG...... to
XYZABCD......
'''


def encode(letter):
    ''' str -> str '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    indx = alph.index(letter)
    shift = (indx - 3) % 26
    result = alph[shift]
    return result

if __name__ == '__main__':

    out = ''
    #message = 'retreat we are beat'
    message ='retreat'
    for letter in message:
        if letter.isalpha():
            out += encode(letter)
        else:
            out += ' '
    print('Message is {0} and when encrypted it is {1}'.format(message, out))