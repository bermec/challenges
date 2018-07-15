import re
a = 'XX X'
ans = re.findall('\S{2}|\S', a)
print(ans)
ans = re.findall('\S{3}|\S', a)
print(ans)
