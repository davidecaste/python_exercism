#!/usr/bin/env python3

"""Determine if a word or a phrase is an isogram (no repeated letters)"""

#counters
from collections import Counter

def is_isogram(string):
    count = Counter(string.lower())
    for letter in count:
        if count[letter] > 1 and letter.isalpha():
            return False
    return True



#dictionaries

def letter_count(string):
    dic = {}
    for letter in string.lower():
        if letter.isalpha():
            count = dic.setdefault(letter, 0)
            dic[letter] = count + 1
    return dic

def is_isogram_dic(string):
    count = letter_count(string)
    for letter in count:
        if count[letter] > 1:
            return False
    return True


#sets

def is_isogram_set(string):
    clean = [letter for letter in string.lower() if letter.isalpha() ]
    to_check = set(clean)
    return len(clean) == len(to_check)

#regex

import re

def is_isogram(string):
    RE = re.compile('[^a-zA-Z]')
    scrubbed = RE.sub('', string).lower()
    return len(scrubbed) == len(set(scrubbed))