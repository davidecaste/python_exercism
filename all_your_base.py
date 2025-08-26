#!/usr/bin/env python3

def to_ten(b, l):    #convert a list of digits, representing a number in base b<=10 to the same number in base ten
    return sum( num * b**index for index, num in enumerate(l[::-1]))
       
def to_base(b, num):    #convert a number in base ten to a number in base b<=10
    dig = []
    while num // b != 0:
        dig.append(num%b)
        num = num // b
    dig.append(num)    
    return dig[::-1]

def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(num < 0 or input_base <= num for num in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    return to_base(output_base, to_ten(input_base, digits))


#meglio

def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any(num < 0 or input_base <= num for num in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    decimal = 0
    for d in digits:                            #converte in decimale
        decimal = decimal * input_base + d  
    
    if decimal == 0: return [0]
    
    out_digits = []
    while decimal > 0:
        decimal, digit = divmod(decimal, output_base)
        out_digits.insert(0, digit)                                             #inserisce in prima posizione
    return out_digits