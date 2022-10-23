
from point import Point
from generator import *
from calculator import *

arrPoints = generatePointsArray() # do generacji tablicy p
arrPoints = readPointsArray() # do odczytu
# generateFile() # do generacji samego pliku

resTSP = findTSPResolution(arrPoints)
print('TSP resolution is {}'.format(resTSP))