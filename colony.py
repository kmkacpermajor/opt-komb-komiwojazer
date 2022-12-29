import math
from point import Point
from constants import *

class Colony:
    def __init__(self, allPoints: list):
        self.pheromoneMatrix = [[startingValue for _ in allPoints] for _ in allPoints]
        self.distanceMatrix = [[self.calcDist(i, j) for i in allPoints] for j in allPoints]
        for i in range(len(self.pheromoneMatrix)):
            self.pheromoneMatrix[i][i] = 0

    def updatePheromoneEdge(self, summaryDist: int, edge: list):
        i = edge[0]
        j = edge[1]
        self.pheromoneMatrix[i][j] = self.pheromoneMatrix[i][j] + (pheromoneMultiplier/summaryDist)

    def evaporateallPheromoneEdges(self):
        for i in range(len(self.pheromoneMatrix)):
            for j in range(len(self.pheromoneMatrix)):
                self.pheromoneMatrix[i][j] = (evaporationMultiplier*self.pheromoneMatrix[i][j]) + tauZero
            self.pheromoneMatrix[i][i] = 0

    def addStartingValueToAll(self):
        for i in range(len(self.pheromoneMatrix)):
            for j in range(len(self.pheromoneMatrix[i])):
                self.pheromoneMatrix[i][j] += startingValue


    def getPheromoneMatrix(self):
        return self.pheromoneMatrix

    def getDistanceMatrix(self):
        return self.distanceMatrix

    def printPheromoneMatrix(self):
        for i in range(len(self.pheromoneMatrix)):
            print(f"{i}:", end="")
            for j in range(len(self.pheromoneMatrix[i])):
                print(f"{self.pheromoneMatrix[i][j]} ", end="")
            print("")

    def calcDist(self, a: Point, b: Point):
   
        ySub = a.y - b.y
        xSub = a.x - b.x

        return math.sqrt( xSub * xSub + ySub * ySub )

