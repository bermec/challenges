'''
Flood-fill is a tool used in essentially any image editing program that's worth its salt.
It allows you to fill in any contigious region of colour with another colour, like
flooding a depression in a board with paint. For example, take this beautiful image. If I
was to flood-fill the colour orange into this region of the image, then that region would
 turned completely orange.

Today, you're going to implement an algorithm to perform a flood-fill on a text ASCII-style image.
Input and Output Description
Challenge Input

You will accept two numbers, w and h, separated by a space. These are to be the width and
height of the image in characters, with the top-left being (0, 0). You will then accept a
grid of ASCII characters of size w*h. Finally you will accept two more numbers, x and y,
and a character c. x and y are the co-ordinates on the image where the flood fill should
be done, and c is the character that will be filled.

Pixels are defined as contigious (touching) when they share at least one edge (pixels that
only touch at corners aren't contigious).

For example:

37 22
.....................................
...#######################...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#######.....
...###.................##......#.....
...#..##.............##........#.....
...#....##.........##..........#.....
...#......##.....##............#.....
...#........#####..............#.....
...#........#..................#.....
...#.......##..................#.....
...#.....##....................#.....
...#...##......................#.....
...#############################.....
.....................................
.....................................
.....................................
.....................................
8 12 @

Challenge Output

Output the image given, after the specified flood-fill has taken place.

.....................................
...#######################...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#...........
...#.....................#######.....
...###.................##......#.....
...#@@##.............##........#.....
...#@@@@##.........##..........#.....
...#@@@@@@##.....##............#.....
...#@@@@@@@@#####..............#.....
...#@@@@@@@@#..................#.....
...#@@@@@@@##..................#.....
...#@@@@@##....................#.....
...#@@@##......................#.....
...#############################.....
.....................................
.....................................
.....................................
.....................................

Sample Inputs and Outputs
Input

16 15
----------------
-++++++++++++++-
-+------------+-
-++++++++++++-+-
-+------------+-
-+-++++++++++++-
-+------------+-
-++++++++++++-+-
-+------------+-
-+-++++++++++++-
-+------------+-
-++++++++++++++-
-+------------+-
-++++++++++++++-
----------------
2 2 @

Output

----------------
-++++++++++++++-
-+@@@@@@@@@@@@+-
-++++++++++++@+-
-+@@@@@@@@@@@@+-
-+@++++++++++++-
-+@@@@@@@@@@@@+-
-++++++++++++@+-
-+@@@@@@@@@@@@+-
-+@++++++++++++-
-+@@@@@@@@@@@@+-
-++++++++++++++-
-+------------+-
-++++++++++++++-
----------------

Input

9 9
aaaaaaaaa
aaadefaaa
abcdafgha
abcdafgha
abcdafgha
abcdafgha
aacdafgaa
aaadafaaa
aaaaaaaaa
8 3 ,

Output

,,,,,,,,,
,,,def,,,
,bcd,fgh,
,bcd,fgh,
,bcd,fgh,
,bcd,fgh,
,,cd,fg,,
,,,d,f,,,
,,,,,,,,,

Extension (Easy/Intermediate)

Extend your program so that the image 'wraps' around from the bottom to the top, and from
the left to the right (and vice versa). This makes it so that the top and bottom, and left
and right edges of the image are touching (like the surface map of a torus).
Input

9 9
\/\/\/\.\
/./..././
\.\.\.\.\
/.../.../
\/\/\/\/\
/.../.../
\.\.\.\.\
/./..././
\/\/\/\.\
1 7 #

Output

\/\/\/\#\
/#/###/#/
\#\#\#\#\
/###/###/
\/\/\/\/\
/###/###/
\#\#\#\#\
/#/###/#/
\/\/\/\#\

'''

import re

data = '''....
...#
...#
...#
...#
...#
...#
...#
3 7 @'''

def blah(height, width, new_data, fill):
    acc = 3

    for y in range(height, -1, -1):
        for x in range(0, acc):
            new_data[y][x] = fill
            #print(new_data)
            print(new_data[y][x])
            print('x: ', x, 'y: ', y)
        acc -= 2
    return new_data


data = data.splitlines()
info = data.pop(-1)
info = info.split()


new_data = []
for dat in data:
    dat = list(dat)
    new_data.append(dat)

width = int(info[0])
height = int(info[1])
fill = info[2]

#lenh = len(new_data[0])

'''
for x in range(0, width):
    temp = new_data[height][x]
    new_data[height][x] = fill
'''

new_data2 = blah(height, width, new_data, fill)
print(new_data2)
