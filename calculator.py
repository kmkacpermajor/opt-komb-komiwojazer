import math
from point import Point

def calcDist(a: Point, b: Point):
   
    ySub = a.y - b.y
    xSub = a.x - b.x

    return math.sqrt( xSub * xSub + ySub * ySub )

def calcDecision(i: int, j: int, pheromoneMatrix: list, allPoints: list):
    iPoint = allPoints[i]
    jPoint = allPoints[j]

    sumOfTau = 0
    sumOfEtaToBeta = 0

    for k in range(len(allPoints)):
        sumOfTau += pheromoneMatrix[k][i]
        try:
            sumOfEtaToBeta += math.pow(1/calcDist(iPoint, allPoints[k]), beta)
        except:
            pass

    tau = pheromoneMatrix[j][i]
    etaToBeta = math.pow(1/calcDist(iPoint, jPoint), beta)

    return tau*etaToBeta / sumOfTau*sumOfEtaToBeta