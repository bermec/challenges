'''
Consider the translation from letters to numbers a -> 1 through z -> 26.
Every sequence of letters can be translated into a string of numbers
this way, with the numbers being mushed together. For instance
hello -> 85121215. Unfortunately the reverse translation is not unique.
85121215 could map to hello, but also to heaubo. Write a program that,
given a string of digits, outputs every possible translation back to letters.

Sample input:

123

Sample output:

abc

aw

lc
'''

import string
import itertools


def alphabet_dict():
    #-- alphabet dictionary -----------------------------------
    alpha_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
    return alpha_dict


def slicer(N):
    '''gives usable slices of one
    or two to cut up the string'''
    masterlist = []
    temp_list = []
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
    return output


def cull_comb_list(l, N):
    corrected = []
    sample = []
    for x in range(0, len(l)):
        sample = []
        for y in l[x]:
            sample.append(y)
            if sum(sample) == N:
                corrected.append(sample)
                print(sample)
            else:
                continue
    return corrected


def letter_sequence(s, N):
    '''apply the string to the slices'''
    combin = ''
    combin_list = []
    chunks = cull_comb_list(l,N)
    for x in range(0, N):
        indice = chunks[x]
-        for y in range(0, len(indice)):
            slice = strng[y:y + indice[y]]
            a_dict = alphabet_dict()
            for k, v in a_dict.items():
                if v == int(slice):
                    sliced = k
                    combin += sliced
                    break
        combin_list.append(combin)
        combin = ''
    return combin_list


if __name__ == '__main__':
    strng = '85121215'

    N = len(strng)
    l = slicer(N)
    ans = letter_sequence(strng, N)
    print(ans)