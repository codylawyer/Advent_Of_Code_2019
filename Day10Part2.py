import numpy as np
import math
import operator
                
f = open('Day10Input.txt')
asteroids = {}
y = 0
for line in f:
    row = line.strip('\n')
    for x,val in enumerate(row):
        if val == '#':
            asteroids[(x,y)] = 1
    y += 1
f.close()

totalAsteroidsToDestroy = len(asteroids)-1
numAsteroidsDestroyed = 0
monitoringStation = (26,29)

asteroidsToDestroy = []
for asteroid in asteroids:
    if not(asteroid == monitoringStation):
        deltaX = asteroid[0] - monitoringStation[0]
        deltaY = -(asteroid[1] - monitoringStation[1])
        asteroidRange = math.sqrt(deltaX**2 + deltaY**2)
        asteroidAngle = (math.atan2(deltaY,deltaX)-math.pi/2)%(2*math.pi)
        if asteroidAngle < 1e-13:
            asteroidAngle = math.pi*2
        asteroidsToDestroy.append([asteroid,asteroidRange,asteroidAngle])
    else:
        asteroids[asteroid] = [0,0]
        asteroidRange = 0

currentAngle = math.pi*2
asteroidsToDestroy.sort(key = operator.itemgetter(2, 1),reverse=True)

numToDestroy = 200
for j in range(0,numToDestroy):
    idx = 0
    minRange = 999.9
    minAngleNext = 9999.0
    nextAngle = None
    for i,asteroidToDestroy in enumerate(asteroidsToDestroy):
        if (abs(asteroidToDestroy[2] - currentAngle)) < 1e-10:
            if (asteroidToDestroy[1]) < minRange:
                idx = i
        else:
            if abs(asteroidToDestroy[2] - currentAngle) < minAngleNext and ((asteroidToDestroy[2] - currentAngle) < 0.0):
                minAngleNext = abs(asteroidToDestroy[2] - currentAngle)
                nextAngle = asteroidToDestroy[2]

    if (j+1) == 200:
        print(asteroidsToDestroy[idx][0][0]*100+asteroidsToDestroy[idx][0][1])
    asteroidsToDestroy.pop(idx)
    
    if nextAngle == None:
        nextAngle = math.pi*2
    currentAngle = nextAngle