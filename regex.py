import re

a = 'm11uu2v.'


b = re.findall('\w\.$', a)
c = re.findall('^\w', a)

print(b, c)

#['v.']
#['m']
stuff = 'From rog@repairman.com'

ans = re.findall('From .*@([^ ]*)', stuff)
print(ans)

# format:

n = '154.3210'
d = '\d'
num = 1
d_s = d * num
ans = re.findall('\d+\.' + d_s, n)
print(ans)