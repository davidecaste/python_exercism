trasl = {'M':1000, 'CM':900, 'D':500, 'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}

def roman(number):
    res = []
    for label in trasl:
        while number >= trasl[label]:
            res.append(label)
            number = number - trasl[label]

    return ''.join(res)
