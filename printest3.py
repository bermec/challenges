

def mid_section():
    return mid


def horiz_bar():
    return horiz


def right_bar():
    return r_bar


def left_bar():
    return lb


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
    r_bar = ('\n' + ' ' * (3 * N) + '|') * N
    lb = '\n' + ('|' + '\n') * (N - 1) + '|'
    one = (lb * 2)
    two = (horiz, r_bar, horiz, lb, horiz)
    three = (horiz, r_bar, horiz, lb, horiz)
    four = (mid, horiz, r_bar)
    five = (horiz, lb, horiz, r_bar, horiz)
    six = (horiz, lb, horiz, mid, horiz)
    seven = (horiz, r_bar * 2)
    eight = (horiz, mid, horiz, mid, horiz)
    nine = (horiz, mid, horiz, r_bar)
    zero = (horiz, mid * 2, horiz)
    dict_num = {1: one, 2: two}
    num = dict_num[int(n)]
    p = print_helper(num)
    p






    mid = mid_section()
    h = horiz_bar()
    r = right_bar()
    l = left_bar()



    #ans = print_helper(zero)
    #ans


