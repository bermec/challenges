
import re
'''
words = '*-5=3-8*-5'
# pick out a neg number preceded by an operator
ans = re.findall('([^\d](-\d)[^\d](\d)[^\d](\d))|(^\d](-\d))', words)
ans2 = re.findall('[^\d](-\d)|(\d)', words)

print(ans)
print(ans2)
'''
words = '*-5+4-3'
ans3 = re.findall('\W(-\d)|(\d)', words)

print('ans3: ', ans3)
strng = ''
for x in range(0, len(ans3)):
    for y in range(0, 2):
        temp = ans3[x][y]
        if temp != '':
            strng += temp + ','
s = strng.split()

print(s)
print(s[0], s[1], s[2])