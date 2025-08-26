#!/usr/bin/env python3

#fatto malone

import math

COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
tol = {'grey' : 0.05, 'violet' : 0.1, 'blue' : 0.25, 'green' : 0.5, 'brown' : 1, 'red' : 2, 'gold' : 5, 'silver' : 10}
PREFIX = {0 : '', 1 : 'kilo', 2 : 'mega', 3 : 'giga'}

dt = {}
for num in range(10):
    dt[COLORS[num]]= num

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        nval =  int(''.join(str(dt[colors[i]]) for i in range(2)) +'0'*(dt[colors[2]]))
        pw = (int(math.log10(nval)) if nval != 0 else 0)//3
        if nval%(1000**pw) == 0:
            return str(nval//(1000**pw)) + f" {PREFIX[pw]}ohms" + f" ±{tol[colors[-1]]}%"
        return str(nval/(1000**pw)) + f" {PREFIX[pw]}ohms" + f" ±{tol[colors[-1]]}%"
    if len(colors) == 5:
        nval =  int(''.join(str(dt[colors[i]]) for i in range(3)) +'0'*(dt[colors[3]]))
        pw = (int(math.log10(nval)) if nval != 0 else 0)//3
        if nval%(1000**pw) == 0:
            return str(nval//(1000**pw)) + f" {PREFIX[pw]}ohms" + f" ±{tol[colors[-1]]}%"
        return str(nval/(1000**pw)) + f" {PREFIX[pw]}ohms" + f" ±{tol[colors[-1]]}%"
    
    
#fatto meglio
    
COLORS = "black brown red orange yellow green blue violet grey white".split()
TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}
UNITS = ["ohms", "kiloohms", "megaohms"]

def resistor_label(colors):
    # set up variables
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, COLORS[0], None

    # sum values and multiply 
    val = 0.0
    for value in values:
        val = val * 10 + COLORS.index(value)
    val *= 10 ** COLORS.index(multiplier)
    # Shift numbers over to get the proper prefix.
    power = 0
    while val >= 1000:
        val /= 1000
        power += 1
    result = f"{val:n} {UNITS[power]}"
    # Add a tolerance, if one is supplied.
    if tolerance:
        result += f" ±{TOLERANCES[tolerance]}%"
    return result