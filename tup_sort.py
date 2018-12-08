l = [1, 4, 3, 15, 5]
ll = list(enumerate(l))
lst = []
for tup in ll:
    tup = tup[::-1]
    lst.append(tup)

lst = sorted(lst)
n = 0
for x in range(0, len(lst) - 1):
    if lst[x + 1][0] == lst[x][0] + 1:
            m = lst[x + 1][1] - lst[x][1]
            n += 1


print(n)