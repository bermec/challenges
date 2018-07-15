''' A word snake is (unsurprisingly) a snake made up of a sequence of words.

For instance, take this sequence of words:

SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE
Notice that the last letter in each word is the same as the first letter in the next word. In order to make this into a word snake, you simply snake it across the screen

SHENANIGANS
          A
          L
          T
          YOUNGSTER
                  O
                  U
                  N
            TELBUOD
            E
            R
            A
            B
            Y
            T
            ESSENCE

Your task today is to take an input word sequence and turn it into a word snake. Here are the rules for the snake:

    It has to start in the top left corner
    Each word has to turn 90 degrees left or right to the previous word
    The snake can't intersect itself

Other than that, you're free to decide how the snake should "snake around". If you want to make it easy for yourself and simply have it alternate between going right and going down, that's perfectly fine. If you want to make more elaborate shapes, that's fine too.
Formal inputs & outputs
Input

The input will be a single line of words (written in ALL CAPS). The last letter of each word will be the first letter in the next.
Output

Your word snake! Make it look however you like, as long as it follows the rules.
Sample inputs & outputs

There are of course many possible outputs for each inputs, these just show a sample that follows the rules
Input 1

SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE

'''


def clean_up(string):
    ''' str -> lst
    convert string to list of integers
    '''
    temp_list = []
    lst = string.split()
    for x in lst:
        temp_list.append(x)
    lst = temp_list
    return lst


if __name__ == '__main__':

    string = 'SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE'
    # convert to usable list
    lst = clean_up(string)

    # pad out with spaces
    padding = len(lst[0])

    # first word SHENANIGANS
    print(lst[0])

    # second and third word SALTY, YOUNGSTER
    leng = len(lst[1])
    for x in range(1, leng + 1):
        if x == len(lst[1]):
            print(lst[1][-1].rjust(padding, ' '), end='' + lst[2][1:])
        else:
            print(lst[1][x].rjust(padding, ' '))

    # fourth word ROUND
    padding2 = padding + len(lst[2]) - 1
    leng1 = len(lst[3])
    print()
    for x in range(1, leng1 - 1):
        item = lst[3][x]
        if x == len(lst[3]):
            print(lst[3][-1].rjust(padding2, ' '), end='')
        else:
            print(lst[3][x].rjust(padding2, ' '))

    # fifth word DOUBLET
    item4 = lst[4]
    item4 = item4[::-1]
    print(item4.rjust(padding2, ' '))

    # sixth word TERABYTE
    padding3 = padding + 2
    for x in range(1, len(lst[5]) - 1):
        item = lst[5][x]
        if x == len(lst[5]):
            print(lst[5][-1].rjust(padding3, ' '), end='')
        else:
            print(lst[5][x].rjust(padding3, ' '))

    # last word ESSENSE
    print(lst[6].rjust(padding2, ' '))

