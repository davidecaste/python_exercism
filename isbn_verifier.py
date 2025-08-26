#!/usr/bin/env python3

"""verifier of validity of isbn code"""

import re

def is_valid(isbn):
    scrubbed = isbn.replace('-', '')
    RE = re.compile(r'^\d{9}[\dX]$')    #9 cifre seguite da cifra o X finale 
    if not RE.match(scrubbed):
        return False

    digits = [int(d) if d != 'X' else 10 for d in scrubbed]
    somma = sum(d *(10 - index) for index, d in enumerate(digits))
    return not somma % 11