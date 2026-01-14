def square_of_sum(n):
    #sum of first n natural numbers > n(n-1)/2
    return int(n*(n+1)/2)**2

def sum_of_squares(n):
    #sum of the square of first n natural numbers > n(n+1)(2n+1)/6
    return int(n*(n+1)*(2*n+1)/6)


def difference_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)
