import itertools
def transpose(text):
    lines = text.splitlines()
    res = itertools.zip_longest(*lines, fillvalue = '@')                #put a dummy value to save the spaces in the strings
    return '\n'.join(''.join(x).rstrip('@').replace('@', ' ') for x in res)    #remove the trailing dummies and put back ' ''