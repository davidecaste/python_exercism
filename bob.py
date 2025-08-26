#!/usr/bin/env python3

def response(hey_bob_raw):
    "Answer depending on input"
    hey_bob=hey_bob_raw.strip()
    if hey_bob == '':
        return ("Fine. Be that way!" )
    elif hey_bob[-1]=='?' and not hey_bob.isupper():
        return("Sure.")
    elif hey_bob[-1]=='?': 
        return("Calm down, I know what I'm doing!")
    elif hey_bob.isupper():
        return("Whoa, chill out!")
    else:
        return("Whatever.")   
        
        
        
    #liste
    
ANSWERS = ['Whatever.', 'Sure.', 'Whoa, chill out!', "Calm down, I know what I'm doing!"]

def response(hey_bob):
    "Answers, depending on input."
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = 2 if hey_bob.isupper() else 0
    is_question = 1 if hey_bob.endswith('?') else 0
    return ANSWERS[is_shout + is_question] #l'addizione qua funziona da congiunzione logica