DIC = {'AUG': 'Methionine', 
    'UUU':'Phenylalanine', 'UUC': 'Phenylalanine', 
    'UUA':'Leucine', 'UUG':'Leucine', 	
    'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine',
    'UAU':'Tyrosine', 'UAC':'Tyrosine',
    'UGU':'Cysteine', 'UGC':'Cysteine',
    'UGG':'Tryptophan',
    'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'} 	

def proteins(strand):
    prots = []
    for i in range(0, len(strand), 3):
        cod = strand[i:i+3]
        amin = DIC[cod]
        if (amin == 'STOP'):
            return prots
        else:
            prots.append(amin)
    return prots