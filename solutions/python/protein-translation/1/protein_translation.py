DIC = {'AUG': 'Methionine', 
    'UUU':'Phenylalanine', 'UUC': 'Phenylalanine', 
    'UUA':'Leucine', 'UUG':'Leucine', 	
    'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine',
    'UAU':'Tyrosine', 'UAC':'Tyrosine',
    'UGU':'Cysteine', 'UGC':'Cysteine',
    'UGG':'Tryptophan',
    'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'} 	

def split_by_three(word):
    res = []
    n = 0
    while 3*n < len(word):
        res.append(word[3*n:3*(n+1)])
        n +=1
    return res

def proteins(strand):
    codons = split_by_three(strand)
    prot = []
    for cod in codons:
        if DIC[cod] == 'STOP':
            return prot
        else:
            prot.append(DIC[cod])
    return prot