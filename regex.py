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