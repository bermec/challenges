Arrays = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [3, 5, 7, 8, 1, 6, 4, 9, 2],
    [8, 1, 6, 7, 5, 3, 4, 9, 2]
]

for array in Arrays:
    valid = True;

    for i in range(3):
        valid &= (sum(array[0+i*3:3+i*3]) == 15)

    for i in range(3):
        valid &= (sum(array[i::3]) == 15)

    valid &= (sum(array[::4]) == 15)
    valid &= (sum(array[2:-2:2][::-1]) == 15)

    print(valid)