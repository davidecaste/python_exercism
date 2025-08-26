#!/usr/bin/env python3

alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]

def rows(letter):
    ind = alphabet.index(letter)
    res = ['A'.center(2*ind+1)]
    if ind == 0:
        return res
    for index in range(1, ind+1):
        nstr = alphabet[index] + len(res[-1].strip())*' ' + alphabet[index]
        res.append(nstr.center(2*ind+1))
    return res + res[len(res)-2::-1]