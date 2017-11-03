'''
You may have seen Pascal's Triangle before. It has been known about
for a long time now and is a very simple concept - it makes several
appearances in mathematics, one of which is when you calculate
the binomial expansion.
If you've not seen it before, you can calculate it by first putting
 1 on the outermost numbers:

    1
   1 1
  1 _ 1
 1 _ _ 1
1 _ _ _ 1

And then each number within the triangle can be calculated by adding
the two numbers above it, to form this:

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

It has several interesting properties, however what we're interested
in is the 3-dimensional version of this triangle - Pascal's Pyramid.
It works in much the same way - the corner numbers are all 1s.
However the edges are all layers of Pascal's triangle, and each inner
number is the sum of the 3 numbers above it. Besides that there is
nothing else to it.

Here are the first 5 cross-sectional 'layers', top to bottom:

1

 1
1 1

  1
 2 2
1 2 1

   1
  3 3
 3 6 3
1 3 3 1

      1
    4  4
   6  12 6
 4  12 12 4
1  4  6  4  1

See how the outermost 'rows' or 'edges' of numbers on all of the above are
layers of Pascal's Triangle, as we saw above. Therefore, The faces of
Pascal's Pyramid, were it a 3D object, would have Pascal's Triangle on them!

Your challenge is, given a number N, to calculate and display the
Nth layer of Pascal's Pyramid.
Formal Inputs and Outputs
Input Description

On the console, you will be given a number N where N > 0.
Output Description

You must print out layer N of Pascal's Pyramid. The triangle cross-section
must be presented so the point is at the top. Each row shall be separated
by newlines, and each number shall be separated by spaces.
Spacing is not important but your submission would be even cooler if it
were displayed properly. For example, for the 3rd layer, a valid output
would be as so:

1
2 2
1 2 1

Or, better:

  1
 2 2
1 2 1

Or even:

   1
     2   2
1   2 1

But why you'd do the latter is beyond me.
Sample Inputs & Outputs
Sample Input

6

Sample Output

1
5 5
10 20 10
10 30 30 10
5 20 30 20 5
1 5 10 10 5 1

Challenge
Challenge Input

14

Notes

There are ways to quickly do this that use the Factorial function.
Also, look at the pattern the 'rows' make in relation to the leftmost
and rightmost number and Pascal's triangle.
Reading material on Pascal's Pyramid can be found here.

Jagged multidimensional arrays will come in handy here.

I'm still trying to gauge relative challenge difficulty,
so please excuse me and let me know if this is too challenging
for an Easy rating.
'''

# ones on the corners, the outside have Pascal's Triangle on them and the inners are a sum of the three numbers above it.


def pasctetrow(n, r):
    """
    return a row of Pascal's Tetrahedron at level n
    """
    row = []
    for c in range(0, r+1):
        row.append(pasctet(n, r, c))
    return row


def pasctet(n, r, c):  # thanks to David Chako

    """
    lookup entry (r = row, c = column)
    in level n of Pascal's Tetrahedron
    """
    i,j,k = getijk(n, r, c)
    return fact(n)/(fact(i)*fact(j)*fact(k))


def getijk(n, r, c):
    i = n-r; j = r-c; k = n-i-j
    return [i, j, k]


def fact(n):
    """
    factorial of n (recursive)
    """
    if n <= 1:
        return (1)
    else:
        return n * fact(n-1)


def pasctetlev(n):
    """print level n of Pascal's Tetrahedron"""
    for r in range(n+1):
        row = pasctetrow(n, r)
        for x in range(0, len(row)):
            if x == len(row) - 1:
                print(int(row[x]))
            else:
                print(int(row[x]), end='' + ' ')


if __name__ == '__main__':
    pasctetlev(14)

# adapted from 4D solutions by Kirby Urner