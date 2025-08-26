#!/usr/bin/env python3
def primes(limit):
    res = list(range(2, limit+1))
    for n in res:
        res = [x for x in res if (x<=n or x%n != 0)]
    return res


#peggiore
def primes_worst(limit):
    nums = set(range(2, limit+1))
    marks = {x for y in nums for x in range(2*y, limit + 1, y) }
    return sorted(nums - marks)