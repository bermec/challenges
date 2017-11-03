import re
''' Extract words that do not follow a comma'''

a = "What then, said I, shall I do?  You shan't, he replied, do anything."
ans = re.findall('[A-Za-z\']+(?!,)', a)
print(ans)

''' Extract e that does not follow s'''
a = 'esetes'
ans = re.findall('e(?!s)', a)
print(ans)

''' Extract es that are not followed by s'''
a = 'eeeseeeteees'
ans = re.findall('e+(?!s)', a)
print(ans)