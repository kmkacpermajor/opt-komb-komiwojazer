import random
from point import Point
from calculator import *
import math
from decimal import *

class Ant:
    def __init__(self, startingPointInd: int, allPoints: list, pheromoneMatrix: list, distanceMatrix: list):
        self.startingPointInd = startingPointInd
        self.allPoints = allPoints
        self.pheromoneMatrix = [row[:] for row in pheromoneMatrix.copy()]
        self.remainingPoints = [i for i in range(0,len(allPoints))]
        self.remainingPoints.remove(self.startingPointInd)
        self.distanceMatrix = distanceMatrix
        self.path = []
        self.summaryDist = 0
        if logLevel > 0:
            print(f"Ant with starting point {self.startingPointInd}")

    def findNext(self, currInd: int, lookPheromone: bool = False, greedy: bool = False):
        bestInd = 0
        optimalDist = 0
        pointsToBeSearched = self.remainingPoints.copy()

        if not greedy:
            if not lookPheromone:
                maxProbability = 0
                for nextInd in pointsToBeSearched:
                    nextProbability = self.calcDecision(currInd,nextInd, pointsToBeSearched)
                    if nextProbability > maxProbability:
                        maxProbability = nextProbability
                        bestInd = nextInd
            else:
                maxPheromone = 0
                for nextInd in pointsToBeSearched:
                    nextPheromone = self.pheromoneMatrix[currInd][nextInd]
                    if nextPheromone > maxPheromone:
                        maxPheromone = nextPheromone
                        bestInd = nextInd
        else:
            minDist = None
            for nextInd in pointsToBeSearched:
                if minDist == None or self.distanceMatrix[nextInd][currInd] < minDist:
                    minDist = self.distanceMatrix[nextInd][currInd]
                    bestInd = nextInd
            optimalDist = minDist

        optimalDist = self.distanceMatrix[currInd][bestInd]

        if logLevel > 0:
            print("I chose index {} to be next".format(bestInd))
        self.summaryDist += optimalDist

        return bestInd

    def findPath(self, lookPheromone: bool = False, greedy: bool = False):
        currInd = self.startingPointInd
        while self.remainingPoints:     
            if greedy:
                nextInd = self.findNext(currInd, greedy = True)
            else:
                if lookPheromone:
                    nextInd = self.findNext(currInd, True)
                else:
                    nextInd = self.findNext(currInd, False)
            self.path.append([currInd, nextInd])
            self.remainingPoints.remove(nextInd)
            currInd = nextInd
            if logLevel > 0:
                print("Remaining points are: {}".format(self.remainingPoints))

        self.path.append([currInd, self.startingPointInd])
        self.summaryDist += self.distanceMatrix[self.startingPointInd][currInd]

    def calcDecision(self, i: int, j: int, toBeSearched: list):
        if i!=j:
            mianownik = 0

            for k in toBeSearched:
                tau = self.pheromoneMatrix[i][k]
                eta = 1/self.distanceMatrix[i][k]
                tauToAlpha = optimize(tau,alpha)
                etaToBeta = optimize(eta,beta)
                mianownik += tauToAlpha*etaToBeta

            tau = self.pheromoneMatrix[i][j]
            eta = 1/self.distanceMatrix[i][j]
            tauToAlpha = optimize(tau,alpha)
            etaToBeta = optimize(eta,beta)
            #print(etaToBeta)
            licznik = tauToAlpha*etaToBeta

            return licznik / mianownik
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

        