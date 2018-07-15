'''
Welcome to my first attempt at a theme week. All week long the
 challenges will be related to this fascinating advanced version
 of the game Rock Paper Scissors. We will explore the depths of
 this game like none have before.
Description:

The best way to see this game and understand the rules is to do
some basic research.

    Wikipedia Entry Link

The challenge is to implement a basic game of Rock Paper Scissors
Lizard Spock (to be called RPSLP for short). Your game will get
the human choice. The computer AI will randomly pick a move.
It will compare the results and display the moves and the out
come (who wins or if a tie)
Input:

Get from the user their move being Rock, Paper Scissors, Lizard,
Spock. Design and how you do it is up to you all.
Output:

Once the human move is obtained have the computer randomly pick
their move. Display the moves back to the user and then give the results.

Again the exact design is up to you as long as the output shows
the moves again and the result of the game (who wins or if a tie).
Example Output:

Player Picks: Rock.
Computer Picks: Spock.

Spock Vaporizes Rock. Computer Wins!

For Weds:

As this is a theme challenge. Weds we continue with a more
intermediate approach to the game. To plan ahead please
consider in your design some ability to have a human choice
be compared to a computer choice or a computer to play itself as well.
Extra Challenge:

The game loops and continues to play matches until the user
quits or a fixed number of games is played. At the end it
records some basic stats.

    Total Games played
    Computer Wins (Number and percentage)
    Human Wins (Number and percentage)
    Ties (Number and Percentage)

'''
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def game_reports(p, c):
    ''' Report of result of contest'''
    if p == 0 and c == 1:
        return 'Spock vapourizes Rock!'
    elif p == 0 and c == 2:
        return 'Paper covers Rock!'
    elif p == 0 and c == 3:
        return 'Rock crushes Lizard!'
    elif p == 0 and c == 4:
        return 'Rock crushes Scissors!'
    elif p == 1 and c == 0:
        return 'Spock vapourizes Rock!'
    elif p == 1 and c == 2:
        return 'Paper disproves Spock!'
    elif p == 1 and c == 3:
        return 'Lizard poisons Spock!'
    elif p == 1 and c == 4:
        return 'Spock smashes Scissors!'
    elif p == 2 and c == 0:
        return 'Paper covers Rock!'
    elif p == 2 and c == 1:
        return 'Paper disproves Spock!'
    elif p == 2 and c == 3:
        return 'Lizard eats Paper!'
    elif p == 2 and c == 4:
        return 'Scissors cuts Paper!'
    elif p == 3 and c == 0:
        return 'Rock crushes Lizard!'
    elif p == 3 and c == 1:
        return 'Lizard poisons Spock!'
    elif p == 3 and c == 2:
        return 'Lizard eats Paper!'
    elif p == 3 and c == 4:
        return 'Scissors decapitates Lizard!'
    elif p == 4 and c == 0:
        return 'Rock crushes Scissors!'
    elif p == 4 and c == 1:
        return 'Spock smashes Scissors!'
    elif p == 4 and c == 2:
        return 'scissors cuts Paper!'
    elif p == 4 and c == 3:
        return 'Scissors decapitates Lizard!'
    else:
        pass


def name_to_number(name):
    ''' convert name to number using if/elif/else. '''
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    return number


def number_to_name(number):
    ''' convert number to name. '''
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    return name



def rpsls(player_choice):

    # print out the message for the player's choice
    print("Player Picks:" + " " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print("Computer Picks:" + " " + comp_choice)

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5

    # if/elif/else to determine winner, print winner message
    if difference > 2:
        winner = "computer"
    elif difference == 1 or difference == 2:
        winner = "player"
    else:
        winner = "a tie"
    report = game_reports(player_number, comp_number)
    print('{0}{2}{1}{2}{3}'.format(report, "winner is", " ",  winner))
    print()

if __name__ == '__main__':

    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")







