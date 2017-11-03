# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init(self, row, col, symbol, num_sprouts_eaten = 0):

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType
        '''
        return self.row, self.col

    def eat_sprout(self):
        '''(Rat -> NoneType
        '''
        self.num_sprouts_eaten += 1

    def __str__(self):
        ''' Rat -> str
        '''
        "{0} at ({1},{2}) ate {3) sprouts" .format \
            (self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """
    def __init__(self, maze, Rat, Rat2):
        ''' (Maze, list of list of str, Rat, Rat -> NoneType
        '''
        pass

    def is_wall(self, maze, rat, rat2):
        ''' (Maze, int, int) -> bool
        '''
        pass

    def get_character(self, Maze, Rat, int, int2):
        ''' (Maze, int, int) -> str '''
        pass

    def move(self, maze, rat, int, int2):
        '''(Maze, Rat, int, int) -> bool '''
        pass

    def __str__(self):
        ''' (Maze) -> str '''

        "{0} at ({1},{2}) ate {3) sprouts" .format \
            (self.symbol, self.row, self.col, self.num_sprouts_eaten)


