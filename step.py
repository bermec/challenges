import string
import itertools

instr = '85121215'
N = len(instr)

#-- alphabet dictionary -----------------------------------
alpha_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
#print(alpha_dict)

comb_list = []
comb_lista = list(itertools.product([1, 2], repeat=N))
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
for lst in comb_lista:
    if lst not in output:
        comb_list.append(lst)
print(comb_list)


output = ''

starter = 0
temp = ''
coded = ''
output_list = []

for x in range (0, len(comb_list)): # length of code blocks
    starter = 0
    target = comb_list[x]
    for digit in target:
        temp = instr[starter:starter + digit]
        for k,v in alpha_dict.items():
            if int(temp) == v:
                coded = k
                output += coded
                temp = ''
                starter = starter + digit
                break
    output_list.append(output)
    output = ''
print(output_list)
