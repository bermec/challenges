''' Your challenge today is to write a program that can draw a checkered grid (like a chessboard) to any dimension. For instance, a 3 by 8 board might look like this:

*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************

Yours doesn't have to look like mine, you can make it look any way you want
(now that I think of it, mine looks kinda bad, actually). Also try to make it
scalable, so that if you want to make a 2 by 5 board, but with bigger squares,
it would print out:

*******************************
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*******************************
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*******************************

Have fun!

'''
n = input('Input size of pattern:  ')
n = int(n)
space = ' '
cross = '+'
for x in range(n + 1):
    print(((cross * n + space * (n - 1)) * n) + cross)
for x in range(n + 1):
    print(cross + (space * (n- 1) + cross * n) * n)