from generator import *
from calculator import *
from colony import Colony
from ant import Ant
from constants import *
import time

startingTime = time.time()

arrPoints = readPointsFile("examples/ekursy.txt")
# generateFile(arrPoints, "przyklad2.txt")
#arrPoints = generatePointsArray(26,[-100,100],[-1000,1000])

iteration = 0
initialize = True
antColony = Colony(arrPoints)
distanceMatrix = antColony.getDistanceMatrix()

if logLevel > 0:
    print("Initial pheromone matrix:")
    antColony.printPheromoneMatrix()

while time.time() < startingTime + timeout:
    print(f"Starting iteration number: {iteration}")
    currPheromoneMatrix = antColony.getPheromoneMatrix()

    antColony.evaporateallPheromoneEdges()
    for startingPointInd in range(len(arrPoints)):
        ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
        ant.findPath(initialize)
        summaryDist = ant.getSummaryDist()
        if logLevel > 0:
            print(ant.getPath())
            print(summaryDist)
        for edge in ant.getPath():
            antColony.updatePheromoneEdge(summaryDist, edge)

    
    
    if logLevel > 0:
        print(f"Iteration {iteration} matrix")
        antColony.printPheromoneMatrix()
    iteration += 1
    initialize = False

ant = Ant(0, arrPoints, antColony.getPheromoneMatrix(), distanceMatrix)
ant.findPath()
if logLevel > 0:
    print(ant.getPath())
print(ant.getSummaryDist())


ant = Ant(0, arrPoints, antColony.getPheromoneMatrix(), distanceMatrix)
ant.findPath(True)
print(ant.getSummaryDist())

# warunki stopu
# czas: max 5 minut
# pliki: berlin52, bier127, tsp250, tsp500, tsp1000