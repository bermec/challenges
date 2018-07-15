''' you have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates and put them in a separate string, which yields two separate instances of the string "dailyprogramer".

use this list for testing:

input: "balloons"

expected output: "balons" "lo"

input: "ddaaiillyypprrooggrraammeerr"

expected output: "dailyprogramer" "dailyprogramer"

input: "aabbccddeded"

expected output: "abcdeded" "abcd"

input: "flabby aapples"

expected output: "flaby aples" "bap"


lst2 = ''

test_lst = 'ttree'
try:
    for x in range(len(test_lst) + 1):
        if test_lst[x + 1] == test_lst[x]:
            lst2 += test_lst[x]
            continue
except:
    print(test_lst, lst2)
'''


test_str = 'ball oons'
s = test_str.split()
test_lst_zero = s[0]
test_lst_one = s[1]

# output: 'b' extracts the duplicate
x = 0
strng = ''
while x + 1 <= len(test_lst_zero) - 1:
    if test_lst_zero[x] == test_lst_zero[x + 1]:
        strng += test_lst_zero[x]
    x += 1

# output: 'ap' extracts the duplicate
test_lst2 = s[1]
x = 0
strng2 = ''
while x + 1 <= len(test_lst2) - 1:
    if test_lst2[x] == test_lst2[x + 1]:
        strng2 += test_lst2[x]
    x += 1


print(strng + strng2)

# use the unordered set as a guide to assemble a string
test_lst_set = set(test_lst_zero)
second_string = ''
for x in test_lst_zero:
    if x not in second_string:
        second_string += x

test_lst_set = set(test_lst_one)
third_string = ''
for y in test_lst_one:
    if y not in third_string:
        third_string += y


print(second_string + ' ' + third_string)