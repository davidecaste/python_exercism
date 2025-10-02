"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, *loc):
        self.health = 3
        self.x_coordinate = loc[0]
        self.y_coordinate = loc[1]
        Alien.total_aliens_created += 1
        
    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return True if self.health >0 else False
    
    def teleport(self, x,y):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, pos):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(lt):
    aliens = []
    for pos in lt:
        aliens.append(Alien(*pos))
    return aliens