from copy import deepcopy
import numpy as np

def applyGravityDim(moon1,moon2,dim):
    pos = 0 
    vel = 1
    if moon1[pos][dim] < moon2[pos][dim]:
        moon1[vel][dim] += 1
        moon2[vel][dim] += -1
    elif moon1[pos][dim] > moon2[pos][dim]:
        moon1[vel][dim] += -1
        moon2[vel][dim] += 1
    return moon1,moon2

def updatePositionDim(moon,dim):
    pos = 0
    vel = 1
    moon[pos][dim] += moon[vel][dim]
    return moon

moon1 = [[8, 0, 8],[0,0,0]]
moon2 = [[0, -5, -10],[0,0,0]]
moon3 = [[16, 10, -5],[0,0,0]]
moon4 = [[19, -10, -7],[0,0,0]]
moons = [moon1,moon2,moon3,moon4]
initialMoons = deepcopy(moons)

pos = 0
vel = 1
periods = []
for dim in range(0,3):
    t = 0
    cycles = [None,None,None,None]
    while True:
        t += 1
        for i,moon1 in enumerate(moons):
            for j,moon2 in enumerate(moons):
                if j>i:
                    [moon1,moon2] = applyGravityDim(moon1,moon2,dim)

        initalState = [False,False,False,False]
        for i,moon in enumerate(moons):
            moon = updatePositionDim(moon,dim)
            if (moon[pos][dim] == initialMoons[i][pos][dim]) and (moon[vel][dim] == 0):
                initalState[i] = True

        if not(False in initalState):
            periods.append(t)
            break

print(np.lcm.reduce(np.asarray(periods,dtype='int64')))