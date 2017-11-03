import re

a = '*-2'
num = re.findall('[-]\d+|\d+', a)
#print(num)

# find '*' but not '-'
ops = re.findall('[^-\d]', a)
#print(ops)

words = '*-5+2-7'
# pick out a neg number preceded by an operator
ans = re.findall('[^\d](-\d)[^\d](\d)[^\d](\d)', words)
print(ans)

# pick out the other numbers
ans2 = re.findall('(\d+)', words)
#print(ans2)

ans2 = re.findall('\d|[^\d](-\d)[^\d]', words)
print(ans2)

str = 'one three two six'
ans3 = re.findall('(?=.*one)(?=.*two)', str)
#print(ans3)

a='''
match 	1 file found?
match 	2 files found?
match 	24 files found?
skip 	No files found.'''

ans = re.findall('\d+files? found\?', a)
print(ans)