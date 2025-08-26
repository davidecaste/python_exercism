#!/usr/bin/env python3

def saddle_points(matrix):
    heigth= len(matrix)
    good = []
    if heigth == 0:
        return good
    width = len(matrix[0])
    for lst in matrix:
        if len(lst) != width:
            raise ValueError("irregular matrix")
    for row, lst in enumerate(matrix): 
        ma = max(lst)
        for i, val in enumerate(lst):
            if val == ma:
                good.append([row, i])
    dic = []
    for cp in good:
        colu = [matrix[row][cp[1]] for row in range(heigth)]
        if matrix[cp[0]][cp[1]] == min(colu):
            dic.append({'row':cp[0]+1, 'column': cp[1]+1})
    return dic   

#fatta bene 

def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')
    row_maxima = list(map(max, matrix))                         #massimi di ogni riga
    col_minima = list(map(min, list(zip(*matrix))))             #minimi sulle colonne: list(zip(*matrix)) produce la lista delle colonne
    return [{'row': r+1, 'column': c+1}
            for r, row_max in enumerate(row_maxima)
            for c, col_min in enumerate(col_minima)
            if row_max == col_min]