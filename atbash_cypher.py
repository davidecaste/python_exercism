#!/usr/bin/env python3

import re

alphabet = ''.join([chr(i) for i in range(ord('a'),ord('z')+1)])
rev_alphabet = alphabet[::-1]
dict = str.maketrans(alphabet, rev_alphabet)



def encode(plain_text):
    clean = re.sub(r'[^a-zA-Z_0-9]', '', plain_text).lower()
    coded = clean.translate(dict)
    return ' '.join(coded[i:i+5] for i in range(0, len(coded), 5))


def decode(ciphered_text):
    return ciphered_text.replace(' ','').translate(dict)
