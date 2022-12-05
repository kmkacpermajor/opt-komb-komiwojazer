from point import Point
from calculator import *
import math

class Ant:
    def __init__(self, startingPointInd: int, allPoints: list, pheromoneMatrix: list, distanceMatrix: list):
        self.startingPointInd = startingPointInd
        self.allPoints = allPoints
        self.pheromoneMatrix = [row[:] for row in pheromoneMatrix]
        self.remainingPoints = [i for i in range(0,len(allPoints))]
        self.remainingPoints.remove(self.startingPointInd)
        self.distanceMatrix = distanceMatrix
        self.decisionMatrix = [[self.calcDecision(j, i) for i in range(len(allPoints))] for j in range(len(allPoints))]
        if logLevel > 0:
            print(f"Mrówka {startingPointInd}")
            for row in self.decisionMatrix:
                print(row)
        self.path = []
        self.summaryDist = 0
        if logLevel > 0:
            print(f"Ant with starting point {self.startingPointInd}")

    def findNext(self, currInd: int, greedy: bool = False):
        bestInd = 0
        optimalDist = 0
        pointsToBeSearched = self.remainingPoints.copy()

        # print(f"decision matrix for {currInd}")
        # self.printPheromoneMatrix()
        if not greedy:
            maxProbability = 0
            for nextInd in pointsToBeSearched:
                nextProbability = self.decisionMatrix[currInd][nextInd]
                if nextProbability > maxProbability:
                    maxProbability = nextProbability
                    bestInd = nextInd

            optimalDist = self.distanceMatrix[bestInd][currInd]
        else:
            minDist = None
            for nextInd in pointsToBeSearched:
                if minDist == None:
                    minDist = self.distanceMatrix[nextInd][currInd]
                    bestInd = nextInd
                else:
                    if self.distanceMatrix[nextInd][currInd] < minDist:
                        minDist = self.distanceMatrix[nextInd][currInd]
                        bestInd = nextInd
            optimalDist = minDist

        pointsToBeSearched.remove(bestInd)
        if logLevel > 0:
            print("I chose index {} to be next".format(bestInd))
        self.summaryDist += optimalDist

        return bestInd

    def findPath(self, greedy: bool = False):
        currInd = self.startingPointInd
        while self.remainingPoints:     
            if not greedy:
                nextInd = self.findNext(currInd)
            else:
                nextInd = self.findNext(currInd, True)
            self.path.append([currInd, nextInd])
            self.remainingPoints.remove(nextInd)
            currInd = nextInd
            if logLevel > 0:
                print("Remaining points are: {}".format(self.remainingPoints))

        self.path.append([currInd, self.startingPointInd])
        self.summaryDist += self.distanceMatrix[self.startingPointInd][currInd]

    def calcDecision(self, i: int, j: int):
        if i!=j:
            sumOfTau = 0
            sumOfEtaToBeta = 0

            for k in range(len(self.allPoints)):
                sumOfTau += self.pheromoneMatrix[i][k]
                try:
                    sumOfEtaToBeta += 1/self.distanceMatrix[i][k]
                except:
                    pass

            tau = self.pheromoneMatrix[i][j]
            etaToBeta = 1/self.distanceMatrix[i][j]

            return tau*etaToBeta / sumOfTau*sumOfEtaToBeta
        else:
            return 0

    def getPath(self):
        return self.path

    def getSummaryDist(self):
        return self.summaryDist

    def printPheromoneMatrix(self):
        for j in range(len(self.pheromoneMatrix)):
            print(f"{j}:", end="")
            for i in range(len(self.pheromoneMatrix[j])):
                print(f"{self.pheromoneMatrix[j][i]} ", end="")
            print("")

        