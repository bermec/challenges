import re
line = '10 101010'
ans = re.findall('(?<=\s)[\d+]*', line)
print(ans)