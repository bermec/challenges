import re
b_s = []
a = ['0', '01', '10001100']
for b in a:
    s = re.findall('([0]+)\d', b)
    b_s.append(s)
print(b_s)

a = '-14x^1'
b = re.findall('^[+-]\d+|^\d+', a)
print(b)
c = '2x -3'
d = re.findall('[+-]\d+$|\d+$', c)
print(d)

e = re.findall('\S\^\d+', a)
print(e)