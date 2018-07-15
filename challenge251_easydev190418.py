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
*---*
'''

pattern = pattern.splitlines()

output = []
import re

def regex(l):
    '''Extract ascii and form a list'''
    temp = []
    for x in range(0, len(l)):
        ans = re.findall('\S\S\S\S\S|\S\S|\S', l[x])

    # iterate and count the individual results
        for item in ans:
            len_item = len(item)
            temp.append(str(len_item))
        # store in a list
        output.append(temp)

    return output


# extract rows of characters and count the row
for x in range(0, len(pattern)):
    output = regex(pattern)
# ------------------------------------------

# adjust the output for print presentation
N = len(output)
M = 0
# set M to length of longest string in the output
for strng in output:
    if len(strng) >= M:
        M = len(strng)
# make all strings the same length for output
b = ''
c = []
for lst in output:
    for item in lst:
        b += item
    b = b.rjust(M, ' ')
    c.append(b)
    b = ''
# ------------------------------------
# All strings are now of equal lengths


# print the row output
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
# -----------------------------



# Prepare for vertical printing

# rearrange pattern
temp = ''
lst = []
for x in range(0, len(pattern[0])):
    for y in range(0, len(pattern)):

        char = pattern[y][x]
        temp += char
    lst.append(temp)
    temp = ''
print(lst)

vert_output = []
temp = []
#for x in range(0, len(lst)):
temp  = regex(lst)
#vert_output.append(temp)
#temp = []

print(vert_output)
'''
# create the count
sum_list = []
temp  = 0
for strng in lst:
    for sub_string in strng:
        sub_string = sub_string.strip()
        num = len(sub_string)
        temp += num
    sum_list.append(temp)
    temp = 0
print(sum_list)





N = len(pattern[0])
lst = []
temp = ''
for x in range(0, N):
    for s in pattern:
        temp2 = s[x]
        print('temp2: ', temp2)
        temp += temp2
    lst.append(temp)
    temp = ''
print('lst:', lst)

output = []
ans = []

for strng in lst:
    ans = re.findall('\S{5}|\S{4}|\S{3}\S{2}|\S', strng)
    ans2 = len(ans)
    output.append(ans2)

print(output)


for x in range(0, N):
    print()
    ans = re.findall('\S{5}|\S{4}|\S{3}\S{2}|\S', lst[x])
    temp = []
    for item in ans:
        len_item = len(item)
        temp.append(str(len_item))
    output.append(temp)
    temp = []

print(output)


# space out for printing
for lst in output:
    while len(lst) < 3:
        lst.insert(0, ' ')
#print(output)

# print the row output
d = '   '
e = []
# width
M = len(output[0])
for x in range(0, M):
    for y in range(0, len(output)):
        d += output[y][x] + ' '
    e.append(d)
    print(d)
    d = '   '
'''