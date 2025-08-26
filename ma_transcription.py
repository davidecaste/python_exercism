#!/usr/bin/env python3

def to_rna(dna_strand):
    old = ['G', 'C', 'T', 'A']
    new = ['C', 'G', 'A', 'U']
    dict = {}
    for index, letter in enumerate(old):
        dict[ord(letter)] = ord(new[index])
    return dna_strand.translate(dict)


#Uguale ma meglio

def to_rna_short(dna_strand):
    repl = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(repl)


#Senza translate (più lento)
dict = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    return ''.join(dict[chr] for chr in dna_strand)