'''
So went to a Casino recently. I noticed at the Blackjack tables the house tends
to use several decks and not 1. My mind began to wonder about how likely natural
blackjacks (getting an ace and a card worth 10 points on the deal) can occur.

So for this monday challenge lets look into this. We need to be able to shuffle
deck of playing cards. (52 cards) and be able to deal out virtual 2 card hands
and see if it totals 21 or not.

    Develop a way to shuffle 1 to 10 decks of 52 playing cards.
    Using this shuffle deck(s) deal out hands of 2s
    count how many hands you deal out and how many total 21 and output the percentage.

Input:

n: being 1 to 10 which represents how many deck of playing cards to shuffle together.
Output:

After x hands there was y blackjacks at z%.
Example Output:

After 26 hands there was 2 blackjacks at %7.

'''
import random

deck = {'Ace': 11,
        'King': 10,
        'Queen': 10,
        'Jack': 10,
        'Ten': 10,
        'Nine': 9,
        'Eight': 8,
        'Seven': 7,
        'Six': 6,
        'Five': 5,
        'Four': 4,
        'Three': 3,
        'Two': 2
        }

win =0
lose = 0
lst = []
acc = 0
hands = 0
while hands < 26:
    acc = 0
    lst = []
    while acc < 2:
        # key/value pair
        candidate = random.choice(list(deck.keys()))
        # value
        valu = deck.get(candidate)
        lst.append(valu)
        acc += 1
    score = sum(lst)
    if score == 21:
        win += 1
    else:
        lose += 1
    hands += 1
    score = 0
#print(win,lose)

print('After 26 hands there were ' + str(win) + ' blackjacks  at ' + str(round(win/26 * 100, 2)) + '%')