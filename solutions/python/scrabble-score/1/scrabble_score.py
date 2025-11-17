DIC = {'AEIOULNRST':1, 'DG':2, 'BCMP':3, 'FHVWY':4, 'K':5, 'JX':8, 'QZ':10}

def score(word):
    word = word.upper()
    sum = 0
    for letter in word:
        for key in DIC:
            if letter in set(key):
                sum+=DIC[key]
    return sum
