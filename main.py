from generator import *
from calculator import *
from colony import Colony
from ant import Ant
from constants import *
import time

startingTime = time.time()

arrPoints = readPointsFile(nameOfFile)
#arrPoints = generatePointsArray(5,[-50,50],[-50,50])
#generateFile(arrPoints, nameOfFile)


iteration = 0
antColony = Colony(arrPoints)
distanceMatrix = antColony.getDistanceMatrix()
#print(distanceMatrix)
sameBest = 0


if logLevel > 0:
    print("Initial pheromone matrix:")
    antColony.printPheromoneMatrix()

bestDist = 0
bestPath = []

while time.time() < startingTime + timeout and sameBest < 20:
    print(f"Starting iteration number: {iteration}")
    
    if logLevel > 0:
        print(f"Iteration before {iteration} matrix")
        antColony.printPheromoneMatrix()
    
    currPheromoneMatrix = [row[:] for row in antColony.getPheromoneMatrix().copy()]
    bestInThis = 0
    
    for startingPointInd in range(len(arrPoints)):
    
        ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
        if random.random() > randomConstant:
            ant.findPath(lookPheromone = True)
        else:
            ant.findPath()
        summaryDist = ant.getSummaryDist()
        if logLevel > 0:
            print(ant.getPath())
            print(summaryDist)

        if bestDist == 0 or summaryDist < bestDist:
            bestDist = summaryDist
            bestPath = ant.getPath()
            sameBest = 0

        if bestInThis == 0 or summaryDist < bestInThis:
            bestInThis = summaryDist

    if bestInThis == bestDist:
        sameBest += 1
        
    print(f"Best in this : {bestInThis}")

    antColony.evaporateallPheromoneEdges()
    for edge in bestPath:
            antColony.updatePheromoneEdge(bestDist, edge)

    if logLevel > 0:
        print(f"Iteration after {iteration} matrix")
        antColony.printPheromoneMatrix()
    iteration += 1

    print(f"Best dist in this iteration: {bestDist} by ant from {bestPath[0][0]}")

currPheromoneMatrix = antColony.getPheromoneMatrix()
bestMeta = 0
bestPointMeta = 0
for startingPointInd in [0]:
    ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
    ant.findPath()
    currDist = ant.getSummaryDist()
    if bestMeta == 0:
        bestMeta = currDist
        bestPointMeta = startingPointInd
    else:
        if currDist < bestMeta:
            bestMeta = currDist
            bestPointMeta = startingPointInd

bestGreedy = 0
bestPointGreedy = 0
for startingPointInd in [0]:
    ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix, distanceMatrix)
    ant.findPath(greedy = True)
    currDist = ant.getSummaryDist()
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