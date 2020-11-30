import random
from models.player import Player


class Maze:
    """
    This is the Maze class
    """

    wall_symbol = 'X'
    exit_symbol = 'E'
    player_symbol = 'P'
    space_symbol = ' '
    
    def __init__(self, filename):
        """
        make a nested list to store the maze map
        :param filename: we will use maze.txt file as param
        """
        self._map = []
        with open(filename) as f:
            # read the maze.txt file
            for line in f:
                # for each line in maze.txt
                row = []
                for char in line:
                    # for rach char in each line
                     if char != '\n':
                         row.append(char)
                        # append the char into the list
                self._map.append(row)
                # append the list into the nested list
        self._numRow = len(self._map)
        # get the rou number
        self._numCol = len(self._map[0])
        # get column number

        for i in range(0, 4):
            # get 4 random items
            while True:
                # find 4 random spots
                (x, y) = self.find_random_spot()
                if not self.is_item(x, y) and not self.is_exit(x, y):
                    break
            self._map[x][y] = str(i)

        self._player = Player()
        """
        Get a player class
        """
        while True:
            # get a random player spot
            (x, y) = self.find_random_spot()
            if not self.is_item(x, y) and not self.is_exit(x, y):
                break
        self._map[x][y] = self.player_symbol
        # use player_symbol to name the current position
        self._player_position = (x, y)
        # get the player position

    @property
    def map(self):
        return self._map

    @property
    def player_position(self):
        return self._player_position

    def can_move_to(self, line_number, column_number):
        # check if the spot is able to move
        try:
            char = self._map[line_number][column_number]
            return char != self.wall_symbol
        except:
            return False
    
    def is_item(self, line_number, column_number):
        # check if the spot is an item or not
        try:
            char = self._map[line_number][column_number]
            return char != self.wall_symbol and char != self.exit_symbol and char != self.player_symbol and char != self.space_symbol
        except:
            return False
    
    def is_exit(self, line_number, column_number):
        # check if the spot is the exit or not
        try:
            char = self._map[line_number][column_number]
            return char == self.exit_symbol
        except:
            return False
                

   
    def find_random_spot(self):
        # Find a random spot
        while True:
            x_position = random.randint(0, self._numRow - 1)
            y_position = random.randint(0, self._numCol - 1)
            if self.can_move_to(x_position, y_position):
                # if the list is an empty spot
                return (x_position, y_position)