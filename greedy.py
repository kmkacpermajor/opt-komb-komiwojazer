from point import Point

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

def findTSPResolution(allPoints: list):
    firstPoint = allPoints[0]
    currPoint = allPoints.pop(0)
    summaryDist = 0

    while allPoints:
        resArr = findShortestInd(allPoints, currPoint)
        currPoint = allPoints.pop(allPoints.index(resArr[0]))
        summaryDist += resArr[1]

    summaryDist += calcDist(currPoint, firstPoint)

    return summaryDist


