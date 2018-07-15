'''
The world championship in Tic Tac Toe, The X-Games is underway. We have been asked to
write a program to see if there is a winning move possible. This tool will be used by
live commentators to use in their play by play.
input

(Next player's Move either an X or an O)

(3 x 3 grid showing the current game)

The grid can have 3 characters

    X for spot held by the X player
    O for spot held by the O player
    - for an empty spot

Example Input 1:

X
XX-
-XO
OO-

Example Input 2:

O
O-X
-OX
---

Example Input 3:

X
--O
OXX
---

Output:

Shows the board with the winning move in place. If there is no winning move
print out "No winning move"
Example Output 1:

XXX
-XO
OO-

Example Output 2:

O-X
-OX
--O

Example Output 3:

No Winning Move!

Extra Challenge:

    Boards where several moves can "win" display all boards showing the winning moves
    with a message saying how many wins are possible
    Boards with no winning move -- suggest a "block" move the player should make
    The world championship in Tic Tac Toe, The X-Games is underway. We have been asked to write a program to see if there is a winning move possible. This tool will be used by live commentators to use in their play by play.
input

(Next player's Move either an X or an O)

(3 x 3 grid showing the current game)

The grid can have 3 characters

    X for spot held by the X player
    O for spot held by the O player
    - for an empty spot

Example Input 1:

X
XX-
-XO
OO-

Example Input 2:

O
O-X
-OX
---

Example Input 3:

X
--O
OXX
---

Output:

Shows the board with the winning move in place. If there is no winning move print out "No winning move"
Example Output 1:

XXX
-XO
OO-

Example Output 2:

O-X
-OX
--O

Example Output 3:

No Winning Move!

Extra Challenge:

    Boards where several moves can "win" display all boards showing the winning moves with a message
    saying how many wins are possible
    Boards with no winning move -- suggest a "block" move the player should make instead with a
    message saying "No winning move: Block here"
instead with a message saying "No winning move: Block here"

'''



def next_move(l, n):
    l = list(l)
    flag = False
    for x in range(0, len(l)):
        if l[x] == '-':
            l[x] = n
            if l.count(n) == 3:
                flag = True
                return l
            else:
                l[x] = '-'
    return flag


game1 = '''x
xx-
-xo
oo-'''

game2 = '''o
o-x
-ox
---'''

game3 = '''x
--o
oxx
---'''

game_collection = [game1, game2, game3]
for game in game_collection:
    the_game = game.splitlines()
    for strng in the_game:
        print(strng)
    the_game[1][2] = 'x'
    the_move = the_game[0]
    print('> ', the_game)
    first_move = the_game[1][0] + the_game[1][1] + the_game[1][2]
    second_move = the_game[2][0] + the_game[2][1] + the_game[2][2]
    third_move = the_game[3][0] + the_game[3][1] + the_game[3][2]
    fourth_move = the_game[1][0] + the_game[2][0] + the_game[3][0]
    fifth_move = the_game[1][1] + the_game[2][1] + the_game[3][1]
    sixth_move = the_game[1][2] + the_game[2][2] + the_game[3][2]
    next_move1 = the_game[1][0] + the_game[2][1] + the_game[3][2]
    next_move2 = the_game[1][2] + the_game[2][1] + the_game[3][0]




    moves = [first_move, second_move, third_move, fourth_move, fifth_move, sixth_move, next_move1, next_move2]
    accum = 0
    for move in moves:
        ans = next_move(move, the_move)
        if ans:
            print('win!')
            break
        else:
            accum += 1
            if accum == 8:
                print('fail')
                accum = 0
            continue
