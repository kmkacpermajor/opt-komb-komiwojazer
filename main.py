from generator import *
from greedy import *
from calculator import *
from colony import Colony
from ant import Ant
from timeout import *

arrPoints = generatePointsArray(26,[-100,100],[-1000,1000])

try:
    with time_limit(300):
        antColony = Colony(arrPoints)
        while True:
            currPheromoneMatrix = antColony.getPheromoneMatrix()
            for startingPointInd in range(len(arrPoints)):
                ant = Ant(startingPointInd, arrPoints, currPheromoneMatrix)
                ant.findPath()
                summaryDist = ant.getSummaryDist()
                for edge in ant.getPath():
                    antColony.updatePheromoneEdge(summaryDist, edge)
                antColony.evaporateallPheromoneEdges()
except TimeoutException as e:
    print("Przekroczony limit czasu")

ant = Ant(0, arrPoints, antColony.getPheromoneMatrix())
ant.findPath()
print(ant.getPath)

# arrPoints = readPointsFile("examples/ekursy.txt")
# generateFile(arrPoints, "przyklad2.txt")

# warunki stopu
# czas: max 5 minut
# pliki: berlin52, bier127, tsp250, tsp500, tsp1000

for x in arrPoints:
    print(x.x, x.y)

#resTSP = findTSPResolution(arrPoints)
#print('TSP resolution is {}'.format(resTSP))