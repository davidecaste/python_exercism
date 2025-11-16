def factors(num):
    res = []
    div = 2
    while  num > 1:
        if num % div == 0:
            num /= div
            res.append(div)
        else:
            if div == 2:
                div +=1
            else:
                div+=2
    return res
            
