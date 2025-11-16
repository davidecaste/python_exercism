#!/usr/bin/env python3

def append(list1, list2):
    return [*list1, *list2]

def concat(lists):
    res = []
    for list in lists:
        res = [*res, *list]
    return res


def filter(function, list):
    return [item for item in list if function(item) == True]


def length(list):
    d = 0
    for item in list:
        d += 1
    return d


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for item in list[::-1]:
        acc = function(acc, item)
    return acc

def reverse(list):
    return list[::-1]
