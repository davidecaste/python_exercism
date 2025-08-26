#!/usr/bin/env python3

#semplice

def score(x, y):
    dist = (x**2 + y**2)**(1/2)
    if dist <= 1:
        return 10
    if dist <= 5:
        return 5
    if dist <= 10:
        return 1
    return 0


#booleani

def score_bool(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return (radius<=1)*5 + (radius<=25)*4 +(radius<=100)*1


#dizionario

def score_dict(x_coord, y_coord):
    point = (x_coord**2 + y_coord**2)
    scores = {
        point <= 100: 1,                    #una key duplicata riscrive il valore nella precedente!
        point <= 25: 5, 
        point <= 1: 10
    }
    
    return scores.get(True, 0)              #restituisce il valore di scores[True] o 0