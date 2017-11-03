''' You will be given many unsigned integers.
Output:

Find the repeats and remove them. Then display the numbers again.
Example:

Say you were given:

    1 1 2 2 3 3 4 4

Your output would simply be:

    1 2 3 4

Challenge Inputs:
1:

3 1 3 4 4 1 4 5 2 1 4 4 4 4 1 4 3 2 5 5 2 2 2 4 2 4 4 4 4 1
2:

65 36 23 27 42 43 3 40 3 40 23 32 23 26 23 67 13 99 65 1 3
65 13 27 36 4 65 57 13 7 89 58 23 74 23 50 65 8 99 86 23 78
89 54 89 61 19 85 65 19 31 52 3 95 89 81 13 46 89 59 36 14
42 41 19 81 13 26 36 18 65 46 99 75 89 21 19 67 65 16 31 8
89 63 42 47 13 31 23 10 42 63 42 1 13 51 65 31 23 28
'''


def clean_up(strng):
    ''' str -> set
    convert string to set of integers
    A set removes duplicates
    '''
    sett = set()
    temp = strng.split()
    for x in temp:
        sett.add(x)
    strng2 = print_set(sett)
    return strng2


def print_set(the_set):
    ''' set -> string
    convert the set for display
    '''
    output = ''
    # set to list and sort
    lst2 = sorted(list(the_set))
    # iterate list for correct display
    for x in range(0, len(lst2)):
        output += lst2[x] + ' '
    return output

if __name__ == '__main__':

    ans = clean_up('1 1 2 2 3 3 4 4')
    print(ans)
    ans = clean_up('3 1 3 4 4 1 4 5 2 1 4 4 4 4 1 4 3 2 5 5 2 2 2 4 2 4 4 4 4 1')
    print(ans)
    ans = clean_up('65 36 23 27 42 43 3 40 3 40 23 32 23 26 23 67 13 99 65 1 3 \
    65 13 27 36 4 65 57 13 7 89 58 23 74 23 50 65 8 99 86 23 78 \
    89 54 89 61 19 85 65 19 31 52 3 95 89 81 13 46 89 59 36 14 \
    42 41 19 81 13 26 36 18 65 46 99 75 89 21 19 67 65 16 31 8 \
    89 63 42 47 13 31 23 10 42 63 42 1 13 51 65 31 23 28')
    print(ans)