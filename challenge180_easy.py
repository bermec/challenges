''' Description

The Look and Say sequence is an interesting sequence of numbers where
each term is given by describing the makeup of the previous term.

The 1st term is given as 1. The 2nd term is 11 ('one one') because the first term
(1) consisted of a single 1. The 3rd term is then 21 ('two one') because the second term
consisted of two 1s. The first 6 terms are:

1
11
21
1211
111221
312211

Formal Inputs & Outputs
Input

On console input you should enter a number N
Output

The Nth Look and Say number.
Bonus

Allow any 'seed' number, not just 1. Can you find any interesting cases?
'''

def looknsay(a, n):
    print(a)
    a = list(str(a))
    c = ''
    d = ''
    acc = 1
    candidate = a[0]


    while acc < n:
        # equals first character of a[x]
        for x in range(len(a)):
            # new character?
            if a[x] == candidate:
                c += a[x]
            else:
                # add character plus length of string
                d = d + str(len(c)) + c[0]
                # fresh string
                c = ''
                # add character
                c += a[x]
                # set for checking next character
                candidate = a[x]
            # check for last character
            if x == len(a) - 1:
                d = d + str(len(c)) + c[0]
                a = d
                acc += 1
                candidate = d[0]
                print(d)
                c = ''
                d = ''
                break

if __name__ == '__main__':

    ans = looknsay(1, 6)
    ans = looknsay(3, 10)


