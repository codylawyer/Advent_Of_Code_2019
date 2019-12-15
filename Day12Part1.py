def applyGravity(moon1,moon2):
    if moon1[0][0] < moon2[0][0]:
        moon1[1][0] += 1
    elif moon1[0][0] > moon2[0][0]:
        moon1[1][0] += -1
    if moon1[0][1] < moon2[0][1]:
        moon1[1][1] += 1
    elif moon1[0][1] > moon2[0][1]:
        moon1[1][1] += -1
    if moon1[0][2] < moon2[0][2]:
        moon1[1][2] += 1
    elif moon1[0][2] > moon2[0][2]:
        moon1[1][2] += -1
    return moon1

def updatePosition(moon):
    moon[0][0] += moon[1][0]
    moon[0][1] += moon[1][1]
    moon[0][2] += moon[1][2]
    return moon

def calculateEnergy(moons):
    totalEnergy = 0
    for moon in moons:
        potEnergy = abs(moon[0][0])+abs(moon[0][1])+abs(moon[0][2])
        kinEnergy = abs(moon[1][0])+abs(moon[1][1])+abs(moon[1][2])
        totalEnergy += potEnergy*kinEnergy
    return totalEnergy

# moon1 = [[-8, -10, 0],[0,0,0]]
# moon2 = [[5, 5, 10],[0,0,0]]
# moon3 = [[2, -7, 3],[0,0,0]]
# moon4 = [[9, -8, -3],[0,0,0]]

moon1 = [[8, 0, 8],[0,0,0]]
moon2 = [[0, -5, -10],[0,0,0]]
moon3 = [[16, 10, -5],[0,0,0]]
moon4 = [[19, -10, -7],[0,0,0]]
moons = [moon1,moon2,moon3,moon4]

timeSteps = 1000
for i in range(0,timeSteps):
    for i,moon1 in enumerate(moons):
        for j,moon2 in enumerate(moons):
            if not(i==j):
                moon1 = applyGravity(moon1,moon2)
    for moon in moons:
        moon = updatePosition(moon)

print(calculateEnergy(moons))