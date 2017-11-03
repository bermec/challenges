
''' create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.

'''

name = input('What is your name? ')
age = input('And your age ? ')
reddit = input('Your Reddit username please... ')

ans = ('your name is {0}, you are {1} years old, and your username is {2}'.format(name, age, reddit))
print(ans)

with open('reddit.txt', 'w') as f:
    f.write(ans)