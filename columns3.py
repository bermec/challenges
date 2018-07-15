
lsts = ['1166123333', '14, 15, 16', '17, 18, 19', '1000011112', '13, 14, 15', '16, 17, 18', '19, 20, 21', '22, 23, 24', '25, 26, 27',
        '28, 29, 30', '31, 32, 33', '34, 35, 36']

x = 0
y = x
c = 11
while y < 3:
    temp = lsts[x]
    print('{0:<11}'.format(lsts[x]), end='')
    x += 3
    print('{0:<11}'.format(lsts[x]), end='')
    x += 3
    print('{0:<11}'.format(lsts[x]), end='')
    x += 3
    print('{0:<11}'.format(lsts[x]), end='')
    print('\n')
    y += 1
    x = y

