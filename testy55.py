import re

b = ['1434', '25 4', '3634']
a = re.findall('\d{4}|\d{3}|\d{2}|\d', b)
temp = ''
lst = []
for x in range(0, len(a[0])):
    for y in range(0, len(a)):

        char = a[y][x]
        temp += char
    lst.append(temp)
    temp = ''
print(lst)

b = '1  \\**+'
b = b.ljust(10, ' ')
print(b)