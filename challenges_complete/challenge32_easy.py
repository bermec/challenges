''' lets simulate a roulette wheel!
a program that takes as input your bet, and gives as output how much you won,
with the appropriate probability

write a program that will take a players bet and output the resulting spin and payout. try using an
american roulette wheel (which has the 00 slot) to add a slight twist.
and try to incorporate as many complex bets as you can to. a comprehensive list can be found here
'''
import random

table = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19,
         31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]

spin = random.randrange(0, len(table))
result = table[spin]

bet = input('Pick your numbers in the form n/n/n.....:  ')
cash = input('Amount to be bet £s :  ')


bet = bet.split('/')


if str(result) in bet:

    n = len(bet)
    payout = ((36/n) - 1) * cash
    print(str(result) + '!!! You won £' + str(payout) + ' !!')
else:
    print(str(result) + '!!!!  LOSER!! Keep betting sucker')
