''' Input: a number

Output : the next higher number that uses the same set of digits.

'''

from itertools import permutations

num = input('Enter a number...   ')

lst = set()
for p in permutations(num):
    s = ''
    for char in p:
        s += char
    lst.add(int(s))

lst = list(lst)
lst.sort()
indx = lst.index(int(num))
print(lst[indx + 1])
# ------------------------------------------------

acc = 1
while True:
    lst = sorted(list(num))
    b = int(num) + acc
    lst2 = sorted(list(str(b)))
    if lst == lst2:
        print(b)
        exit()
    acc += 1
    b = 0


