import re

alpha_string = 'abcdefghijklmnopqrstuvwxyz'
f = ['test', 'tesd']
cand = 'test'
x = re.findall('^([a-z]{3})', cand)
y = re.findall('\w([a-z]{3})', cand)
z = re.findall('(\d)\d(\d+)', cand)

print(x)

for letter in alpha_string:
    ans = x[0] + letter
    if ans in f:
        print(ans)

ans = re.sub('e(?<=\w)','z', f[0])
print(ans)
'''
a = 'test'
regex = re.findall('\a', x, a)
print(regex)
'''