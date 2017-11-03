''' Input: a list

Output: Return the two halves as different lists.

If the input list has an odd number, the middle item can go to any of the list.

Your task is to write the function that splits a list in two halves.

'''

lst = [1, 2, 3, 4, 5]

half_lst = len(lst) // 2

first_lst = []
second_lst = []

for x in range(0, half_lst):
    candidate = lst[x]
    first_lst.append(candidate)

for y in range(0, len(lst)):
    if lst[y] not in first_lst:
        second_lst.append(lst[y])



print(first_lst)
print(second_lst)