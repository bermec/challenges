import re
''' Extract words that do Not immediately precede the characters (usd)'''

a = "lsd100usd101"
ans = re.findall('(?<!usd)\d{3}', a)
print(ans)

''' Extract e that does Not immediately precede s'''
a = 'esetes'
ans = re.findall('(?<!s)e', a)
print(ans)

''' Extract es that are Not immediately preceded by s'''
a = 'eeeseeeteees'
ans = re.findall('(?<!s)e+', a)
print(ans)

a = '78y45t23err44.56vv78j'
ans = re.findall('(?<!.)\d+', a) # note: first number only
print(ans)