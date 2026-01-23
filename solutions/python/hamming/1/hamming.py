def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    dist = 0
    for ind, letter in enumerate(strand_a):
        if letter != strand_b[ind]:
            dist +=1
    return dist