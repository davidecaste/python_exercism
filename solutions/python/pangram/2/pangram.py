import string 

def is_pangram(sentence):
    """determine if a sentence is a pangram
    sentence: str"""
    if sentence == '':
        return False
    letters = string.ascii_lowercase
    for letter in letters:
        if letter not in set(sentence.lower()): 
            return False 
    return True 
    
    
