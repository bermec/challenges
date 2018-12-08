'''
A Latin square is an n × n array filled with n different symbols, each occurring
 exactly once in each row and exactly once in each column.

For example:

    1

And,

    1 2

    2 1

Another one,

    1 2 3

    3 1 2

    2 3 1

In this challenge, you have to check whether a given array is a Latin square.
Input Description

Let the user enter the length of the array followed by n x n numbers. Fill an
array from left to right starting from above.
Output Description

If it is a Latin square, then display true. Else, display false.
Challenge Input

    5

    1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1

    2

    1 3 3 4

    4

    1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1

Challenge Output

    true

    false

    false

Bonus

A Latin square is said to be reduced if both its first row and its first column
are in their natural order.

You can reduce a Latin square by reordering the rows and columns. The example
 in the description can be reduced to this

    1 2 3

    2 3 1

    3 1 2

If a given array turns out to be a Latin square, then your program should reduce
it and display it.


'''

import math


def reduce_me(s):
    """ lst -> str
    Reduce a Latin list """
    for x in range(0, len(s)):
        b = s[x:] + s[:x]
        print(b)


def rows_check(l, check):
    row_check = False
    for lst in l:
        temp = sorted(lst)
        if temp == check:
            row_check = True
        else:
            return False
    return row_check


def columns_check(l, a, check):
    len_a = len(a)
    sqrt_a = int(math.sqrt(len_a))
    column_check = False
    temp_list = []
    for x in range(0, sqrt_a):
        for y in range(0, sqrt_a):
            temp = latin_list[x][y]
            temp_list.append(temp)
        temp_list = sorted(temp_list)
        if temp_list == check:
            column_check = True
            temp_list = []
        else:
            return False
    return column_check


latin_list = []
lst = ['1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1', '1 3 3 4',
     '2 3 4 1 3 2 4 2 3 4 1 4 3 2 1']
for a in lst:
    a = a.split()

    len_a = len(a)
    sqrt_a = int(math.sqrt(len_a))
    acc = 0
    temp = []

    for y in range(0, len_a):
        temp .append(a[y])
        acc += 1
        if acc == sqrt_a:
            latin_list.append(temp)
            temp = []
            acc = 0
    #print(latin_list)

    check = sorted(latin_list[0])
    check_string = ''.join(check)
    #print(check)

    #-- row_check -----------------

    row_check = rows_check(latin_list, check)
    if row_check:
        pass
    else:
        print('Fail')
        continue

    #-- column check ----------------

    column_check = columns_check(latin_list, a, check)
    if column_check:
        reduced = reduce_me(check_string)
        print('Latin!')
    else:
        print('Fail')
        continue

