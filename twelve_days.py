#!/usr/bin/env python3

days = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

text = ["Nowhere nohow",
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "]


def one_verse(days, text, start):
    verse = [f"On the {days[start]} day of Christmas my true love gave to me: "]

    if start == 1:
        # The first time we need to trim the "and " in a Partridge
        gifts = [text[1][4:]]
    else:
        gifts = [text[day] for day in range(1, start + 1)]

    return ''.join(verse + gifts[::-1])


def recite(start: int, finish: int) -> list:
    return [one_verse(days, text, i) for i in range(start, finish+1)]
