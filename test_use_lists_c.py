'''
This programming challenge is a classic interview question for software engineers:
given a string, find the longest sub-string that contains, at most, two characters.

Author: /u/Regul
Formal Inputs & Outputs
Input Description

Through standard console input, you will be given a string to search, which only
contains lower-case alphabet letters.
Output Description

Simply print the longest sub-string of the given string that contains, at most, two
unique characters. If you find multiple sub-strings that match the description,
print the last sub-string (furthest to the right).
Sample Inputs

abbccc
abcabcabcabccc
qwertyytrewq

Sample Outputs

bbccc
bccc
tyyt
'''

#strng = 'abcabcabcabccc'
#strng = 'abbccc'
#strng = 'qwertyytrewq'
#strng = 'abcdef'
strng ='aabbce'

def sub_string(strng):
    indexes = []
    totals = []
    accum = 1
    temp = 0
    count = 0

    for x in range(0, len(strng)):
        if count == 0:
            temp = x
        try:
            one = strng[x]
            next = strng[x+1]
            if strng[x] != strng[x + 1]:
                indexes.append(temp)
                totals.append(accum)
                accum = 1
                count = 0
                continue
        except IndexError:
            indexes.append(temp)
            totals.append(accum)
            accum = 1
            count = 0
            continue
        if count == 0:
            temp = x
        count += 1
        accum += 1

    '''pull out largest value, if more than one, 
    furthest right.'''
    # largest series
    max_series = (max(totals))

    # index of the largest series
    indx = totals.index(max_series)

    # indexes of series either side
    try:
        indexes_of_interest = indexes[indx-1], indexes[indx], indexes[indx+1]
        indexes_of_interest = list(indexes_of_interest)
    except IndexError:
        indexes_of_interest = indexes[indx-1], indexes[indx]

    # if string totals all the same
    if totals[1:] == totals[:-1]:
        indexes_of_interest = indexes[-2:]

    output = ''
    if len(indexes_of_interest) == 2:
         for x in indexes_of_interest:
             num = totals[indexes.index(x)]
             output += strng[x:x + num]
    elif strng[indexes_of_interest[0]] == strng[indexes_of_interest[2]]:
        for x in indexes_of_interest:
            num = totals[indexes.index(x)]
            output += strng[x:x + num]
    elif totals[indexes_of_interest[0]] > totals[indexes_of_interest[2]]:
        indexes_of_interest.pop(2)
        for x in indexes_of_interest:
            num = totals[indexes.index(x)]
            output += strng[x:x + num]
    else:
        indexes_of_interest.pop(0)
        for x in indexes_of_interest:
            num = totals[indexes.index(x)]
            output += strng[x:x + num]
    return output


if __name__ == '__main__':

    candidates = ['abcabcabcabccc', 'abbccc', 'qwertyytrewq', 'abcdef', 'aabbc']
    output = []

    for candidate in candidates:
        ans = sub_string(candidate)
        output.append(ans)

    print(output)







