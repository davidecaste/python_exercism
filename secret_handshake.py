#!/usr/bin/env python3

ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']

def commands(binary_str):
    to_do = []
    for ind, letter in enumerate(binary_str[4:0:-1]):
        if letter == '1':
            to_do.append(ACTIONS[ind])
    return to_do if binary_str[0] == '0' else to_do[::-1]