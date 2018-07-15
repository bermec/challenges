def quicksort(lst, lst2):
    acc = 0
    while True:
        lst += lst2
        lst2 = []
        for x in range(len(lst) - 2, -1, -1):
            pivot = lst[-1]
            acc += 1
            if acc >= len(lst):
                return lst
            if lst[x] >= pivot:
                temp = lst[x]
                lst.remove(lst[x])
                lst2.append(temp)
                acc = 0

if __name__ == '__main__':
    lst2 = []
    lst= [4, 7, 2, 9, 1]
    ans = quicksort(lst, lst2)
    print(ans)