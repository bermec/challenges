''' Description

Atbash is a simple substitution cipher originally for the Hebrew alphabet,
but possible with any known alphabet. It emerged around 500-600 BCE.
It works by substituting the first letter of an alphabet for the last letter,
the second letter for the second to last and so on, effectively reversing the alphabet.
Here is the Atbash substitution table:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: ZYXWVUTSRQPONMLKJIHGFEDCBA

Amusingly, some English words Atbash into their own reverses, e.g., "wizard" = "draziw."

This is not considered a strong cipher but was at the time.

For more information on the cipher, please see the Wikipedia page on Atbash.
Input Description

For this challenge you'll be asked to implement the Atbash cipher and encode (or decode)
some English language words. If the character is NOT part of the English alphabet (a-z),
you can keep the symbol intact. Examples:

foobar
wizard
/r/dailyprogrammer
gsrh rh zm vcznkov lu gsv zgyzhs xrksvi

Output Description

Your program should emit the following strings as ciphertext or plaintext:

ullyzi
draziw
/i/wzrobkiltiznnvi
this is an example of the atbash cipher

Bonus

Preserve case.

'''

# using modular arithmetic
def atbash(word):
    out_string = ''
    for x in word:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if x.isalpha():
            indx = alphabet.index(x)
            out_string += alphabet[25 - indx]
        else:
            out_string += x
    return out_string

if __name__ == '__main__':
    print('Atbash output:')

    candidate = 'ullyzi'
    first = atbash(candidate)
    print(candidate + ' -> ' + first)

    candidate = 'draziw'
    second = atbash(candidate)
    print(candidate + ' -> ' + second)

    candidate = '/i/wzrobkiltiznnvi'
    third = atbash(candidate)
    print(candidate + ' -> ' + third)

    candidate = 'gsrh rh zm vcznkov lu gsv zgyzhs xrksvi'
    fourth = atbash(candidate)
    print(candidate + ' -> ' + fourth)

    candidate = 'Oolbwh'
    preserve_case = atbash(candidate)
    print('Case preserved: ' + candidate + ' -> ' + preserve_case)


