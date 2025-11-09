#!/usr/bin/env python3


#primo tentativo

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    dist = 0
    for ind, letter in enumerate(strand_a):
        if letter != strand_b[ind]:
            dist +=1
    return dist

#senza indici

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    dist = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            dist +=1
    return dist

#conciso

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    dist = 0
    return sum( a != b for a,b in zip(strand_a,strand_b))