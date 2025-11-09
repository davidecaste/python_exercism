versi = ['the house that Jack built.', 'the malt that lay in', 'the rat that ate', 'the cat that killed', 'the dog that worried',
        'the cow with the crumpled horn that tossed','the maiden all forlorn that milked','the man all tattered and torn that kissed', 
        'the priest all shaven and shorn that married', 'the rooster that crowed in the morn that woke', 'the farmer sowing his corn that kept', 
        'the horse and the hound and the horn that belonged to']

        
def recita_un(num):
    lst = ['This is'] + [versi[val] for val in range(num, -1, -1) ]
    return ' '.join(lst)

        
def recite(start_verse, end_verse):
    return [ recita_un(verse-1) for verse in range(start_verse, end_verse+1) ]