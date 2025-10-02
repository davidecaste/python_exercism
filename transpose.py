#!/usr/bin/env python3

import itertools
def transpose(text):
    lines = text.splitlines()
    res = itertools.zip_longest(*lines, fillvalue = ' ')
    return '\n'.join(''.join(x).rstrip('@').replace('@', ' ') for x in res)