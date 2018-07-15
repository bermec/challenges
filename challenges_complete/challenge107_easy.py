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
    comb_list2 = convert(comb_list, N)
    for lst in comb_list2:
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


def convert(l, N):
    '''shorten list of tuples to list of lists
    of sum eight '''
    lst2 = []
    output_list = []
    for tup in l:
        lst2 = []
        for element in tup:
            while sum(lst2) < N:
                lst2.append(element)
                break
        if sum(lst2) == N:
            output_list.append(lst2)
    return output_list

def letter_sequence(strng, N):
    '''apply the string to the slices'''
    combin = ''
    combin_set = set()
    chunks = slicer(N)
    for x in range(0, len(chunks)):
        #list of indices to work with
        indice_list = chunks[x]
        accum = 0
        y = 0
        while accum < len(indice_list):
            second_indice = indice_list[accum] + y
            slice = strng[y:second_indice]
            if int(slice) > 27:
                break
            y = second_indice
            accum += 1

            a_dict = alphabet_dict()
            for k, v in a_dict.items():
                if v == int(slice):
                    sliced = k
                    combin += sliced
                    break
        if len(combin) > 0:
            combin_set.add(combin)
        combin = ''
    return combin_set


if __name__ == '__main__':
    strng = '85121215'
    N = len(strng)
    ans = letter_sequence(strng, N)
    print(ans)