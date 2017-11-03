lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
N = 3
lst_split = [lst[i:i + N] for i in range(0, len(lst), N)]

for x in range(0, len(lst_split)):
    for y in range(0, len(lst_split)):
        num = strs[lst_split[x][y]]
        num1 = strs[lst_split[x][y + 1]]
        print(num, num1)

        num, num1 = num1, num
        print(strs)