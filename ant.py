from constants import *
import math
from copy import copy, deepcopy

class Ant:
    def __init__(self, startingPointInd: int, allPoints: list, pheromoneMatrix: list, distanceMatrix: list):
        self.startingPointInd = startingPointInd
        self.allPoints = allPoints
        self.pheromoneMatrix = deepcopy(pheromoneMatrix)
        self.remainingPoints = [i for i in range(0,len(allPoints))]
        self.remainingPoints.remove(self.startingPointInd)
        self.distanceMatrix = distanceMatrix
        self.path = []
        self.summaryDist = 0
        if logLevel > 0:
            print(f"Ant with starting point {self.startingPointInd}")

    def findNext(self, currInd: int, greedy: bool = False):
        bestInd = 0
        optimalDist = 0
        pointsToBeSearched = self.remainingPoints.copy()
        if logLevel > 0:
            print(f"Points to be searched: {pointsToBeSearched}")

        if not greedy:
            maxProbability = 0
            for nextInd in pointsToBeSearched:
                nextProbability = self.calcDecision(currInd,nextInd, pointsToBeSearched)
                if logLevel > 0:
                    print(f"Probability for nextInd {nextInd} is {nextProbability}")
                if nextProbability > maxProbability:
                    maxProbability = nextProbability
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
            if logLevel > 0:
                print(f"<<<<< rem poi: {self.remainingPoints} from going from point {currInd} with starting {self.startingPointInd}")
            self.remainingPoints.remove(nextInd)
            currInd = nextInd
            if logLevel > 0:
                print("Remaining points are: {}".format(self.remainingPoints))

        self.path.append([currInd, self.startingPointInd])
        self.summaryDist += self.distanceMatrix[self.startingPointInd][currInd]

    def calcDecision(self, i: int, j: int, toBeSearched: list):
        if i!=j:
            if len(self.remainingPoints) != 1:
                mianownik = 0

                if logLevel > 0:
                    print(f"toBeSearched for {i},{j}: {toBeSearched}")
                for k in toBeSearched:
                    tau = self.pheromoneMatrix[i][k]
                    eta = 1/self.distanceMatrix[i][k]
                    tauToAlpha = math.pow(tau,alpha)
                    etaToBeta = math.pow(eta,beta)
                    mianownik += tauToAlpha*etaToBeta

                tau = self.pheromoneMatrix[i][j]
                eta = 1/self.distanceMatrix[i][j]
                tauToAlpha = math.pow(tau,alpha)
                etaToBeta = math.pow(eta,beta)
                licznik = tauToAlpha*etaToBeta

                if mianownik == 0:
                    return 0

                return licznik / mianownik
            else:
                return 1
        else:
            return 0

    def printPheromoneMatrix(self):
        for j in range(len(self.pheromoneMatrix)):
            print(f"{j}:", end="")
            for i in range(len(self.pheromoneMatrix[j])):
                print(f"{self.pheromoneMatrix[j][i]} ", end="")
            print("")

    def getPath(self):
        return self.path

    def getSummaryDist(self):
        return self.summaryDist        

        