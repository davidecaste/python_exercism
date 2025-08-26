#!/usr/bin/env python3


COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    indexes = [str(COLORS.index(col)) for col in colors]
    return int(''.join(indexes[0:2]))


#dizionari

dict = {}
for num in range(10):
    dict[COLORS[num]]= num


def value_d(colors):
    return int(''.join(str(dict[colors[i]]) for i in range(len(colors))))