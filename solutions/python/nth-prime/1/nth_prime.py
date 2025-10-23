def prime_check(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5) +1):
        if n % k == 0:
            return False
    return True     

def prime_generator():
    n = 2
    while True:
        if prime_check(n):
            yield n
        n+=1

def prime(number):
    if number < 0:
        raise ValueError('No such prime')
    if number == 0:
        raise ValueError('there is no zeroth prime')
    gen = prime_generator()
    return [next(gen) for i in range(number)][-1]