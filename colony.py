from point import Point
from constants import *
from calculator import *
import random

class Colony:
    def __init__(self, allPoints: list):
        self.pheromoneMatrix = [[startingValue for _ in allPoints] for _ in allPoints]
        self.distanceMatrix = [[calcDist(i, j) for i in allPoints] for j in allPoints]
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


