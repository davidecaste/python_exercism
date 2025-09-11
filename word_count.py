#!/usr/bin/env python3

import string 
def count_words(sentence):
    PUNCT = (string.punctuation + string.whitespace).replace("'", "")
    for p in PUNCT:
        sentence = sentence.replace(p, ' ')
    dict = {} 
    words = sentence.split()
    for word in words:
        if word not in dict.keys():
            dict(word) = 1
        else:
            dict(word) += 1
    return dict 