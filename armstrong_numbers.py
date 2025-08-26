#!/usr/bin/env python3

def is_armstrong_number(number):
    """return True if number is equal to the sum of its digits raised to the number of digits
    number : int
    """
    
    string_number = str(number)
    length = len(string_number)
    arm_sum = 0
    for char in string_number:
        arm_sum += int(char)**length 
    return number == arm_sum