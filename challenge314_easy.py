'''
Given a list of integers separated by a single space on standard input,
print out the largest and smallest values that can be obtained by
concatenating the integers together on their own line. This is from Five
programming problems every Software Engineer should be able to solve in l
ess than 1 hour, problem 4. Leading 0s are not allowed (e.g. 01234 is not
a valid entry).

This is an easier version of #312I.
Sample Input

You'll be given a handful of integers per line. Example:

5 56 50

Sample Output

You should emit the smallest and largest integer you can make, per line.
Example:

50556 56550

Challenge Input

79 82 34 83 69
420 34 19 71 341
17 32 91 7 46

Challenge Output

3469798283 8382796934
193413442071 714203434119
173246791 917463217

Bonus

EDIT My solution uses permutations, which is inefficient.
Try and come up with a more efficient approach.
'''

# solution uses a padding-out technique

def selection_sort_low(l):
    '''low to high'''
    for element in range(len(l) - 1, 0, -1):
        max_pos = 0
        for pos in range(1, element + 1):
            if l[pos] > l[max_pos]:
                max_pos = pos
        temp = l[element]
        l[element] = l[max_pos]
        l[max_pos] = temp
    return l


def selection_sort_hi(l):
    '''low to high'''
    for element in range(len(l) - 1, 0, -1):
        max_pos = 0
        for pos in range(1, element + 1):
            if l[pos] < l[max_pos]:
                max_pos = pos
        temp = l[element]
        l[element] = l[max_pos]
        l[max_pos] = temp
    return l


candidates = '''79 82 34 83 69
420 34 19 71 341
17 32 91 7 46'''

candidates = candidates.splitlines()

n = 6 # a suitably large length of number string
dict = {}
mult_list = []
for lst in candidates:
    lst = list(map(int,lst.split()))
    mult_list = []
    for num in lst:
        num = str(num)
        b = num * n
        c = b[:n]
        dict[c] = num
        mult_list.append(c)

    sorted_list = selection_sort_low(mult_list)
    output = ''
    for element in mult_list:
        num = dict[element]
        num = num[:2]
        output += num
    print(output)

    sorted_list = selection_sort_hi(mult_list)
    output = ''
    for element in mult_list:
        num = dict[element]
        num = num[:2]
        output += num
    print(output)




