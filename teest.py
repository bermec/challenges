'''
a = [' ', '', ' ', (4, 'x')]
b = a[::-1]
print(b)
lenb= len(b)
for x in b:
    try:
        print(x[0] * x[1])
    except:
        continue

a = [' ', '', ' ', (4, 'x')]
b = a[::-1]

lenb= len(b) - 1
for x in range(lenb, -1, -1):
    try:
        print(b[x][0] * b[x][1])
    except:
        continue
        '''

a = ['  4 5', '12345']
b = ''
c = []
for x in range(0, 5):
    print(a[0][x], end='')
    print('{: >2}'.format(a[1][x]))


m = ['12345', '67890']
n = []
for strng in m:
    strng = strng[2:]
    n.append(strng)

print(n)

a = ['1']
while len(a) < 3:
    a.insert(0, ' ')



