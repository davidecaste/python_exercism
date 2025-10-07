from random import choice

class Character:
    def __init__(self):
        self.constitution = points() 
        self.strength = points()
        self.dexterity = points()
        self.intelligence = points()
        self.wisdom = points()
        self.charisma = points()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([item for item in vars(self).values()])

def points():
    rolls = sorted([choice(range(1,7)) for num in range(4)], reverse = True)
    return sum(rolls[:2])

def modifier(constitution):
    return (constitution - 10 )//2
