'''
Scrabble is a popular word game where players remove tiles with letters on them from
a bag and use them to create words on a board. The total number of tiles as well as
the frequency of each letter does not change between games.

For this challenge we will be using the tile set from the English edition, which has
100 tiles total. Here's a reference for the distribution and point value of each tile.

Each tile will be represented by the letter that appears on it, with the exception
that blank tiles are represented by underscores _.
Input Description

The tiles already in play are inputted as an uppercase string. For example,
if 14 tiles have been removed from the bag and are in play, you would be given
an input like this:

AEERTYOXMCNB_S

Output Description

You should output the tiles that are left in the bag. The list should be in descending
order of the quantity of each tile left in the bag, skipping over amounts that have no tiles.

In cases where more than one letter has the same quantity remaining, output those letters
in alphabetical order, with blank tiles at the end.

10: E
9: I
8: A
7: O
5: N, R, T
4: D, L, U
3: G, S
2: F, H, P, V, W
1: B, C, J, K, M, Q, Y, Z, _
0: X

If more tiles have been removed from the bag than possible, such as 3 Qs, you should give a
helpful error message instead of printing the list.

Invalid input. More Q's have been taken from the bag than possible.

Challenge Inputs

    PQAREIOURSTHGWIOAE_

    LQTOONOEFFJZT

    AXHDRUIOR_XHJZUQEE

Challenge Outputs

1.

10: E
7: A, I
6: N, O
5: T
4: D, L, R
3: S, U
2: B, C, F, G, M, V, Y
1: H, J, K, P, W, X, Z, _
0: Q

2.

11: E
9: A, I
6: R
5: N, O
4: D, S, T, U
3: G, L
2: B, C, H, M, P, V, W, Y, _
1: K, X
0: F, J, Q, Z

3.

Invalid input. More X's have been taken from the bag than possible.

Bonus

After the normal output, output the distribution of tiles in play and the
total point score of both sets of tiles.
'''
'''
letter_dict = {10: 'E',
                9: I,
                8: A,
                7: O,
                5: (N, R, T),
                4: (D, L, U),
                3: (G, S),
                2: (F, H, P, V, W),
                1: (B, C, J, K, M, Q, Y, Z, _ ),
                0: X}'''

#print(letter_dict)

'''
Scrabble is a popular word game where players remove tiles with letters on them from
a bag and use them to create words on a board. The total number of tiles as well as
the frequency of each letter does not change between games.

For this challenge we will be using the tile set from the English edition, which has
100 tiles total. Here's a reference for the distribution and point value of each tile.

Each tile will be represented by the letter that appears on it, with the exception
that blank tiles are represented by underscores _.
Input Description

The tiles already in play are inputted as an uppercase string. For example,
if 14 tiles have been removed from the bag and are in play, you would be given
an input like this:

AEERTYOXMCNB_S

Output Description

You should output the tiles that are left in the bag. The list should be in descending
order of the quantity of each tile left in the bag, skipping over amounts that have no tiles.

In cases where more than one letter has the same quantity remaining, output those letters
in alphabetical order, with blank tiles at the end.

10: E
9: I
8: A
7: O
5: N, R, T
4: D, L, U
3: G, S
2: F, H, P, V, W
1: B, C, J, K, M, Q, Y, Z, _
0: X

If more tiles have been removed from the bag than possible, such as 3 Qs, you should give a
helpful error message instead of printing the list.

Invalid input. More Q's have been taken from the bag than possible.

Challenge Inputs

    PQAREIOURSTHGWIOAE_

    LQTOONOEFFJZT

    AXHDRUIOR_XHJZUQEE

Challenge Outputs

1.

10: E
7: A, I
6: N, O
5: T
4: D, L, R
3: S, U
2: B, C, F, G, M, V, Y
1: H, J, K, P, W, X, Z, _
0: Q

2.

11: E
9: A, I
6: R
5: N, O
4: D, S, T, U
3: G, L
2: B, C, H, M, P, V, W, Y, _
1: K, X
0: F, J, Q, Z

3.

Invalid input. More X's have been taken from the bag than possible.

Bonus

After the normal output, output the distribution of tiles in play and the
total point score of both sets of tiles.
'''

a_list = '''A - 9 tiles
B - 2 tiles
C - 2 tiles
D - 4 tiles
E - 12 tiles
F - 2 tiles
G - 3 tiles
H - 2 tiles
I - 9 tiles
J - 1 tile
K - 1 tile
L - 4 tiles
M - 2 tiles
N - 6 tiles
O - 8 tiles
P - 2 tiles
Q - 1 tile
R - 6 tiles
S - 4 tiles
T - 6 tiles
U - 4 tiles
V - 2 tiles
W - 2 tiles
X - 1 tile
Y - 2 tiles
Z - 1 tile
_ - 2 tiles'''
# form into list of strings
a_list = a_list.splitlines()
alpha_dict = {}
print(a_list)
import re

for line in a_list:
    # tile
    tile = re.findall('^\w|^\W', line)
    # number of tiles
    num = re.findall('\d+', line)
    # convert into dictionary
    alpha_dict[tile[0]] = int(num[0])

letters = 'PQAREIOURSTHGWIOAE_'

# calculate remaining tiles
for letter in letters:
    alpha_dict[letter] -= 1
    if alpha_dict[letter] < 0:
        print('Invalid input, more ' + letter + '\'s ' + 'have been taken than possible.')
        continue

# sort data for display
import operator

sorted_data = sorted(alpha_dict.items(), key=operator.itemgetter(1), reverse=True)

output_num = 0
codes = ''

for x in range(12, -1, -1):
    for d in sorted_data:
        if d[1] == x:
            output_num = d[1]
            codes += d[0]
    if codes != '':
        codes = list(codes)
        print(str(output_num) + ': ' + ', '.join(codes))
        codes = ''

