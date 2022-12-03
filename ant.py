from point import Point
from calculator import *
import math

class Ant:
    def __init__(self, startingPointInd: int, allPoints: list, pheromoneMatrix: list):
        self.startingPointInd = startingPointInd
        self.allPoints = allPoints
        self.pheromoneMatrix = pheromoneMatrix
        self.remainingPoints = [i for i in range(0,len(allPoints))]
        self.remainingPoints.remove(self.startingPointInd)
        self.decisionMatrix = [[calcDecision(i, j, self.pheromoneMatrix, self.allPoints) for i in range(len(allPoints))] for j in range(len(allPoints))]
        self.path = []
        self.summaryDist = 0
        print("Remaining points in this ant: {}".format(self.remainingPoints))

    def findNext(self, currInd: int):
        maxProbability = 0
        maxInd = 0
        pointsToBeSearched = self.remainingPoints.copy()
        for nextInd in pointsToBeSearched:
            nextProbability = self.decisionMatrix[currInd][nextInd]
            if nextProbability > maxProbability:
                maxProbability = nextProbability
                maxInd = nextInd
        
        self.summaryDist += calcDist(self.allPoints[currInd], self.allPoints[maxInd])
        pointsToBeSearched.remove(maxInd)
        print("I want index {} to be removed".format(maxInd))
        return maxInd

    def findPath(self):
        currInd = self.startingPointInd
        while self.remainingPoints:     
            nextInd = self.findNext(currInd)
            self.path.append([currInd, nextInd])
            self.remainingPoints.remove(nextInd)
            currInd = nextInd
            print("Remaining points are: {}".format(self.remainingPoints))

        self.path.append([currInd, self.startingPointInd])

    def getPath(self):
        return self.path

    def getSummaryDist(self):
        return self.summaryDist

        