from point import Point
import random

def readPointsFile(fileName: str):
    pointsArr = []
    with open(fileName) as pointsFile:
        pointsFile.readline() # wywalam sobie linie z ilością

        for pointString in pointsFile:
            pointString = pointString.strip().split(' ')
            pointString.pop(0)
            pointsArr.append(Point([int(pointCoord) for pointCoord in pointString]))
    
    return pointsArr
    
def generateFile(pointsArr: list, fileName: str):
    with open(fileName, "w") as pointsFile:
        pointsFile.write("{}".format(len(pointsArr)))
        i = 1
        for point in pointsArr:
            pointsFile.write("\n{} {} {}".format(i, point.x, point.y))
            i += 1

def generatePointsArray(n: int, rangeX=[-1000,1000], rangeY=[-1000,1000]):
    # generacja tablicy punktów
    allPoints = []
    for _ in range(n):
        x = random.randint(rangeX[0], rangeX[1])
        y = random.randint(rangeY[0], rangeY[1])
        allPoints.append(Point([x, y]))
    return allPoints
