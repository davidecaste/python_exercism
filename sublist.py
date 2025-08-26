#!/usr/bin/env python3

"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sub_list(l1, l2): #determines if l1 is a sublist of l2
    n1 = len(l1)
    n2 = len(l2)
    return any(l2[i:i+n1] == l1 for i in range(n2 - n1 + 1))

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if sub_list(list_one, list_two):
        return SUBLIST
    if sub_list(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
