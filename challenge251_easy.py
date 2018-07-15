'''
    Nonograms, also known as Hanjie, Picross or Griddlers, are picture logic puzzles in
    which cells in a grid must be colored or left blank according to numbers at the
    side of the grid to reveal a hidden picture. In this puzzle type, the numbers are a
    form of discrete tomography that measures how many unbroken lines of filled-in
    squares there are in any given row or column.

In a Nonogram you are given the number of elements in the rows and columns. A row/column
where containing no element has a '0' all other rows/columns will have at least one number.

Each number in a row/column represent sets of elements next to each other.

If a row/column have multiple sets, the declaration of that row/column will have multiple
numbers. These sets will always be at least 1 cell apart.

An example
			2 	1 	1
		1 	1 	1 	2 	1
	2 		* 	*
1 	2 		* 		* 	*
	0
2 	1 	* 	* 		*
	2 			* 	*
Input description

Today you will receive an image in ASCII with ' ' being empty and '*' being full.
 The number of rows and columns will always be a multiple of 5.

    *
   **
  * *
 *  *
*****

Output description

Give the columns and rows for the input

Columns:
    1 1
1 2 1 1 5

Rows:
  1
  2
1 1
1 1
  5

Ins

1

    *
   /|
  / |
 /  |
*---*

2

    /\ #
   /**\#
  /****\
 /******\
/--------\
 |      |
 | || # |
 | || # |
 | ||   |
 *------*

Bonus

Place the columns and rows in a grid like you would give to a puzzler

        1 1
    1 2 1 1 5
  1
  2
1 1
1 1
  5

'''

pattern = '''    *
   /|
  / |
 /  |
*---*'''

pattern = pattern.splitlines()

output = []
import re

for x in range(0, len(pattern)):
    print()
    ans = re.findall('\S\S\S\S\S|\S\S|\S', pattern[x])
    temp = []
    for item in ans:
        len_item = len(item)
        temp.append(str(len_item))
    output.append(temp)
    temp = []
N = len(output)

b = ''
c = []
for lst in output:
    for item in lst:
        b += item
    b = b.rjust(2, ' ')
    c.append(b)
    b = ''

d = '   '
e = []
# width
M = len(c[0])

for x in range(0, M):
    for y in range(0, len(c)):
        d += c[y][x] + ' '
    e.append(d)
    print(d)
    d = '   '

for x in range(0, N):
    temp = c[x][0]
    temp2 = c[x][1]
    print(c[x][0], end='')
    print('{: >2}'.format(c[x][1]))



