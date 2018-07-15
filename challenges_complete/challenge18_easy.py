''' Often times in commercials, phone numbers contain letters so that they're easy to remember
(e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters
into a phone number with only numbers and the appropriate dash. Click here to learn more about the telephone keypad.

Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278

Most of the keys also bear letters according to the following system:
A standard telephone keypad.

    0 = none (in some telephones, "OPERATOR" or "OPER")
    1 = none (in some older telephones, QZ[citation needed])
    2 = ABC
    3 = DEF
    4 = GHI
    5 = JKL
    6 = MNO
    7 = PQRS (in older telephones, PRS)

    8 = TUV
    9 = WXYZ (in older telephones, WXY)

'''

dikt ={'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6, 'N': 6,
'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

number = input('Enter telephone number:  ')

decoded = ''

for char in number:
    if char.isalpha():
        char = char.capitalize()
        char = dikt[char]
        decoded += str(char)
    else:
        decoded += str(char)

print(decoded)

