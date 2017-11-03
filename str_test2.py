strg = 'ttyuopiriillp'
a = 'tripp'
acc = 0
temp = ''
templ = ''
for y in range(0, len(a)):
    for x in range(0, len(strg)):
        strx = strg[x]
        ay = a[y]
        if strg[x] == a[y]:
            strg = strg[x:]
            temp += a[y]

            if temp == a:
                print('correct')
                break
            else:
                break