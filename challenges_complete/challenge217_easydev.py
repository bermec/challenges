

def piles(file, n, grid):
    lst = []
    with open(file) as f:
        for line in f:
            line = line.split()
            for num in line:
                num = int(num)
                lst.append(num)



    least = min(lst)
    for x in range(0, len(lst)):
        if lst[x] == least:
            lst[x] += 1
            n -= 1
            if n >= 0:
                break
            least = min(lst)


    for x in range(0, len(lst)):
        if x > 0:
            if x % grid == 0:
                lst[x] = str(lst[x])
                print(lst[x])
            else:
                lst[x] = str(lst[x])
                print(lst[x].ljust(4), end= '')
    print(lst[x].ljust(4), end= '')


if __name__ == '__main__':
     ans = piles('217_200_4.txt', 200, 4)
