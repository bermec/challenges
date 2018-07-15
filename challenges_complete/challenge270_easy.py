import re
import itertools
holding_list = []

with open('270_text.txt') as f:
    for line in f:
        extract = re.findall('[\s\S]', line.strip('\n'))
        holding_list.append(extract)

zapped = list(map(list, itertools.zip_longest(*holding_list, fillvalue=' ')))
for lst in zapped:
    for item in lst:
        print(item, end='')
    print()