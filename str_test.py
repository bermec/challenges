strg = 'ttyuopiriillp'

a = 'tripp'
acc = 0
temp = ''
templ = ''
for x in range(0, len(strg)):
    if templ == a[acc]:
        temp += templ
        acc += 1
        continue
    if strg[x] == a[acc]:

        temp += a[acc]
        acc += 1
        templ = strg[x]
        if temp == a:
            print('correct')
            break