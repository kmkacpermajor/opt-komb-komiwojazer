import random
alpha = random.randint(0,100)
beta = random.randint(0,100)
pheromoneMultiplier = random.randint(0,100)  # Q > 0
evaporationMultiplier = random.uniform(0.000001,0.999999) # 0 < ro < 1
startingValue = random.uniform(0.000001,0.099999) # 0 < ro < 1
tauZero = random.uniform(0.000001,0.000999) # 0 < ro < 1

logLevel = 0
timeout = 600
nameOfFile = "examples/bier127.txt"

