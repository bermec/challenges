lst = [1, 1, 2, 2, 2, 2, 1]
lst2 = []
for element in lst:
    while sum(lst2) < 8:
        lst2.append(element)
        break

print(lst2)