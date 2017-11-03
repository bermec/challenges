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
    # counter
    accumulator = 0

    # convert b to a dictionary to cover
    # duplicate letters
    b = dict(enumerate(b))

    # use b as a reference to catalogue a
    a_dict = {}
    for char in a:
        for item in b:
            bval = b[item]
            if b[item] == char:
                # if item not in b_dict:
                a_dict.update({item: bval})
    a = a_dict

    # two numbers for exchanging dict elements
    num_a = random.randrange(0, len(a))
    num_b = random.randrange(0, len(a))

    # exchange the two elements
    a[num_a], a[num_b] = a[num_b], a[num_a]

    while a != b:
        num_a = random.randrange(0, len(a))
        num_b = random.randrange(0, len(a))
        # Swap two dictionary entries
        a[num_a], a[num_b] = a[num_b], a[num_a]

        if a == b:
            return print('{} iterations.'.format(accumulator))
        else:
            accumulator += 1
    return print('{} iterations.'.format(accumulator))

if __name__ == '__main__':
    scrambled = 'lolheworld'
    the_word = 'helloworld'
    bogo(scrambled, the_word)
