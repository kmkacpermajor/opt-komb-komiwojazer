import random
alpha = random.randint(0,100)
beta = random.randint(0,100)
pheromoneMultiplier = random.randint(0,100)  # Q > 0
evaporationMultiplier = random.uniform(0.000001,0.999999) # 0 < ro < 1
startingValue = 0.1
shouldInitializeGreedy = False
tauZero = 0
randomConstant = 1

logLevel = 0
timeout = 300
nameOfFile = "examples/berlin52.txt"

