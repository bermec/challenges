''' The one-dimensional simple cellular automata Rule 110
is the only such cellular automata currently known to be turing-complete,
and many people say it is the simplest known turing-complete system.

Implement a program capable of outputting an ascii-art representation of
applying Rule 110 to some initial state. How many iterations and what
your initial state is is up to you!

You may chose to implement rule 124 instead if you like (which is the
same thing, albeit backwards).

Bonus points if your program can take an arbitrary rule integer from
The one-dimensional simple cellular automata Rule 110 is the only such
cellular automata currently known to be turing-complete, and many people
say it is the simplest known turing-complete system.

'''
import random

#this represents how many times program will cycle
total=random.randrange(1,256)
row=[]

# total cycles is random
for i in range(total):
    newRow=[]#these need to reset each time they go through the loop and recalculate
    attach=[]
#this adds 3 elements to the 'old' row (i use 3 so the list grows by one each cycle)
    for i in range(3):
        attach.extend([random.randrange(0,2)])
    row.extend(attach)
#determines the next row of elements
    for i in range(len(row)-2):
        if row[i:i+3]==[1,1,1] or row[i:i+3]==[1,0,0] or row[i:i+3]==[0,0,0]:
            newRow.extend([0])
        else:
            newRow.extend([1])
    row=newRow
#converts lists to characters
    for i in range(len(row)):
        if row[i]==0:
            print(' ', end='')
        else:
            print('X', end='')
    print()
