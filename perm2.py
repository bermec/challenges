def insert(lst, n):
    lst = list(lst)
    c = '1'
    lst.insert(n, c)
    return lst

a = '23'
b = a[::-1]
list_a = list(a)
list_b = list(b)
lst = [list_a, list_b]

c = 1
new = []
sett = set()
accum = 0
for element in lst:
    while True:
        for x in range(0, len(element)):
            new.append(element[x])
        else:
            ins_ert = insert(new, accum)
            ins_ert = ''.join(ins_ert)
            sett.add(ins_ert)
            new = []
            accum += 1


print(sett)
