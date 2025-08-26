#!/usr/bin/env python3

"""Caesar's cypher"""

alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
ALPHABET = [chr(i) for i in range(ord('A'),ord('Z')+1)]
lgt = len(alphabet)
def rotate_word(word, key):
    word2 = ''
    for letter in word: 
        if letter in alphabet:
            ind = alphabet.index(letter)
            word2 = word2 + alphabet[(ind + key) % lgt]
        if letter in ALPHABET:
            ind = ALPHABET.index(letter)
            word2 = word2 + alphabet[(ind + key) % lgt]
        else:
            word2 = word2 + letter
    return word2

def rotate(text, key):
    words = text.split()
    new_text = [rotate_word(word, key) for word in words]
    return ' '.join(new_text)