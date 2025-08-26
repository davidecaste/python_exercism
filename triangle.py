#!/usr/bin/env python3

def is_triangle(sides):
    """verify triangular inequalities
    sides = [x, y, z], x,y,z: int
    """
    if not sum(sides):
        return False
    else:
        for i in range(3):
            j, k = (i-1) % 3, (i+1) % 3
            if sides[i] > sides[j] + sides[k]:
                return False 
    return True 


def equilateral(sides):
    """check if all sides are equal
    sides = [x, y, z], x,y,z: int
    """
    return sides[0] == sides[1] and sides[1] == sides[2] and is_triangle(sides)


def isosceles(a, b, c):
    """check if two sides are equal
    sides = [x, y, z], x,y,z: int
    """
    if a == b or b == c or a == c:
        return True
    else:
        return False 


def scalene(a, b, c):
    """check if all sides are different
    sides = [x, y, z], x,y,z: int
    """
    return ( not equilateral([a, b, c]) ) and ( not isosceles([a, b, c]) )



# conciso

def equilateral_conc(sides):
    a, b, c = sorted(sides)
    return 0 < a == c #disuguaglianze automaticamente soddisfatte se il più piccolo è > 0

def isosceles_conc(sides):
    a, b, c = sorted(sides)
    return 0 < a and c < a + b and b in (a, c) #l'ultima condizione mi da che il triangolo è isoscele

def scalene_conc(sides):
    a, b, c = sorted(sides)
    return 0 < a < b < c < a + b   #mi basta sempre controllare solo il più grande!
