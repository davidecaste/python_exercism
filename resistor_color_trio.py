#!/usr/bin/env python3

import math

COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

PREFIX = {0 : '', 1 : 'kilo', 2 : 'mega', 3 : 'giga'}

dict = {}
for num in range(10):
    dict[COLORS[num]]= num

def label(colors):
    nval =  int(''.join(str(dict[colors[i]]) for i in range(2)) +'0'*(dict[colors[2]]))
    pw = (int(math.log10(nval)) if nval != 0 else 0)//3
    return str(nval//(1000**pw)) + f" {PREFIX[pw]}ohms"