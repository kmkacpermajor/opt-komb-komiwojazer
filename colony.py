from point import Point
from constants import *
from calculator import *
import random

class Colony:
    def __init__(self, allPoints: list):
        self.pheromoneMatrix = [[random.randint(0,100)/100 for _ in allPoints] for _ in allPoints]
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
                self.pheromoneMatrix[j][i] *= evaporationMultiplier

    def getPheromoneMatrix(self):
        return self.pheromoneMatrix


