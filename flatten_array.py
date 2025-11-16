#!/usr/bin/env python3

def flatten(iterable):
    res = []
    for item in iterable:
        if isinstance(item, list):
            res = [*res, *flatten(item)]
        elif item != None:
            res.append(item)
    return res
