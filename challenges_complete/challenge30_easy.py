''' Write a program that takes a list of integers and a target number and determines
if any two integers in the list sum to the target number.
If so, return the two numbers. If not, return an indication that no such integers exist.
'''

sample_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target_num = 17
flag = False
for x in range(0, len(sample_list)):
    for y in range(x + 1, len(sample_list)):
        if sample_list[x] + sample_list[y] == target_num:
            print('Numbers found: ', sample_list[x], sample_list[y])
            flag = True

if flag == False:
    print('Not found')