''' Write a function that takes two arguments, x and y,
which are two strings containing Roman Numerals without prefix subtraction
(so for instance, 14 is represented as XIIII, not XIV). The function must
return true if and only if the number represented by x is less than the number
represented by y. Do it without actually converting the Roman numerals into regular numbers.

Challenge: handle prefix subtraction as well.
'''

__name__ == '__main__'

def RomanCompare(x, y):

    roman_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    for z in range(0, len(roman_list)):
        xcount = x.count(roman_list[z])
        ycount = y.count(roman_list[z])
        if xcount > ycount:
            return True
        else:
            return False
    

if __name__ == '__main__':
    ans = RomanCompare('MLL', 'MLL')
    print(ans)