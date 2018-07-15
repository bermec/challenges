def main(file, n, grid):
    lst = []
    with open(file) as f:
        for line in f:
            line = line.split()
            for num in line:
                num = int(num)
                lst.append(num)

    while n > 0:
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
    lst[x] = str(lst[x])
    print(lst[x].ljust(4), end= '')
    return n

if __name__ == '__main__':

    ans = main('217_200_4.txt', 200, 4)
    print()
    print("Answer:", ans)

    ans = main('217_41_1.txt', 41, 1)
    print()
    print("Answer:", ans)

    ans = main('217_2048_15.txt', 2048, 15)
    print()
    print("Answer:", ans)

    ans = main('217_10000_12.txt', 10000, 12)
    print()
    print("Answer:", ans)


