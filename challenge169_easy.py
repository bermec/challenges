'''
Given a NxN size 2D array of numbers. Develop a way to rotate the data
as if you rotated the data by 90 degrees clockwise.
Example:

N = 3
Data:
1 2 3
4 5 6
7 8 9
Rotate 90 degrees:
7 4 1
8 5 2
9 6 3
Rotate it again 90 degrees:
9 8 7
6 5 4
3 2 1
Challenge Input:

N = 10
1 2 3 4 5 6 7 8 9 0
0 9 8 7 6 5 4 3 2 1
1 3 5 7 9 2 4 6 8 0
0 8 6 4 2 9 7 5 3 1
0 1 2 3 4 5 4 3 2 1
9 8 7 6 5 6 7 8 9 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
9 8 7 6 7 8 9 8 7 6
0 0 0 0 0 0 0 0 0 0
Optional:

Show the 2D array at 90, 180, 270 degree clockwise from the
original position.'''

array = '''1 2 3
4 5 6
7 8 9'''

l = list(array.split())
leng = len(l) ** 0.5
n = int(len(l) ** 0.5)

#-- initial  -----------------------

# list of lists
L = [l[i:i + n] for i in range(0, len(l), n)]


for el in L:
    print('{0} {1}'.format(el[0],' '.join(str(i) for i in el[1:])))

#-- 90 degree -------------------------------------------------------
l.reverse()
lst = []
a = int(leng - 1)
b = int(len(l)**0.5)
acc = 0
# split list in chunks
while True:
    for i in range(a, len(l), b):
        lst.append(l[i])
    a -= 1
    acc += 1
    if acc == b:
        break

L = [lst[i:i + n] for i in range(0, len(lst), n)]

print()
for element in L:
    print('{0} {1}'.format(element[0], ' '.join(str(i) for i in element[1:])))

# 180 degree -------------------------------------------------------
# using the reversed list
L = [l[i:i + n] for i in range(0, len(l), n)]

print()
for el in L:
    print('{0} {1}'.format(el[0],' '.join(str(i) for i in el[1:])))

#-- 270 degees ----------------------------------------------------
# list back to initial, a reverse of 90 degrees
l.reverse()
lst = []
a = int(leng -1)
b = int(len(l)**0.5)
acc = 0
while True:
    for i in range(a, len(l), b):
        lst.append(l[i])
    a -= 1
    acc += 1
    if acc == b:
        break

L = [lst[i:i + n] for i in range(0, len(lst), n)]

print()
for element in L:
    print('{0} {1}'.format(element[0], ' '.join(str(i) for i in element[1:])))
