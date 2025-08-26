#!/usr/bin/env python3

"""translate a word in Pig Latin"""


#con insiemi e liste

vowels = 'aeiou'
vowels_2='aeiouy'

def translate(text):
    res = []
    for word in text.split():
        if word[0] in vowels or word[0:2] in {'xr', 'yt'}:
            res.append(word + "ay")
            continue

        for index in range(1, len(word)):
            if word[index] in vowels_2:                                                            #trova la prima vocale o y
                index += 1 if word[index] == 'u' and word[index - 1] == "q" else 0                  #se ho trovato una sequenza 'qu' mi sposto alla fine, altrimenti no
                res.append(word[index:] + word[:index] + "ay")                                    #inverto e aggiungo
                break

    return " ".join(res)



#con espressioni regolari

import re


#ho due gruppi: 1. (x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?) che matcha tutte le parole che cominciano in  x o t non seguite da r e t o parole che cominciano con 
# una vocale, tutto possibilmente seguito da 'qu'.
#               2. (.+)$ il resto della parola 

        
        
RE = re.compile('^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')                       


def translate_word(word):
    # lambda introduce una fuzione anonima
    # se il primo argomento di .sub è una funzione allora applico questa funzione ai match e uso il risultato come rimpiazzo
    # *m.groups() è la lista dei match, la funzione li scambia
    return RE.sub(lambda m: '{1}{0}ay'.format(*m.groups()), word)
        
def translate(phrase):
    return ' '.join(map(translate_word, phrase.split()))                                #map applica translate_word ad ogni componente della lista 
