from point import Point
from calculator import *
import math

class Ant:
    def __init__(self, startingPointInd: int, allPoints: list, pheromoneMatrix: list):
        self.startingPointInd = startingPointInd
        self.allPoints = allPoints
        self.pheromoneMatrix = pheromoneMatrix
        self.remainingPoints = [i for i in range(0,len(allPoints))].pop(self.startingPointInd)
        self.decisionMatrix = [[calcDecision(i, j, self.pheromoneMatrix, self.allPoints) for i in range(len(allPoints))] for j in range(len(allPoints))]
        self.path = []
        self.summaryDist = 0

    def findNext(self, currInd: int):
        maxProbability = 0
        maxInd = 0
        for nextInd in self.remainingPoints:
            nextProbability = self.decisionMatrix[currInd][nextInd]
            if nextProbability > maxProbability:
                maxProbability = nextProbability
                maxInd = nextInd
        
        self.summaryDist += calcDist(self.allPoints[currInd], self.allPoints[maxInd])
        self.remainingPoints.pop(self.allPoints.index(maxInd))
        return maxInd

    def findPath(self):
        currInd = self.startingPointInd
        while self.remainingPoints:
            nextInd = findNext(currInd)
            self.path.append([currInd, nextInd])

        self.path.append([currInd, startingPointInd])

    def getPath(self):
        return self.path

    def getSummaryDist(self):
        return self.summaryDist

        