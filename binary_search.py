#!/usr/bin/env python3

def find(search_list, value):
    lg = len(search_list)
    if lg ==0:
        raise ValueError('value not in array')    
    iniz = 0
    fine = lg-1
    while iniz <= fine:
        m = iniz + ((fine-iniz )// 2)
        if search_list[m] < value:
            iniz = m+1 
        elif search_list[m] > value:
            fine = m-1
        else:
            return m
    raise ValueError('value not in array')
    