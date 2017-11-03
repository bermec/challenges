'''
A number of sailors (let's call it N) are stranded on an island with a huge pile of coconuts and a monkey.
During the night, each sailor (in turn) does the following without the others knowing:

    He takes one N'th (e.g. if N=5, one fifth) of the coconuts in the pile and hides them
    The division leaves one coconut left over, which is given to the monkey.

In the morning, they split the remaining coconuts between them. This time the split is even.
There's nothing left over for the monkey.

Your task: Given the number of sailors (N), how many coconuts were in the pile to begin with
(lowest possible number)?

Formal inputs/outputs
Input

The input is a single number: N, the number of sailors.
This number is a whole number that is greater than or equal to 2.
Output

The output is a single number: the number of coconuts in the original pile.
Sample input/output

Input:

5

Output:

3121

Sample solution for 5 sailors: https://jsfiddle.net/722gjnze/8/
'''

''' Due to the maths being beyond my pay grade I
have ported a javascript file to python 3'''


def transaction(n):
    return (n - 1) / 5 * 4

def is_correct(n):
    for var in range(0, 5):
        if n % 5 != 1:
            return False
        n = transaction(n)
    return n % 5 == 0

LIMIT = 1000000
i = 1
while i < LIMIT and not is_correct(i):
    i += 1
print("The answer is: %s" % i)