'''
For those who want to know more about Texas Hold 'Em Poker or just need a refresher.
Check Wikipedia Article on Texas Hold 'Em Poker

For the first challenge we will simulate the dealing part of the game.
Input:

You will be asked how many players 2 to 8. You will always be one of the
players and you are facing 1 to 7 other computer controlled players.
Output:

Display the 2 cards each player is dealt and the display the 5 community cards.

Format is left up to you. (The exact method of the output a card. For my
examples I am using verbal words but someone might use unicode symbols for
the card suit or other. You design this as long as we can tell the cards
apart it is all good)
Example:

How many players (2-8) ? 3

Your hand: 2 of Clubs, 5 of Diamonds
CPU 1 Hand: Ace of Spades, Ace of Hearts
CPU 2 Hand: King of Clubs, Queen of Clubs

Flop: 2 of Hearts, 5 of Clubs, Ace of Clubs
Turn: King of Hearts
River: Jack of Hearts

Dealing Cards:

To keep things close to the game you will be dealing from 1 deck of
standard playing cards. Once you deal that card you cannot deal it again.
The exact method is part of the challenge and for you to decide, design and implement.

In Texas Hold em you burn a card (draw and discard without looking at it)
before you do the flop, turn and river. It removes these cards from the pool of
possible cards that can be dealt. If you wish to show these cards
(I did not in my example) then please for science go for it.
'''
import random


def choice(s):
    return random.choice(s)

def dealing(s):
    return ('{0}{1}{2}'.format(s[0], ' of ', s[1]))


suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
rank =['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King']

dealt = []
num = 0

#school = input('Number of players? ')
school = 6


print('Player')

while num < 2:
    player_rank = choice(rank)
    player_suit = choice(suits)
    player = (player_rank, player_suit)

    if player not in dealt:
        print(dealing(player))
        num += 1
    else:
        continue
    dealt.append(player)

num = 0
print()
print("Players (cpu)")
accum = 1
for x in range(school - 1):
    num = 0
    print('CPU: ', accum)
    while num < 2:
        cpu_rank = choice(rank)
        cpu_suit = choice(suits)
        cpu = (cpu_rank, cpu_suit)

        if cpu not in dealt:
            print(dealing(cpu))
            num += 1
        else:
            continue
        dealt.append(cpu)
    accum += 1

num = 0
print()
print('Flop')
while num < 3:
    flop_rank = choice(rank)
    flop_suit = choice(suits)
    flop =(flop_rank, flop_suit)

    if flop not in dealt:
        print(dealing(flop))
        num += 1
    else:
        continue
    dealt.append(flop)

num = 0
print()
print('Turn')
while num < 1:
    turn_rank = choice(rank)
    turn_suit = choice(suits)
    turn = (turn_rank, turn_suit)

    if turn not in dealt:
        print(dealing(turn))
        num += 1
    else:
        continue
    dealt.append(turn)

num = 0
print()
print('River')
while num < 1:
    river_rank = choice(rank)
    river_suit = choice(suits)
    river = (river_rank, river_suit)
    if river not in dealt:
        print(dealing(river))
        num += 1
    else:
        continue
    dealt.append(river)