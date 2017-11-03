import re
a = '1234'
ans = re.findall('\d\d(\d)\d', a)
print(ans)