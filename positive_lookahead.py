import re
''' Extract words that are Immediately preceded by a comma'''

a = "What then, said I, shall I do?  You shan't, he replied, do anything."
ans = re.findall('[A-Za-z\']+(?=,)', a)
print(ans)
# ['then', 'I', 'shan't', 'replied']

''' Extract \w+ that is immediately preceded by \sBrown'''
a = 'Jim Brown'
ans = re.findall('\w+(?=\sBrown)', a)
print(ans)

''' Extract es that are immediately preceded by s'''
a = 'eeeseeeteees'
ans = re.findall('e+(?=s)', a)
print(ans)