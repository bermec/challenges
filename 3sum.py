from itertools import permutations

lst = [-7, 4, 6, -1, 2, 1]

for x in range(0, len(lst)):
    candidate = lst[x]
    lst.pop(x)
    perms = list(permutations(lst, 2))
    #print(perms)
    for perm in perms:
        if sum(perm) == abs(candidate):
            print(perm)
exit()