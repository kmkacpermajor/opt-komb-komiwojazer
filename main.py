from generator import *
from calculator import *

# zrób do tego jakieś menu proste:
# czy odczytać
# czy zapisać
# ile punktów i jakie przedziały

arrPoints = generatePointsArray(26,[-100,100],[-1000,1000])
# arrPoints = readPointsFile("examples/ekursy.txt")
# generateFile(arrPoints, "przyklad2.txt")

for x in arrPoints:
    print(x.x, x.y)

resTSP = findTSPResolution(arrPoints)
print('TSP resolution is {}'.format(resTSP))