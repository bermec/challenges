
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
    return strng[::-1]

def palindrome(strng):
    if strng == strng[::-1]:
        return True
    return  False

if __name__ == '__main__':

    print(num_bases(4449, 12))
    print(num_bases(19959694, 35))
    print(num_bases(376609378180550, 29))

    palins = ''
    num = 10858
    for x in range(2, 36):
        check = num_bases(num, x)
        if palindrome(check):
            palins += str(check) + ' '

    print('Palindromes of 10858: ', palins)

    print(num_bases(5, 2))