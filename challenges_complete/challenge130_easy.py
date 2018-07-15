''' You will be given a string of the for NdM, where N and M are describe above
in the challenge description. Essentially N is the number of times to roll the die,
while M is the number of faces of this die.
N will range from 1 to 100, while M will range from 2 to 100, both inclusively.
This string will be given through standard console input.
Output Description

You must simulate the die rolls N times, where if there is more than one roll
you must space-delimit (not print each result on a separate line). Note that
the range of the random numbers must be inclusive of 1 to M, meaning that a die
with 6 faces could possibly choose face 1, 2, 3, 4, 5, or 6.
Sample Input

2d20
4d6

Sample Output

19 7
5 3 4 6

'''



import re
import random


def extract(code):
    candidates = re.findall('\d+', code)
    return candidates



def rollem(n, m):
    acc = 1
    lst = []
    while acc < n + 1:
        num = random.randint(1, m)
        lst.append(num)
        acc += 1
    return lst

if __name__ =='__main__':
    ans1 = extract('2d20')
    print(ans1)
    ans2 = rollem(int(ans1[0]), int(ans1[1]))

    print(ans2)
    ans1 = extract('4d6')
    print(ans1)
    ans2 = rollem(int(ans1[0]), int(ans1[1]))

    print(ans2)
