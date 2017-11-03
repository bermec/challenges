import re
''' Extract words that immediately precedes the match'''

a = "usd100"
ans = re.findall('(?<=usd)\d{3}', a)
print(ans)
# ['100']

''' Extract e that immediately precedes s'''
a = 'esetes'
ans = re.findall('(?<=s)e', a)
print(ans)
# ['e']

''' Extract es that immediately preceded by s'''
a = 'eeeseeeteees'
ans = re.findall('(?<=s)e+', a)
print(ans)
# ['eee'] after s