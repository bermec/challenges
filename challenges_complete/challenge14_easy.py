''' Input: list of elements and a block size k or some other variable of your choice

Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.

For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.

'''
lst =[12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]
lst2 = []
for x in range(0, len(lst), 2):
    slice = lst[x:x +2]
    slice.reverse()
    for char in slice:
        lst2.append(char)

print(lst2)