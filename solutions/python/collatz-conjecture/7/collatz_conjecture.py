def steps(number):
    """return the number of steps needed to reach 1 with the Collatz procedure. Use ternary operator.
    number: int 
    """
    if number > 0:
        a = number 
        count = 0
        while a != 1:
           count +=1
           a = a / 2 if a % 2 == 0 else a * 3 + 1
        return count
    else:
        raise ValueError("Only positive integers are allowed")  