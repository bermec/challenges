
a = '12345'

#-- create step sequence --------------------------
import itertools
masterlist = []
temp_list = []
N = 5

comb_list = list(itertools.product([1, 2], repeat=N))
for lst in comb_list:
    sum_temp_list = 0
    temp_list = []
    for element in lst:
        temp_list.append(element)
        sum_temp_list = sum(temp_list)
        if sum_temp_list == N:
            masterlist.append(temp_list)
            break
        elif sum_temp_list > N:
            break

output = []
for lst in masterlist:
    if lst not in output:
        output.append(lst)


print(output)




    

