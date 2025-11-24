from random import sample
import string

def pick_name(): #sceglie nome casuale (2 lettere e 3 numeri)
    letters = sample(string.ascii_uppercase, 2) + sample(string.digits, 3)
    return ''.join(letters)

class Robot:

    def reset(self):
        # These are small: take two
        pick_name()
        self.name = pick_name()
        
    def __init__(self):
        self.name = pick_name()

    def __str__(self):
        return self.name 