''' Write a program to solve the sliding window minimum problem using any of the methods possible.
his could be a helpful link.
'''

lst = [1, 2, 3, 4, 5]

for x in range(0, len(lst) - 2):
    print(min(lst[x: x+3]))