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
        
    def __init__(self, symbol, row, col):
        ''' (Rat, str, int, int) -> NoneType
        '''   
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        
        
        
    
    def set_location(self, row, col):
        ''' (Rat,int, int) -> NoneType
        '''
        return [row][col]
        
        
    def eat_sprout(self):
        '''(Rat) -> Nonetype
        '''
        if set_location(self, row, col) == SPROUT:
            self.num_sprouts_eaten += 1

     
    def ___str___(self):
        ''' (Rat) -> str
        
        Return a string representation of the rar in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.
        '''
        "{0} + ' ' + 'at' + ' ' + '(' + {1} + ')'".format(self.symbol, self.row)


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    
    def __init__(self, maze, Rat_1, Rat_2):
        
        """(Maze, list of list of str, Rat, Rat) -> NoneType 
        
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
        ['#', '.', '.', '.', '.', '.', '#'], \
        ['#', '.', '#', '#', '#', '.', '#'], \
        ['#', '.', '.', '@', '#', '.', '#'], \
        ['#', '@', '#', '.', '@', '.', '#'], \
        ['#', '#', '#', '#', '#', '#', '#']], \
        Rat('P', 1, 1), Rat('J', 2, 4))
        """
        
        self.maze = maze
        self.Rat_1 = Rat_1
        self.Rat_2 = Rat_2
        self.num_sprouts_left = 0
        
    def is_wall(self, row, col):
        ''' (Maze, int, int) -> bool
        '''

        return maze[row][col] == WALL
        
        
    def get_character(self, row, col):
        ''' (Maze, int, int) -> str
        '''
        char = maze[row][col]
        return char

        
        
    def move(Rat, row, col):
        '''(Rat,int, int) -> bool
        '''
        row_temp = row
        col_temp = col
        if row_temp < len(row) and col_temp < len(col)and Maze.is_wall == False:
            return True
            
        
    def __str__(self):
        ''' (Maze) -> str
        '''

        return "{0} + ' at ' + '(' + {1} + ',' + {2} + ')' + ' ate ' + {3} + ' sprouts.'" \
            .format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
       


if __name__  == '__main__':
    maze = Maze([['#', '.', '.', '.', '@', '.', '#'],
            ['#', '.', '#', '#', '#', '.', '#'],
            ['#', '.', '.', '#', '@', '.', '#'],
            ['#', '@', '#', '.', '@', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#']], Rat('P', 1, 1), Rat('J', 1, 3,))

    ans = Rat('P', 1, 4)
    print(ans)

