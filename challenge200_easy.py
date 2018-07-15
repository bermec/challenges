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

def blah(height, width, new_data):
    acc = width + 4
    for y in range(height, -1, -1):
        for x in range(4, acc):
            new_data[y][x] = fill
        acc -= 2
    return new_data



def blah2(height, width, new_data):
    acc = width + 4
    for y in range(height + 1, height + 5):
        for x in range(4, acc):
            new_data[y][x] = fill
        acc -= 1
    return new_data

if __name__ == '__main__':
    import re

    data = '''.....................................
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
    8 12 @'''

    data = data.splitlines()
    newline = []
    for line in data:
        line = line.strip()
        newline.append(line)

    data = newline

    info = data.pop(-1)
    info = info.split()

    new_data = []
    for dat in data:
        dat = list(dat)
        new_data.append(dat)

    width = int(info[0])
    height = int(info[1])
    fill = info[2]

    lenh = len(new_data[0])

    new_data = blah(height, width, new_data)
    new_data = blah2(height, width, new_data)

    for data in new_data:
        for item in data:
            print(item, end='')
        print()

    # or using regex...

    data = '''.....................................
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
        8 12 @'''

    candidates = data.splitlines()

    for x in range(0, len(candidates)):
        temp = candidates[x]
        select = re.findall(r'(?<=\s\s\s\s\.\.\.\#)\.*(?=\#)', temp)
        try:
            N = len(select[0])
        except:
            N = 0
        if 1 <= N <= 8:
            N = len(select[0])
            temp = candidates[x]
            p = re.compile(r'(?<=\s\s\s\s\.\.\.\#)\.*(?=\#)')
            c = re.sub(p, 's' * N, temp)
            print(c)
            continue
        else:
            print(temp)

    candidates = '''
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
    '''
    candidates = candidates.splitlines()

    for line in candidates:
        select = re.findall('\-\+(\-+)+\-', line)

        if len(select) > 0:
            N = len(select[0])
            select = re.sub('(?!\-\+)\-+(?<!\+\-)',  '@' * N, line)
            print(select)
            continue
        print(line)


    candidates = '''
    aaaaaaaaa
    aaadefaaa
    abcdafgha
    abcdafgha
    abcdafgha
    abcdafgha
    aacdafgaa
    aaadafaaa
    aaaaaaaaa
    '''
    candidates = candidates.splitlines()

    for line in candidates:
        select = re.sub('a', ',', line)
        print(select)


