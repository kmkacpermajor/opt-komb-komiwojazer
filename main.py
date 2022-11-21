from generator import *
from calculator import *
from greedy import *

arrPoints = generatePointsArray(26,[-100,100],[-1000,1000])
# arrPoints = readPointsFile("examples/ekursy.txt")
# generateFile(arrPoints, "przyklad2.txt")

# warunki stopu
# czas: max 5 minut
# pliki: berlin52, bier127, tsp250, tsp500, tsp1000

for x in arrPoints:
    print(x.x, x.y)

resTSP = findTSPResolution(arrPoints)
print('TSP resolution is {}'.format(resTSP))