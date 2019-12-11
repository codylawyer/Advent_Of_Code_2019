import numpy as np

def clearLineOfSight(asteroid1,asteroid2,asteroids):
    deltaX = asteroid2[0] - asteroid1[0]
    deltaY = asteroid2[1] - asteroid1[1]
    xDir = np.sign(deltaX)
    yDir = np.sign(deltaY)

    if not(abs(int(deltaX)) == 0):
        slope = deltaY/deltaX
        startX = asteroid1[0]
        b = asteroid1[1]-slope*startX
        steps = int(abs(deltaX))
        for i in range(1,steps):
            x = i*xDir+startX
            y = slope*x + b
            if (abs(abs(y) - abs(round(y))) < np.finfo(float).eps):
                y = int(round(y))
                x = int(x)
                if (x,y) in asteroids.keys():
                    return False
    else:
        startX = asteroid1[0]
        startY = asteroid1[1]
        steps = int(abs(deltaY))
        for i in range(1,steps):
            x = startX
            y = i*yDir+startY
            y = int(y)
            x = int(x)
            if (x,y) in asteroids.keys():
                return False
    return True

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

maxViewable = 0
bestAsteroid = None
for asteroid in asteroids.keys():
    viewable = 0 
    for asteroidLookingAt in asteroids.keys():
        if not(asteroid == asteroidLookingAt):
            if clearLineOfSight(asteroid,asteroidLookingAt,asteroids):
                viewable += 1
    asteroids[asteroid] = viewable
    if viewable > maxViewable:
        maxViewable = viewable
        bestAsteroid = asteroid

print(bestAsteroid,maxViewable)
