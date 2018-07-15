''' Write a function that given two sorted lists,
returns a list whith the two lists merged together into one sorted list.

So, for instance, for inputs [1,5,7,8] and [2,3,4,7,9] it should return [1,2,3,4,5,7,7,8,9].

Try and make your code as efficient as possible.

'''

lst1 = [1, 5, 7, 8]
lst2 = [2, 3, 4, 7, 9]
lst3 = []

import itertools
for item in itertools.chain(lst1, lst2):
    lst3.append(item)

print(sorted(lst3))