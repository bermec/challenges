horiz = '+ ' + '- ' * 3 + '+' + '\n'
mid = [('|' + ' ' * 7 + '|' + '\n') * 2 + '|' + ' ' * 7 + '|']
c = [' ' * 8 + ('|' + '\n'), ' ' * 8 + ('|' + '\n')]
r_bar = ' ' * 8 + '|'
lb = ('|' + '\n') * 3

def mid_section():
    return mid[0]


def horiz_bar():
    return horiz


def right_bar():
    temp = ''
    accum = 1
    while accum <= 4:
        temp += r_bar + '\n'
        accum += 1
    return temp


def left_bar():
    global lb
    return lb


if __name__ == '__main__':

    mid = mid_section()
    h = horiz_bar()
    r = right_bar()
    #print(h)
    l = left_bar()
    #print(l)
    print(mid, h, r)
    pass



