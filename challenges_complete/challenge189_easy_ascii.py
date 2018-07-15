''' We all know the classic game hangman, today we'll be making it. With the wonderful
bonus that we are programmers and we can make it as hard or as easy as we want. here
is a wordlist to use if you don't already have one. That wordlist comprises of words
spanning 3 - 15+ letter words in length so there is plenty of scope to make this interesting!
Rules

For those that don't know the rules of hangman, it's quite simple.

There is 1 player and another person (in this case a computer) that randomly
chooses a word and marks correct/incorrect guesses.

The steps of a game go as follows:

    Computer chooses a word from a predefined list of words
    The word is then populated with underscores in place of where the letters should. ('hello' would be '_ _ _ _ _')
    Player then guesses if a word from the alphabet [a-z] is in that word
    If that letter is in the word, the computer replaces all occurences of '_' with the correct letter
    If that letter is NOT in the word, the computer draws part of the gallow and eventually all of the hangman
    until he is hung (see here for additional clarification)

This carries on until either

    The player has correctly guessed the word without getting hung

or

    The player has been hung

Formal inputs and outputs
input description

Apart from providing a wordlist, we should be able to choose a difficulty to filter our words down further.
For example, hard could provide 3-5 letter words, medium 5-7, and easy could be anything above and beyond!

On input, you should enter a difficulty you wish to play in.
output description

The output will occur in steps as it is a turn based game. The final condition is either win, or lose.
Clarifications

Punctuation should be stripped before the word is inserted into the game
("administrator's" would be "administrators")

'''

def scaffold():
    a = '------\n|/  |\n|\n|\n|\n|\n--------'
    return a


def head():
    a = '------\n|/  |\n|   O\n|   \n|\n|\n--------'
    return a

def body():
    a = '------\n|/  |\n|   O\n|   |\n|   |\n|\n--------'
    return a


def left_arm():
    a = '------\n|/  |\n|   O\n| -=|\n|   |\n|\n--------'
    return a


def right_arm():
    a = '------\n|/  |\n|   O\n| -=|=-\n|   |\n|\n--------'
    return a

def left_leg():
    a = '------\n|/  |\n|   O\n| -=|=-\n|   |\n|   /\n--------'
    return a


def right_leg():
    a = '------\n|/  |\n|   O\n| -=|=-\n|   |\n|  /\\\n--------'
    return a




def update_dash_word(a, b, index):
    for x in index:
        b = b[:x] + a[x] + b[x + 1:]
    return b



if __name__ =='__main__':

    import random

    # the state of the gallows
    modules = [scaffold(), head(), body(), left_arm(), right_arm(), left_leg(), right_leg()]

    y = 0
    ans = modules[y]
    word_list = []

    # read words from file
    with open('enable1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 5:
                word_list.append(line)

    # pick a word from the list - the_word
    n = random.randrange(1000)
    the_word = word_list[n]

    # blank word
    dash_word = '-----'

    while dash_word != the_word:
        if y == 6:
            print(the_word, 'Beaten!!')
            exit()

        s = input('Guess a letter:  ')

        # find index of 's' in the_word (or not)
        indexes = []
        for letter in the_word:
            if letter == s:
                x = the_word.index(letter)
                indexes.append(x)
        # if no match...
        if len(indexes) == 0:
            y += 1

            print('y = :', y)
            print(modules[y])
            print(dash_word)
            continue

        if dash_word == the_word:
            print('Well done! You have cracked it!!')
            print(the_word)
            exit()

        dash_word = update_dash_word(the_word, dash_word, indexes)
        print(modules[y])
        print(dash_word)









