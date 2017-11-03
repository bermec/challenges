test = {'xy':140, 'an': 130, 'xx':140, 'na':130}
'''
results = set()
total = []
candidate = 0
check_set = set()
for key, value in test.items():
    candidate = value


    for key, value in test.items():
        if value == candidate and key not in check_set:
            results.add((key))
            check_set.add(key)
    if len(results) > 0:
        total.append(results)
    results = set()
print(total)

'''

d = {}

for key, value in test.items():
    d[value] = d.get(value, 0) + 1

print(d)
