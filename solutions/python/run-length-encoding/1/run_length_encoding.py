import string
to_use = string.ascii_letters + string.digits + ' '

def decode(word):
    if not set(word) <= set(to_use):
        raise ValueError('Unexpected character')

    res = '' #ci metto le lettere
    num = [] #ci metto i numeri

    for letter in word:
        if letter.isdigit():
            num.append(letter)
        else:
            if len(num) == 0:
                add = 1    #se non ho numeri è una lettera sola
            else:
                add = int(''.join(num))    #collezione tutti i numeri
            res += (letter * add) 
            num = []
    return res
            


def encode(word):
    if not set(word) <= set(to_use):
        raise ValueError('Unexpected character')

    act = ''    #che lettera sto guardando
    count = 1   #quante act ho viste
    res = ''    #da espandere
    for letter in word + '2':    #aggiungo un carattere non alfabetico per gestire l'ultima lettera
        if letter == act:
            count += 1
        else:
            if count == 1:
                res += act
            else:
                res += str(count) + act
            act = letter
            count = 1
    return res