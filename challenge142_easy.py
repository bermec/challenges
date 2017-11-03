'''
Falling-sand Games are particle-simulation games that focus on the interaction
between particles in a 2D-world. Sand, as an example, might fall to the ground
forming a pile. Other particles might be much more complex, like fire, that
might spread depending on adjacent particle types.

Your goal is to implement a mini falling-sand simulation for just sand and
stone. The simulation is in 2D-space on a uniform grid, where we are viewing
this grid from the side. Each type's simulation properties are as follows:

    Stone always stays where it was originally placed. It never moves.
    Sand keeps moving down through air, one step at a time, until it either
    hits the bottom of the grid, other sand, or stone.

Formal Inputs & Outputs
Input Description

On standard console input, you will be given an integer N which represents
the N x N grid of ASCII characters. This means there will be N-lines of
N-characters long. This is the starting grid of your simulated world: the
character ' ' (space) means an empty space, while '.' (dot) means sand,
and '#' (hash or pound) means stone. Once you parse this input, simulate
the world until all particles are settled (e.g. the sand has fallen and
either settled on the ground or on stone). "Ground" is defined as the solid
surface right below the last row.
Output Description

Print the end result of all particle positions using the input format for particles.
Sample Inputs & Outputs
Sample Input

5
.....
  #
#

    .

Sample Output

  .
. #
#
    .
 . ..

'''

import random
#N = input('Input size of grid: ')
N = 8
sqrN = N ** 2


# construct list length
lst = [' '] * N ** 2

# first layer of '*'
for index in range(0, N):
    lst[index] = '.'

# use random to find sand and brick indexes
acc = N
while acc < sqrN:
    num = (random.randrange(N)) + acc
    lst[num] = random.choice(['#', '.'])
    acc += N

# arrange list into columns
index_list = []
acc = 0
while acc < N:
    for x in range(0 + N, N * N-1, N):
        ans = x + acc
        index_list.append(ans)
    acc += 1

# index_list into list of lists
lst_split = [index_list[i:i + (N - 1)] for i in range(0, len(index_list), N - 1)]

# let it rain
accum = 0
while accum < N:
    for y in range(0, len(lst_split)):
        for x in range(0, len(lst_split[y])):
            indx = lst_split[y][x]
            test = lst[indx]
            if test == ' ':
                if lst[indx - N] == '.':
                    lst[indx], lst[indx - N] = lst[indx - N], lst[indx]
    accum += 1

# print out resulting list in blocks
acc = 1
for x in range(0, N * N):
    if acc == N:
        print(lst[x])
        acc = 1
    else:
        print(lst[x], end='')
        acc += 1

