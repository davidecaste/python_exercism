#!/usr/bin/env python3

def let_co(word):
    dic = {}
    for letter in word:
        count = dic.setdefault(letter, 0)
        count += 1
        dic[letter] = count
    return dic

def is_an(word, wrd):
    return let_co(word.lower()) == let_co(wrd.lower()) and word.lower() != wrd.lower()     

def find_anagrams(word, candidates):
    return [wrd for wrd in candidates if is_an(word, wrd)]    


#più corto

def detect_anagrams(word, pool):
    return [i for i in pool if sorted(i.lower()) == sorted(word.lower()) and i.lower() != word.lower()]