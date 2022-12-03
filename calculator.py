import math
from constants import *
from point import Point

def calcDist(a: Point, b: Point):
   
    ySub = a.y - b.y
    xSub = a.x - b.x

    return math.sqrt( xSub * xSub + ySub * ySub )

