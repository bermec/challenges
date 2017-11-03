'''
 When you were a little kid, was indiscriminately flicking light switches super fun?
 I know it was for me. Let's tap into that and try to recall that feeling
 with today's challenge.

Imagine a row of N light switches, each attached to a light bulb.
All the bulbs are off to start with. You are going to release your inner child
so they can run back and forth along this row of light switches, flipping bunches
of switches from on to off or vice versa. The challenge will be to figure out
the state of the lights after this fun happens.
Input description

The input will have two parts. First, the number of switches/bulbs (N) is specified.
On the remaining lines, there will be pairs of integers indicating ranges of switches
that your inner child toggles as they run back and forth. These ranges are inclusive
(both their end points, along with everything between them is included), and the
positions of switches are zero-indexed (so the possible positions range from 0 to N-1).

Example input:

10
3 6
0 4
7 3
9 9

There is a more thorough explanation of what happens below.
Output description

The output is a single number: the number of switches that are on after all the running around.

Example output:

7

Explanation of example

Below is a step by step rendition of which switches each range toggled in order to get the output described above.

    0123456789
    ..........
3-6    ||||
    ...XXXX...
0-4 |||||
    XXX..XX...
7-3    |||||
    XXXXX..X..
9-9          |
    XXXXX..X.X

As you can see, 7 of the 10 bulbs are on at the end.
Challenge input

1000
616 293
344 942
27 524
716 291
860 284
74 928
970 594
832 772
343 301
194 882
948 912
533 654
242 792
408 34
162 249
852 693
526 365
869 303
7 992
200 487
961 885
678 828
441 152
394 453


'''

data = '3 6\
    0 4\
    7 3\
    9 9'
data = data.split()

data2 = '616 293\
    344 942\
    27 524\
    716 291\
    860 284\
    74 928\
    970 594\
    832 772\
    343 301\
    194 882\
    948 912\
    533 654\
    242 792\
    408 34\
    162 249\
    852 693\
    526 365\
    869 303\
    7 992\
    200 487\
    961 885\
    678 828\
    441 152\
    394 453'

data_list = []
for x in data:
    if x.isdigit():
        data_list.append(x)
#print(data_list)

n = 10
n2 = 1000

lights = ['0'] * n

for x in range(0, len(data_list), 2):
    a = int(data_list[x])
    b = int(data_list[x + 1])
    if b < a:
        temp = b
        b = a
        a = temp

    for x in range(a, b + 1):
        if lights[x] == '0':
            lights[x] = 'x'
        else:
            lights[x] = '0'

print(lights.count('x'))

data2 = data2.split()
data_list = []
for x in data2:
    if x.isdigit():
        data_list.append(x)


lights = ['0'] * n2

for x in range(0, len(data_list), 2):
    a = int(data_list[x])
    b = int(data_list[x + 1])
    if b < a:
        temp = b
        b = a
        a = temp

    for x in range(a, b + 1):
        if lights[x] == '0':
            lights[x] = 'x'
        else:
            lights[x] = '0'

print(lights.count('x'))
