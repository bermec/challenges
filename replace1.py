import re
#from string import whitespace
lst = ['0. 0.']
print(len(lst[0]))
print(lst)

for x in range(0, len(lst)):
    temp = ''
    for element in lst[x]:
        if element != ' ':
            temp += element
        lst[x] = temp




print(lst)

string = "0. 0."
string = ''.join(filter(None,string.split(' ')))
print(string)

a = {'0.0':'s'}
b = '0.0'
if b in a:
    print('aye')