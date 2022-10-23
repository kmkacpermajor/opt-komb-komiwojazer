from point import Point

def readPointsFile(fileName: str):
    pointsArr = []
    with open(fileName) as pointsFile:
        pointsFile.readline() # wywalam sobie linie z ilością

        for pointString in pointsFile:
            pointsArr.append(Point([int(pointCoord) for pointCoord in pointString.split(' ')]))
    
    return pointsArr
    
def generateFile(pointsArr: list, fileName: str):
    with open(fileName, "w") as pointsFile:
        pointsFile.write("{}".format(len(pointsArr)))
        for point in pointsArr:
            pointsFile.write("\n{} {}".format(point.x, point.y))

def generatePointsArray(n: int, przedzialX=[-1000,1000], przedzialY=[-1000,1000]):
    # generacja tablicy punktów
    return None