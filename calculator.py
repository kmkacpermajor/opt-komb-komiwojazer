import math
from constants import *
from point import Point

def calcDist(a: Point, b: Point):
   
    ySub = a.y - b.y
    xSub = a.x - b.x

    return math.sqrt( xSub * xSub + ySub * ySub )

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result

    if power % 2 != 0:
        result = result * val
    return result


