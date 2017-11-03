'''
A bogo sort is a purposefully inefficient algorithm for sorting a sequence.
Today we will be using this for strings to test for equality.

Here is wikipedias entry for a Bogo-Sort
Inputs & Outputs

Given a scrambled string N and another string M. You must sort N so that
it matches M. After it has been sorted, it must output how many iterations
it took to complete the sorting.
Sample Inputs & Outputs

Input:

Bogo("lolhe","Hello")

Output:

1456 iterations
'''
import random


def bogo(a, b):
    temp = a
    accumulator = 0
    this_bogo = None
    while this_bogo != b:
        c = random.randint(0, len(a)-2)
        pluck_one = a.pop(pluck_one)
        a.append(pluck_one)
        if a == b:
            return print('{} iterations.'.format(accumulator))
        else:
            accumulator += 1
            a = temp


def bogo(a, b):
    temp = a
    accumulator = 0
    this_bogo = None
    while this_bogo != b:
        c = random.randint(0, len(a)-1)
        d = random.randint(0, len(a)-1)
        if c != d:
            a[c], a[d] = a[d], a[c]
            if a == b:
                return print('{} iterations.'.format(accumulator))
            else:
                accumulator += 1
                a = temp
        else:
            continue



if __name__ == '__main__':
    # Bumped up the target to get a
    # satisfying amount of iterations :)
    scrambled = list('lolheorwdl')
    the_word = list('helloworld')
    bogo(scrambled, the_word)
