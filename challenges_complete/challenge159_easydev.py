
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

    print("winner is" + " " + winner)
    print(game_reports(player_number, comp_number))
    print()

if __name__ == '__main__':

    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")



