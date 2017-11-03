'''
Contrary to popular belief, the tetromino pieces you are given in a game
of Tetris are not randomly selected.
Instead, all seven pieces are placed into a "bag." A piece is randomly
removed from the bag and presented to the player until the bag is empty.
When the bag is empty, it is refilled and the process is repeated for any
additional pieces that are needed.

In this way, it is assured that the player will never go too long without
seeing a particular piece. It is possible for the player to receive two
identical pieces in a row, but never three or more. Your task for today is
to implement this system.
Input Description

None.
Output Description

Output a string signifying 50 tetromino pieces given to the player using
the random bag system. This will be on a single line.

The pieces are as follows:

    o
    I
    S
    Z
    L
    j
    T

Sample Inputs

None.
Sample Outputs

    LJOZISTTLOSZIJOSTJZILLTZISJOOJSIZLTZISOJTLIOJLTSZO
    OTJZSILILTZJOSOSIZTJLITZOJLSLZISTOJZTSIOJLZOSILJTS
    ITJLZOSILJZSOTTJLOSIZIOLTZSJOLSJZITOZTLJISTLSZOIJO

Note

Although the output is semi-random, you can verify whether it is likely to be
correct by making sure that pieces do not repeat within chunks of seven.
'''
import random

tetri = '''    O
    I
    S
    Z
    L
    J
    T
'''
output = ''
strng = tetri.split()
temp = ''
while True:
    item = random.choice(strng)
    if item not in temp:
        temp += item
        if len(temp) == 7:
            output += temp
            temp = ''
            # if there is 7 x 7 add one
            if len(output) == 49:
                topup = random.choice(strng)
                output += topup
                print(output)
                break