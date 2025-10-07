#!/usr/bin/env python3

import re
def ope(x):
    return 2*x if 2*x <9 else 2*x - 9

class Luhn:
    def __init__(self, card_num):
        self.id = card_num

    def valid(self):
        to_check=self.id.replace(' ', '')
        if re.search(r'[^0-9]', to_check):
            return False
        l = [int(n) if k%2==0 else ope(int(n)) for k, n in enumerate(to_check[::-1])]
        return sum(l) % 10 == 0 and len(l) > 1

