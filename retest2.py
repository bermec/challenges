import re

a = '*3+12*2'

b = re.findall('\d+', a)
c = re.findall('[^\d]', a)
print(b, c)

lst = [('a','c'),('f', 'l')]
candidate = ('f', 'l')

test = candidate[0]
test2 = candidate[1]

for x in lst:
    if test and test2 in x:
        print('aye')
