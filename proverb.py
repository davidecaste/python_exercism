#!/usr/bin/env python3

def proverb(*input_data, qualifier=None):
    res = [f'For want of a {first} the {second} was lost.' for first, second in zip(input_data, input_data[1:])]
    if len(input_data) != 0:
        final = input_data[0] if qualifier == None else f'{qualifier} {input_data[0]}'
        res.append(f'And all for the want of a {final}.')
    return res 