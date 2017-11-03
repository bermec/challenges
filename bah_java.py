import re
from collections import _count_elements

with open('holmes.txt') as f:
    the_text = f.read().lower()
    text_lst = re.findall('\w+', the_text)
    print(text_lst)
#sett = set()

dikt = _count_elements()
#for word in text_lst:
    #sett.add(word)

#sett = list(sett)
for item in text_lst:
    dikt.update
for x in range(0, len(sett)):
    dikt[sett[x]] = text_lst.count(sett[x])

print(dikt)

dikt2 = sorted(dikt.items(), key = itemgetter(1))[::-1]
print(dikt2)