#!/usr/bin/env python3

def leap_year(year):
    """determines if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def leap_year_ternary(year):
    """determines if a year is a leap year. Uses ternary operator."""
    return (not year % 400 if not year % 100 else not year % 4)                 #zero è falso! Quindi la prima condizione not year % 100 è verificata se year è divisibile per 100