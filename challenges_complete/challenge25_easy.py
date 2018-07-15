''' In an election, the person with the majority of the votes is the winner.
Sometimes due to similar number of votes, there are no winners.

Your challenge is to write a program that determines the winner of a vote,
or shows that there are no winners due to a lack of majority.

'''

votes = ['B', 'B', 'A', 'A', 'C', 'A', 'A', 'C', 'C', 'B', 'A', 'B', 'C', 'A', 'C']

def winner_str(strng):
    print('The outright winner is {0}!'.format(strng))

def no_overall():
    print('No outright winner, coalition required.')

def draw(strng):
    print('The result is null, {0} have tied, a re-run is required.'.format(strng))

count_A = votes.count('A')
count_B = votes.count('B')
count_C = votes.count('C')

if count_A > (count_B + count_C):
    winner = count_A
    winner_str('A')
elif count_B > (count_A + count_C):
    winner_str('B')
else:
    if count_C > (count_A + count_B):
        winner_str('C')

if count_A - (count_B + count_C) <= 0:
    no_overall()
elif count_B - (count_A + count_C) <= 0:
    no_overall()
else:
    if count_C - (count_A + count_B) <= 0:
        no_overall()

if count_C - (count_A + count_B) <= 0 and count_A == count_B:
    draw("'A' and 'B' ")
elif count_B - (count_A + count_C) <= 0 and count_A == count_C:
    draw("'A' and 'C'")
else:
    if count_A - (count_B + count_C) <= 0 and count_B == count_C:
        draw("'B' and 'C' ")
