#!/usr/bin/env python3

def square_root(number):                                        #ricerca binaria
    """return square root"""
    low = 1
    sup = number
    res = 1
    while (low <= sup):
        mid = low + (sup-low) // 2
        print(f'low:{low}, mid:{mid}, sup: {sup}')
        if mid * mid <= number:
            res = mid
            low = mid + 1
        else:
            sup = mid -1
    return res