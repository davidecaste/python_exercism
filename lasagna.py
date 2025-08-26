#!/usr/bin/env python3
#esercizio 1 di Exercism


"""Functions used in preparing Guido's gorgeous laeturn the total number of minutes you have been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.sagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return 40 - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Compute the preparation time depending to the layers added to the lasagna
       :param number of layers:int - number of layers of lasagna
       :return:int - total time needed

    PREPARATION_TIME is the time needed for layer
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """The function return the total number of minutes you have been cooking, or the sum of your preparation time and the time the        lasagna has already spent baking in the oven.
    :param number_of_layers:int, elapsed_bake_time:int
    :return:int"""
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)