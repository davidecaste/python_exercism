#!/usr/bin/env python3

def divisor(number):                                #print list of divisor, minus number itself
    div = [1]
    for num in range(2, int(number**(1/2))+1):
        if number % num == 0:
            div.append(num)
            if number // num not in div:
                div.append (number // num)
    return div
    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return 'deficient'
   
    al = sum(divisor(number))
    dict = {
        al < number : 'deficient',
        al > number : 'abundant',
        al == number : 'perfect'
    }
    return dict[True]
    