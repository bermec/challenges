import re
a = '456-123'
x = re.findall('^\d+', a)
y = re.findall('\d+$', a)
b = re.sub(x[0], y[0], a)
c = re.sub(y[0], x[0], b)
print(a, b, c, x, y)
