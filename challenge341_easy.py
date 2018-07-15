'''
Locate all repeating numbers in a given number of digits.
The size of the number that gets repeated should be more
than 1. You may either accept it as a series of digits
or as a complete number. I shall explain this with examples:

11325992321982432123259

We see that:

    321 gets repeated 2 times

    32 gets repeated 4 times

    21 gets repeated 2 times

    3259 gets repeated 2 times

    25 gets repeated 2 times

    59 gets repeated 2 times

Or maybe you could have no repeating numbers:

1234565943210

You must consider such a case:

9870209870409898

Notice that 987 repeated itself twice (987, 987) and 98
repeated itself four times (98, 98, 987 and 987).

Take a chunk "9999". Note that there are three 99s and two 999s.

9999 9999 9999

9999 9999
'''

import re

results = set()
store = []

#a = '9870209870409898'
#a = '11325992321982432123259'
#a = '9999'
#a = '1234565943210'
a = '11111011110111011'
#a = '1234565943210'

for n in range(2, len(a)):
    for x in range(0, (len(a) - n + 1)):
        slice = a[x: x + n]
        indx = str(x) + ':' + str(x + n)


        slice = a[x: x + n]
        # find all occurances of the slice
        check = re.findall('{0}'.format(slice), a)
        store.append(check)

for lst in store:
    if store.count(lst) >= 2:
        # add to the set to eliminate duplicates
        results.add(str(lst[0]) + ': ' + str(store.count(lst)))

for item in results:
    print(item)

