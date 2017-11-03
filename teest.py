#strng = 'abcabcabcabccc'
#strng = 'abbccc'
strng = 'qwertyytrewq'
totals_dict = {}
accum = 1
temp = 0
count = 0

for x in range(0, len(strng)):
    if count == 0:
        temp = x
    try:
        if strng[x] != strng[x + 1]:
            totals_dict[temp] = accum
            accum = 1
            count = 0
            continue
    except IndexError:
        totals_dict[temp] = accum
        accum = 1
        count = 0
        continue
    if count == 0:
        temp = x
    count += 1
    accum += 1

print(totals_dict)

# pull out largest value, if more than one, furthest right.
max_series = max(totals_dict.values())
max_index = max(totals_dict, key=totals_dict.get)
print(max_index, max_series)
print(strng[max_index:max_index + max_series])

key_list = []
the_list = totals_dict.keys()
print(the_list[0])
key_list.append(the_list)
print(key_list)


new_dict = {}
for k,v in totals_dict.items():
    if k == max_index:
        pass

print(new_dict)