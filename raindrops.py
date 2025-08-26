#!/usr/bin/env python3

def convert(number):
    "convert number in the sounds of drop."
    div = [3, 5, 7]
    let = ['i', 'a', 'o']
    res = ''
    for i in range(3):
        if number % div[i] == 0:
            res = res + "Pl"+let[i]+"ng"
    return str(number) if not res else res


#dizionari

def convert_dict(number):
    sounds = {3 : 'Pling', 5 : 'Plang', 7: 'Plong'}
    
    res = ''.join(sounds[divisor] for divisor in sounds.keys() if number % divisor == 0) #generator - expression (più o meno come comprensione delle liste)

    return res or str(number)
            



#f-strings
def conver_str(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:
        if number % factor == 0:
            sounds += f'Pl{vowel}ng'
    
    return sounds or str(number)

