
N = 5
holding_list = []
pascal_triangle = [1]
holding_list.append(pascal_triangle)
next_row = []
accum = 0

while accum <= N:
    next_row = []
    for x in range(0, len(pascal_triangle) + 1):
        try:
            test1 = pascal_triangle[x]
            test2 = 0
            if x - 1 == -1:
                test2 = 0
            else:
                test2 = pascal_triangle[x - 1]
            num = test1 + test2
        except IndexError:
            num = 1
        next_row.append(num)
    holding_list.append(next_row)
    print(next_row)
    pascal_triangle = next_row
    accum += 1