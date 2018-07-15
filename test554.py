
import re
a = '*\*/'

b = re.findall('\S{10|\S{9}|\S{8}|\S{7}|\S{6}|\S{5}|\S{4}|\S{3}|\S{2}|\S{1}', a)
print(b, len(b[0]))



b = re.findall('\S{4}', a)
print(b, len(b[0]))


'''a = [['1'], ['1', '1']]
b = ''
c = []
for lst in a:
    for item in lst:
        b += item
    b = b.rjust(2, ' ')
    c.append(b)
    b = ''
print(c)'''