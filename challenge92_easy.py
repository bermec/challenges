'''
Today's easy challenge is to write a program that draws a number
in the terminal that looks like one of those old school seven
segment displays you find in alarm clocks and VCRs. For instance,
if you wanted to draw the number 5362, it would look somthing like:

+--+  +--+  +--+  +--+
|        |  |        |
|        |  |        |
+--+  +--+  +--+  +--+
   |     |  |  |  |
   |     |  |  |  |
+--+  +--+  +--+  +--+

I've added some +'s to the joints to make it a bit more readable,
but that's optional.

Bonus: Write the program so that the numbers are scalable.
In other words, that example would have a scale of 2 (since every
line is two terminal characters long), but your program should
also be able to draw them in a scale of 3, 4, 5, etc.

'''

def mid_section():
    return mid


def horiz_bar():
    return horiz


def right_bar():
    return r_bar


def left_bar():
    return l_bar


def print_helper(num):
    for item in num:
        print(item, end='')

if __name__ == '__main__':

    N = input('size? ')
    N = int(N)

    n = input('number 0 to 9: ')
    n = int(n)

    mid = ('\n' + '|' + ' ' * ((N * 2) + 1) + '|') * N
    horiz = '\n' + '+ ' + '- ' * N + '+'
    r_bar = ('\n' + ' ' * (3 * N - (N - 2)) + '|') * N
    l_bar = '\n' + ('|' + '\n') * (N - 1) + '|'

    one = (l_bar * 2)
    two = (horiz, r_bar, horiz, l_bar, horiz)
    three = (horiz, r_bar, horiz, l_bar, horiz)
    four = (mid, horiz, r_bar)
    five = (horiz, l_bar, horiz, r_bar, horiz)
    six = (horiz, l_bar, horiz, mid, horiz)
    seven = (horiz, r_bar * 2)
    eight = (horiz, mid, horiz, mid, horiz)
    nine = (horiz, mid, horiz, r_bar)
    zero = (horiz, mid * 2, horiz)
    dict_num = {1: one, 2: two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 0:zero}
    num = dict_num[int(n)]

    mid = mid_section()
    h = horiz_bar()
    r = right_bar()
    l = left_bar()

    p = print_helper(num)
    p





