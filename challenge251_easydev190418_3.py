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

pattern = '''    /\ #
   /**\#
  /****\\
 /******\\
/--------\\
 |      |
 | || # |
 | || # |
 | ||   |
 *------*
'''

pattern = pattern.splitlines()
print(pattern)
import re

def regex(l):
    '''Extract ascii and form a list'''
    output = []
    temp = []
    for x in range(0, len(l)):
        ans = re.findall('\S{10|\S{9}|\S{8}|\S{7}|\S{6}|\S{5}|\S{4}|\S{3}|\S{2}|\S{1}', l[x])
        print('ans: ', ans)
        print('length of l: ', len(l))
        # iterate and count the individual results
        for item in ans:
            len_item = len(item)
            temp.append(str(len_item))
        # store in a list
        output.append(temp)
        temp = []

    return output


def pad_out(l):
    # adjust the output for print presentation
    N = len(l)
    M = 0
    # set M to length of longest string in the output
    for strng in l:
        if len(strng) >= M:
            M = len(strng)
    # make all strings the same length for output
    b = ''
    c = []
    for lst in l:
        for item in lst:
            b += item
        b = b.rjust(M, ' ')
        c.append(b)
        b = ''
    return c


if __name__ ==  '__main__':
    # Prepare for vertical printing


    len_string = 0
    for strng in pattern:
        temp = len(strng)
        if temp >= len_string:
            len_string = temp

    # pad out to 10
    for strng in pattern:
        strng = strng.ljust(len_string)
    print(pattern)
    print(pattern[8][0])



    # rearrange pattern
    temp = ''
    lst = []
    len_pattern = len(pattern)
    for x in range(0, len(strng)):
        for y in range(0, len_pattern):
            try:
                char = pattern[y][x]
            except IndexError:
                temp += ' '
            temp += char
        lst.append(temp)
        temp = ''
    print(lst)
    

    # extract rows of characters and count the row
    vert_output = []
    vert_output = regex(lst)

    # pad out for printing
    vert_pad = pad_out(vert_output)

    # print
    for s in vert_pad:
        for item in s:
            print(item, end='')
        print()

    '''
    # extract rows of characters and count the row
    output = regex(pattern)

    # pad out for printing
    padded = pad_out(output)

    # print the row output
    c = padded
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

'''
