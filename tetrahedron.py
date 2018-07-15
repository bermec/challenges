def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def pyramid(N, N2, y, z):
    column = []
    for x in range(0, N2):
        ans = int(factorial(N) / (factorial(y) * factorial(x) * factorial(z)))
        column.append(ans)
        y -= 1
    return column


if __name__ == '__main__':

    holding_list = []

    N = 5
    y = N
    z = 0
    N2 = N + 1
    column1 = pyramid(N, N2, y, z)
    holding_list.append(column1)

    y = N
    y -= 1
    z += 1
    N2 = N
    column2 = pyramid(N, N2, y, z)
    holding_list.append(column2)

    y = N
    y -= 2
    z += 1
    N2 = N - 1
    column3 = pyramid(N, N2, y, z)
    holding_list.append(column3)


    y = N
    y -= 3
    z += 1
    N2 = N - 2
    column4 = pyramid(N, N2, y, z)
    holding_list.append(column4)


    y = N
    y -= 4
    z += 1
    N2 = N - 3
    column5 = pyramid(N, N2, y, z)
    holding_list.append(column5)


    y = N
    y -= 5
    z += 1
    N2 = N - 4
    column6 = pyramid(N, N2, y, z)
    holding_list.append(column6)

    holding_list = list(reversed(holding_list))
    for lst in holding_list:
        for num in lst:
            print(num, ' ', end='')
        print('\n')




