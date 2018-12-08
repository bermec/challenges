'''
This week all challenges will be inspired by the game Flash Point

The game is a fun cooperative game, where a bunch of fire(wo)men try to rescue victims
in a burning building.

Each round the fire is spreading, and it is this mechanic that we are going to implement.
Formal Inputs & Outputs
Input description

You recieve a floorplan of the building with the current situation on it.
The floorplan is a grid and all tiles are connected vertically and horizontally.
There is never ever a diagonally interaction.

Here is the legend to what is what:

S <- smoke
F <- fire
# <- wall
| <- closed door
/ <- open door
= <- damaged wall
_ <- broken wall or broken door
  <- Open space (blank space)

After the floorplan you will recieve a bunch off coordinates ((0,0)
is top left coord).

Each of these coordinates indicate where smoke developes.
Depending on the tile it lands can have various outcomes:

S -> S becomes F, smoke turns into fire
F -> Nothing happens
# -> invalid move
| -> invalid move
/ -> invalid move
= -> invalid move
_ -> invalid move
  ->   becomes S, Smoke develops on a blank spot

Additional rules:

    Fire and smoke: When smoke is next to a fire itself turns into a fire

    Doors and broken walls: doors and broken walls (or broken doors)
    connect to spaces. This means that if smoke is at one side and fire
    at the other the smoke turns into fire

Small house:

#############/#
#     |       #
#     #       #
#     #       #
#######       #
#     _       #
###############

Small house Input

1 1
1 2
1 3
5 6
4 2
1 1
1 2
5 5
5 5
9 1
5 7
2 2

Output description

Show the final Output

#############/#
#F    |  S    #
#FF   #       #
#F    #       #
#######       #
#    F_F      #
###############

'''