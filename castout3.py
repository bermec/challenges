a = 'I have read some text why dont you, you2 will find it worthwhile I hope.'
N = 29
b = ''
a = a.split()
x = 0
while True:
    temp = len(b)
    try:
        if len(a[x + 1]) + len(b) + len(a[x]) <= N:
            b += a[x] + ' '
            x += 1
        else:
            temp = len(b)
            #print(b)
            while len(b) < N:
                b += ' '
            print(b, end='')
            b = ''
    except IndexError:
        b += a[x] + ' '
        print(b)
        exit()

