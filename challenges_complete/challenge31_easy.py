''' Write a function that takes two base-26 numbers in which digits are represented by letters
 with A=0, B=1, … Z=25 and returns their product using the same notation. As an example, CSGHJ × CBA = FNEUZJA.

Your task is to write the base-26 multiplication function.

Try to be very efficient in your code!

I have converted to base 10, multiplied and converted back to base 26.
'''

dikt ={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 0}

def invert_dict(d):
    return {v:k for k, v in dikt.items()}


def alpha_to_num(strng):
    ''' str -> int '''

    acc = 0
    lst1 = list(strng)
    lst1 = lst1[::-1]
    for x in range(0, len(lst1)):
        item = lst1[x]
        n = dikt[item]# * 26 ** x
        acc += n
    return  acc


def num_to_alpha(n):
    '''  int -> tuple '''
    b = None
    lst = []
    while b != 0:
        a = n // 26
        b = n % 26
        lst.append(b)
        n = a
    return lst


def decode(lst):
    '''  list -> str '''
    global inv_dict
    strng = ''
    lst.pop()
    lst = lst[::-1]

    for item in lst:
        strng += inv_dict[item]
    return  strng



if __name__ == '__main__':

    string1 = input('Enter first number to be multiplied:  ')
    string2 = input('Enter second..:  ')
    inv_dict = invert_dict(dikt)
    string1 = string1.upper()
    string2 = string2.upper()
    num1 = alpha_to_num(string1)
    num2 = alpha_to_num(string2)
    num3 = num1 * num
    alfa = num_to_alpha(num3)
    result = decode(alfa)

    print('Answer =   ', result)




