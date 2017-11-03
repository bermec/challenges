

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





