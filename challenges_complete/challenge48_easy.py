''' Take an array of integers and partition it so that all the even integers
in the array precede all the odd integers in the array. Your solution must
take linear time in the size of the array and operate in-place
with only a constant amount of extra space.

Your task is to write the indicated function.

'''

a = [9, 7, 98, 89, 4, -7, 6, 44,-90, 66, 55, 81, 14]

for x in range(len(a) - 1, -1, -1):
    if a[x]%2 == 1:
        b = a.pop(x)
        a.append(b)


print(a)