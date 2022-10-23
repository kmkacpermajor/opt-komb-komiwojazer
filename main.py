import math

class Point():
    def __init__(self, pointArr):
        self.x = pointArr[0]
        self.y = pointArr[1]

    def y(self):
        return self.y

    def x(self):
        return self.x

def calcDist(a: Point, b: Point):
   
    ySub = a.y - b.y
    xSub = a.x - b.x

    return math.sqrt( xSub * xSub + ySub * ySub )

def findShortestInd(allPoints: list, currPoint: Point):
    minDist = None
    minPoint = None
    for nextPoint in allPoints:
        if minDist == None:
            minDist = calcDist(nextPoint, currPoint)
            minPoint = nextPoint
        else:
            dist = calcDist(nextPoint, currPoint)
            if dist < minDist:
                minDist = dist
                minPoint = nextPoint

    return minPoint, minDist


fileName = "przyklad.txt"

try:
    with open(fileName) as pointsFile:
        n = int(pointsFile.readline())
        points = []

        for pointString in pointsFile:
            points.append(Point([int(pointCoord) for pointCoord in pointString.split(' ')])) 

        firstPoint = points[0]
        currPoint = points.pop(0)
        summaryDist = 0

        while points:
            resArr = findShortestInd(points, currPoint)
            currPoint = points.pop(points.index(resArr[0]))
            summaryDist += resArr[1]

        summaryDist += calcDist(currPoint, firstPoint)

        print('TSP summary distance: {}'.format(summaryDist))
except FileNotFoundError:
    print("File doesn't exist")


