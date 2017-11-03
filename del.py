dikt = {}
lst = [5,7,9]

accum = 1
num = 'num'

for visitor in lst:
    dikt[num] = dikt.get(num, []) + [visitor, accum]
    accum += 1

total = 0
for value in dikt.values():
    for x in range(0, len(value), 2):
        total += value[x]
    average = total / value[-1]

print(dikt, average)

