#!/usr/bin/env python3

def mult(limit, num):
    if num == 0:
        return set()
    res = set()
    k=1
    while num * k < limit:
        res.add(num*k)
        k+=1
    return res



def sum_of_multiples(limit, multiples):
    to_sum=set()
    for num in multiples:
        to_sum = to_sum.union(mult(limit, num))
    return sum(to_sum), to_sum


#breve

def sum_of_multiples(roof, starts):
    return sum(x for x in range(roof) if any(x%y == 0 for y in starts if y > 0))