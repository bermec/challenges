''' Write a program to left or right justify a text file
'''

store = 0

with open('enable1.txt', 'r') as f:
    for line in f:
        if len(line) >= store:
            store = len(line)

open('ena2.txt', "w").write("")
out = open('ena2.txt', "a")

with open('enable1.txt', 'r') as f:
    for line in f:
        out.write(line.rjust(store, ' '))



