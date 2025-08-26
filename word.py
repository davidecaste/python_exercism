#!/usr/bin/env python3

def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    question = question.strip()

    if not question:
        raise ValueError("syntax error")

    formula = question.split()
    while len(formula) > 1:
        try:
            x_value = int(formula[0])
            y_value = int(formula[2])
            symbol = formula[1]
            remainder = formula[3:]

            if symbol == "plus":
                formula = [x_value + y_value] + remainder
            elif symbol == "minus":
                formula = [x_value - y_value] + remainder
            elif symbol == "multiplied":
                formula = [x_value * y_value] + remainder
            elif symbol == "divided":
                formula = [x_value / y_value] + remainder
            else:
                raise ValueError("syntax error")
        except:
            raise ValueError("syntax error")

    return int(formula[0])


#oppure 

def answer(question):
    operators = {'minus': lambda a, b: a - b, 'plus': lambda a, b: a + b, 'multiplied': lambda a, b: a * b, 'divided': lambda a, b: a / b, 'power': lambda a, b: a**b}
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    if question.endswith("cubed?"):
        raise ValueError("unknown operation")
    word = question[8:-1].replace('by ', '').split(' ')    #rimuove what is e il punto di domanda
    res = []
    try:
        res = float(word[0])        #controlla se la prima parola è un numero
    except ValueError:
        raise ValueError("syntax error")
    for op in range(1, len(word), 2):                        #salto i numeri
        try:
            res = operators[word[op]](res, float(word[op + 1])) #applico l'operazione a op e op+1
        except KeyError:
            raise ValueError("syntax error")            #se ci sono parole non in operators
        except ValueError:
            raise ValueError("syntax error")            #se prima edopo una parola non ci sonodue numeri
        except IndexError:
            raise ValueError("syntax error")
    return res