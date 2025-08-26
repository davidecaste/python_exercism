#!/usr/bin/env python3

brackets = {'(':')', '[':']', '{':'}'}
brcs = {'(', ')', '[',']', '{','}'}

def is_paired(input_string):
    to_check = []
    for symbol in input_string:
        if symbol not in brcs:                                        #se non è una parentesi passa al simbolo successivo
            continue
        if symbol in brackets:                                        #se è una parentesi aperta aggiungi alla lista da controllare
            to_check.append(symbol)
        elif not to_check or brackets[to_check[-1]] != symbol:        #se è una parentesi chiusa e la lista da controllare è vuota o l'ultimo elemento non combacia allora ritorna falso
            return False
        else:                                                         #ho chiuso la parentesi
            to_check.pop()
    return not to_check                                               #se la lista non è vuota allora ritorna falso
