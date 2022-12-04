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
        self.pheromoneMatrix[j][i] += pheromoneMultiplier/summaryDist

    def evaporateallPheromoneEdges(self):
        for j in range(len(self.pheromoneMatrix)):
            for i in range(len(self.pheromoneMatrix)):
                self.pheromoneMatrix[j][i] *= (1-evaporationMultiplier)

    def getPheromoneMatrix(self):
        return self.pheromoneMatrix

    def getDistanceMatrix(self):
        return self.distanceMatrix

    def printPheromoneMatrix(self):
        for j in range(len(self.pheromoneMatrix)):
            print(f"{j}:", end="")
            for i in range(len(self.pheromoneMatrix[j])):
                print(f"{self.pheromoneMatrix[j][i]} ", end="")
            print("")


