# Globals for the directions
# Change the values as you see fit
NORTH = 'north'
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'
DIRECTIONS = {NORTH: (0,1), EAST:(1,0), SOUTH:(0, -1), WEST:(-1, 0)}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, dir):
        directions = list(DIRECTIONS.keys())
        for letter in dir:
            if letter == 'R':
                self.direction = directions[(directions.index(self.direction) + 1) % 4]
            if letter == 'L':
                self.direction = directions[(directions.index(self.direction) - 1) % 4]
            if letter == 'A':
                self.coordinates = tuple(map(sum, zip(self.coordinates, DIRECTIONS[self.direction])))
    
