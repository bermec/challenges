''' The population count of a bitstring is the number of set bits (1-bits) in the string.
For instance, the population count of the number 23, which is represented in binary as 10111 is 4.

Your task is to write a function that determines the population count of a number representing a bitstring
'''

import  re

bin_string = ''
num = 5005
#-- calculate the binary number -----------
for x in range(int(num ** 0.5), -1, -1):
    bin_calc = 2 ** x

    if bin_calc <= num:
        bin_string += '1'
        num -= bin_calc
    else:
        bin_string += '0'

#-- a bit over the top, strip leading zeros ---
bin_string = re.sub("^0+","", bin_string)
print(bin_string)
#-- count ones --------------------
one_count = bin_string.count('1')
print(one_count)