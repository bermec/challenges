a = 'I have read some text why dont you, you2 will find it worthwhile I hope.'
N = 29
b = ''
'''
acc = 0
for char in a:
    b += char
    kount = len(b)
    if len(b) == N:
        if char == ' ':
            print(b)
        else:
            b = b[::-1]
            while b[0] != ' ':
                b = b[1:]
            b = b[::-1]
            print(b)
            exit()
'''
a = a.split()
#print(a)
for x in range(0, len(a)):
    temp = len(b)
    try:
        if len(a[x + 1]) + len(b) + len(a[x]) <= N:
            b += a[x] + ' '
        else:
            temp = len(b)
            #print(b)
            while len(b) < N:
                b += ' '
            x -= 1
            print(b, end='')
            b = ''
    except IndexError:
        b += a[x] + ' '
        print(b)

