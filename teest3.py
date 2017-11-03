lst = [1, 2, 1, 2, 3]

dict1 = {}

for num in lst:
    dict1[num] = dict1.setdefault(num, 0) + 1
print(dict1)
maximum = max(dict1, key =  dict1.get)
print(maximum)
max2 = [key for key,val in dict1.items() if val == max(dict1.values())]
print(max2)