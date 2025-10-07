#!/usr/bin/env python3

secs_in_year = 31557600
CONV = {'mercury':0.2408467, 'venus':0.61519726, 'mars' : 1.8808158, 'jupiter':11.862615, 'saturn' : 29.447498, 'uranus':84.016846, 'neptune' :164.79132 }

class SpaceAge:
    def __init__(self, seconds):
        self.earth_age = seconds/secs_in_year

    def on_earth(self):
        return round(self.earth_age, 2)

    def on_mercury(self):
        return round(self.earth_age/CONV['mercury'],2)
        
    def on_venus(self):
        return round(self.earth_age/CONV['venus'],2)
        
    def on_mars(self):
        return round(self.earth_age/CONV['mars'], 2)

    def on_jupiter(self):
        return round(self.earth_age/CONV['jupiter'], 2)
        
    def on_saturn(self):
        return round(self.earth_age/CONV['saturn'], 2)

    def on_uranus(self):
        return round(self.earth_age/CONV['uranus'], 2)
        
    def on_neptune(self):
        return round(self.earth_age/CONV['neptune'], 2)


#higher order

import functools

secs_in_year = 31557600
CONV = {'mercury':0.2408467, 'venus':0.61519726, 'mars' : 1.8808158, 'jupiter':11.862615, 'saturn' : 29.447498, 'uranus':84.016846, 'neptune' :164.79132, 'earth':1 }

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds/secs_in_year
        for planet, ratio in CONV.items():
            setattr(self, f"on_{planet}", functools.partial(self.years_planet, ratio))

    def years_planet(self, ratio):
        return round(self.years / ratio, 2)