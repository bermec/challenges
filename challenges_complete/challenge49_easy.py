''' The Monty Hall Problem is a probability brain teaser that
has a rather unintuitive solution.

The gist of it, taken from Wikipedia:

    Suppose you're on a game show, and you're given the choice of three doors:
    Behind one door is a car; behind the others, goats. You pick a door,
    say No. 1 [but the door is not opened], and the host, who knows what's behind the doors,
    opens another door, say No. 3, which has a goat. He then says to you, "Do you want to
    pick door No. 2?" Is it to your advantage to switch your choice? (clarification: the host will always reveal a goat)

Your task is to write a function that will compare the strategies of switching and not switching over many
random position iterations. Your program should output the proportion of successful choices by each strategy.
Assume that if both unpicked doors contain goats the host will open one of those doors at random with equal probability.

If you want to, you can for simplicity's sake assume that the player picks the first door every time.
The only aspect of this scenario that needs to vary is what is behind each door.
'''
import random
door1, door2, door3 = [''] * 3
cont_count = 0
alt_count = 0
acc = 0
doors = [door1, door2, door3]
prizes = ['car', 'goat', 'goat2']

def choice(lst):
    return random.choice(lst)

while acc <= 100000:
    #-- place prizes behind doors -----------------
    prize = choice(prizes)
    door1 = prize
    doors = [door1, door2, door3]
    while True:
        prize = choice(prizes)
        door2 = prize
        doors = [door1, door2, door3]
        if door2 == door1:
            continue
        else:
            break

    while True:
        prize = choice(prizes)
        door3 = prize
        doors = [door1, door2, door3]
        if door3 == door2 or door3 == door1:
            continue
        else:
            break
    #-- contestant picks a door ----------------------
    contestant = ''
    door_choice = choice(doors)
    contestant = door_choice


    #-- gameshow host picks a door --------------------
    game_host = ''

    while True:
        door_choice = choice(doors)
        game_host = door_choice
        if game_host == 'car' or game_host == contestant :
            continue
        else:
            break

    #-- the alternative door -----------------------------------------------------
    while True:
        alternate_contestant = choice(doors)
        if alternate_contestant == game_host or alternate_contestant == contestant:
            continue
        else:
            break

    #-- check results ----------------------
    if contestant == 'car':
        cont_count += 1
    elif alternate_contestant == 'car':
        alt_count += 1

    acc += 1


print('First choice: ',cont_count,'  second choice:  ', alt_count)









