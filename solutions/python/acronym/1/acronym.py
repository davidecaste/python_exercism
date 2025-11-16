import string 
punct = string.punctuation.translate(str.maketrans('','', '-'))    #punctuation minus -

def abbreviate(words):
    list=words.translate(str.maketrans('-',' ',punct)).split()     #removes elements of punct and then split
    return ''.join([word[0].upper() for word in list])
