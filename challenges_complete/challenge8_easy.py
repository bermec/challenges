''' write a program that will print the song "99 bottles of beer on the wall".

for extra credit, do not allow the program to print each loop on a new line.

'''

for x in range(99, 0, -1):
    if x == 1:
        print("{0} green bottle hanging on the wall, {0} green bottle hanging on the wall, and if one green "
              "bottle should accidentally fall there would be {1} green bottles hanging on the wall.".format(x, x - 1))
    while x > 1:

        print(('{0} green bottles hanging on the wall, {0} green bottles hanging on the wall, '
              'and if one green bottle should accidentally fall there would be {1} green bottles hanging on the wall. '
              .format(x, x - 1)), end='')
        break
