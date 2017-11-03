lines = 'werk-s'
sub = '123456'
linesNew = ''
acc = 0
for i in lines:
    temp = str(i)
    temp2 = temp.replace(i, sub[acc])
    linesNew += temp2
    acc += 1
print(linesNew)

>>>123456