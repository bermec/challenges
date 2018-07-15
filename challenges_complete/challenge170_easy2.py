'''
 (Easy): Blackjack Checker

Blackjack is a very common card game, where the primary aim is to pick up
cards until your hand has a higher value than everyone else but is less
than or equal to 21. This challenge will look at the outcome of the game,
rather than playing the game itself.

The value of a hand is determined by the cards in it.

    Numbered cards are worth their number - eg. a 6 of Hearts is worth 6.

    Face cards (JQK) are worth 10.

    Ace can be worth 1 or 11.

The person with the highest valued hand wins, with one exception - if a person has
5 cards in their hand and it has any value 21 or less, then they win automatically.
This is called a 5 card trick.

If the value of your hand is worth over 21, you are 'bust', and automatically lose.

Your challenge is, given a set of players and their hands, print who wins (or if it
is a tie game.)
Input Description

First you will be given a number, N. This is the number of players in the game.

Next, you will be given a further N lines of input. Each line contains the name
of the player and the cards in their hand, like so:

Bill: Ace of Diamonds, Four of Hearts, Six of Clubs

Would have a value of 21 (or 11 if you wanted, as the Ace could be 1 or 11.)
Output Description

Print the winning player. If two or more players won, print "Tie".
Example Inputs and Outputs
Example Input 1

3
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs

Example Output 1

Alice has won!

Example Input 2

4
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs
David: Two of Hearts, Three of Clubs, Three of Hearts, Five of Hearts, Six of Hearts

Example Output 2

David has won with a 5-card trick!
'''

import re

players = []
card_values = []

scores = 0

card_nums = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
             'Nine': 9, 'Ten':  10, 'Jack': 10, 'Queen': 10, 'King': 10}

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

hands1 = '''Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs'''

hands2 = '''Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs
David: Two of Hearts, Three of Clubs, Three of Hearts, Five of Hearts, Six of Hearts'''

hands3 = '''Alice: Six of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Eight of Spades
Chris: Ten of Hearts, Three of Diamonds, Four of Clubs'''


def list_sum(numlist):
    ''' (list): -> list
    return the summation of a list
    list_sum([1, 2, 3])
    >>> 6
    list_sum([3, 4, 5])
    >>> 12 '''
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + list_sum(numlist[1:])


hands = hands1.splitlines()

# Extract players
for line in hands:
    player = re.findall('^\w+', line)
    players.append(player[0])

# Extract card values
for line in hands:
    values = re.findall('\w+(?=\sof\s[Hearts|Clubs|Diamonds|Spades])', line)
    card_values.append(values)

# Convert to numerical values
# Place into hands_held
hands_held = []
score_collection = []
for cards in card_values:
    for card in cards:
        score_collection.append(card_nums[card])
    hands_held.append(score_collection)
    score_collection = []


# Sum the hands_held
sums_of_hands = []
for hand in hands_held:
    num = list_sum(hand)
    sums_of_hands.append(num)

five_card_tricks = []
twenty_ones = []
winner_highest = []
hand_totals = []
player_index = []

# Check players(s) hand
# group into winning categories
# accum gives the index of the player
accum = 0
for hand in hands_held:
    sum_of_hand = list_sum(hand)
    if sum_of_hand > 21:
        accum += 1
        continue
    # could it be 5 card trick?
    elif len(hand) == 5:
        if 11 in hand:
            sum_of_hand -= 10
        if sum_of_hand <= 21:
            five_card_tricks.append(accum)
    # or maybe a maximum (21)
    elif sum_of_hand == 21:
        twenty_ones.append(accum)
        accum += 1
    else:
        # next highest hand wins
        maxx = list_sum(hand)
        hand_totals.append(maxx)
        player_index.append(accum)
        accum += 1



highest_value = max(hand_totals)
if hand_totals.count(highest_value) > 1:
    print('Tie!')
    exit()

# player with highest hand - less than 21
index = hand_totals.index(highest_value)
winner_highest.append(player_index[index])

results = [five_card_tricks, twenty_ones, winner_highest]
# winner check
for lst in results:
    if len(lst) > 0:
        for result in lst:
            if len(lst) > 1:
                exit()
            else:
                print(players[result] + ' has won!')
                exit()



