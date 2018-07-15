'''import re

results = []

a = '1234241234'
for n in range(2, len(a) // 2):
    for x in range(0, (len(a)- 1)//2):
        slice = a[x: x + n]
        check = re.findall('{0}'.format(slice), a)
        if check.count(check[0]) >= 2:
            results.append(str(check[0]) + ': ' + str(check.count(check[0])))
print(results)'''


s = [['99', '99'], ['99', '99']]

n = s.count(s[0])
pass
