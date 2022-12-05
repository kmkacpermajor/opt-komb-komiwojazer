from generator import *
from calculator import *
from colony import Colony
from ant import Ant
from constants import *
import time

startingTime = time.time()

arrPoints = readPointsFile("examples/berlin52.txt")
#arrPoints = generatePointsArray(3,[-10,10],[-10,10])
#generateFile(arrPoints, "przyklad2.txt")


iteration = 0
initialize = shouldInitializeGreedy
antColony = Colony(arrPoints)
distanceMatrix = antColony.getDistanceMatrix()
#print(distanceMatrix)

if logLevel > 0:
    print("Initial pheromone matrix:")
    antColony.printPheromoneMatrix()

while time.time() < startingTime + timeout:
    print(f"Starting iteration number: {iteration}")
    currPheromoneMatrix = [row[:] for row in antColony.getPheromoneMatrix()]

    if logLevel > 0:
        print(f"Iteration before {iteration} matrix")
        antColony.printPheromoneMatrix()

    bestDist = 0
    
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

            if bestDist == 0:
                bestDist = summaryDist
            else:
                if summaryDist < bestDist:
                    bestDist = summaryDist

    if logLevel > 0:
        print(f"Iteration after {iteration} matrix")
        antColony.printPheromoneMatrix()
    iteration += 1
    initialize = False

    print(f"Best dist in this iteration: {bestDist}")

currPheromoneMatrix = antColony.getPheromoneMatrix()
bestMeta = 0
bestPointMeta = 0
for startingPointInd in range(len(arrPoints)):
    ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
    ant.findPath()
    currDist = ant.getSummaryDist()
    if logLevel > 0:
        print(ant.getPath())
        print(f"from {startingPointInd}: {currDist}")
    if bestMeta == 0:
        bestMeta = currDist
        bestPointMeta = startingPointInd
    else:
        if currDist < bestMeta:
            bestMeta = currDist
            bestPointMeta = startingPointInd

bestGreedy = 0
bestPointGreedy = 0
for startingPointInd in range(len(arrPoints)):
    ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
    ant.findPath(True)
    currDist = ant.getSummaryDist()
    if logLevel > 0:
        print(ant.getPath())
        print(f"from {startingPointInd}: {currDist}")
    if bestGreedy == 0:
        bestGreedy = currDist
        bestPointGreedy = startingPointInd
    else:
        if currDist < bestGreedy:
            bestGreedy = currDist
            bestPointGreedy = startingPointInd

print()
print(f"Best meta from {bestPointMeta}: {bestMeta}")
print(f"Best greedy from {bestPointGreedy}: {bestGreedy}")

# warunki stopu
# czas: max 5 minut
# pliki: berlin52, bier127, tsp250, tsp500, tsp1000