def triplets_with_sum(n):
    trip = []
    for a in range(1, int(n/3)+1):
        c = (n**2 - 2*a*n + 2*a**2) / (2*(n - a))
        b = n - a - int(c)
        if (not (c).is_integer()) or b <= a:
            continue 
        trip.append([a,b,int(c)])
    return trip 