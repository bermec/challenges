

def hexAdd(a, b):
    x = int(a, 16)
    y = int(b, 16)
    z = x + y
    return hex(z)[2:]


if __name__ == '__main__':

    ans = hexAdd('f', 'f')
    print(ans)