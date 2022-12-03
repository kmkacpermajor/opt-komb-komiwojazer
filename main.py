from generator import *
from greedy import *
from calculator import *
from colony import Colony
from ant import Ant
import time

timeout = 2
startingTime = time.time()

arrPoints = generatePointsArray(26,[-100,100],[-1000,1000])

antColony = Colony(arrPoints)
while time.time() < startingTime + timeout:
    currPheromoneMatrix = antColony.getPheromoneMatrix()
    for startingPointInd in range(len(arrPoints)):
        ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix)
        ant.findPath()
        summaryDist = ant.getSummaryDist()
        print(ant.getPath())
        for edge in ant.getPath():
            antColony.updatePheromoneEdge(summaryDist, edge)
        antColony.evaporateallPheromoneEdges()

ant = Ant(0, arrPoints, antColony.getPheromoneMatrix())
ant.findPath()
print(ant.getPath())

# arrPoints = readPointsFile("examples/ekursy.txt")
# generateFile(arrPoints, "przyklad2.txt")

# warunki stopu
# czas: max 5 minut
# pliki: berlin52, bier127, tsp250, tsp500, tsp1000

#resTSP = findTSPResolution(arrPoints)
#print('TSP resolution is {}'.format(resTSP))