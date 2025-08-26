#!/usr/bin/env python3

def dec_bin(num):
    res = []
    while num > 0:
        res.insert(0, num % 2)
        num //= 2
    return res

def egg_count(display_value):
    return sum(dec_bin(display_value))