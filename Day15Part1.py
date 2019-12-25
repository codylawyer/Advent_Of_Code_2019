from IntCode import runProgram
from os import system
import random
import queue

system('cls')
def printMap(areaMap,curX,curY):
    mapSizeX = 50
    mapSizeY = 50
    outputMapString = ''
    for y in range(int(mapSizeY/2)+curY,-int(mapSizeY/2)+1+curY,-1):
        for x in range(int(mapSizeX/2)+curX,-int(mapSizeX/2)+1+curX,-1):
            value = areaMap.get((x,y), "?")
            if (x,y) == (curX,curY):
                value = 'D'
            outputMapString += value
        outputMapString += '\n'
    print(outputMapString)
    #input()

def bfs(areaMap,curX,curY,locationsVisited,locationQueue):
    toVisit = locationQueue.get()
    curX = toVisit[0]
    curY = toVisit[1]
    if (locationsVisited.get((curX,curY+1), False) == False):
        locationQueue.put((curX,curY+1))
    if (locationsVisited.get((curX,curY-1), False) == False):
        locationQueue.put((curX,curY-1))
    if (locationsVisited.get((curX-1,curY), False) == False):
        locationQueue.put((curX-1,curY))
    if (locationsVisited.get((curX+1,curY), False) == False):
        locationQueue.put((curX+1,curY))


def nextMove(areaMap,curX,curY,curDir,locationsVisited):
    canMoveDirs = []
    if (areaMap.get((curX,curY+1), '') == ''):
        canMoveDirs.append(1)
    if (areaMap.get((curX,curY-1), '') == ''):
        canMoveDirs.append(2)
    if (areaMap.get((curX-1,curY), '') == ''):
        canMoveDirs.append(3)
    if (areaMap.get((curX+1,curY), '') == ''):
        canMoveDirs.append(4)
    if len(canMoveDirs) > 0:
        return canMoveDirs[random.randint(0,len(canMoveDirs)-1)]

    if (areaMap.get((curX,curY+1), '') == '.'):
        canMoveDirs.append(1)
    if (areaMap.get((curX,curY-1), '') == '.'):
        canMoveDirs.append(2)
    if (areaMap.get((curX-1,curY), '') == '.'):
        canMoveDirs.append(3)
    if (areaMap.get((curX+1,curY), '') == '.'):
        canMoveDirs.append(4)
    if len(canMoveDirs) > 0:
        return canMoveDirs[random.randint(0,len(canMoveDirs)-1)]

f = open('Day15Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

ip = 0
relativeBase = 0
halt = False

areaMap = {}
curX = 0
curY = 0
curDir = 1
prevDir = curDir
inputParameters = [curDir]
locationsVisited = {}
repairFound = False

locationQueue = queue.Queue()
locationQueue.put((curX,curY+1))

while not(halt):
    [program,ip,relativeBase,outputs,halt,waiting] = runProgram(program,ip,relativeBase,inputParameters,'Parameter',False)
    
    if outputs[0] == 0:
        if curDir == 1:
            areaMap[(curX,curY+1)] = '#'
            locationsVisited[(curX,curY+1)] = True
            #curDir = 4
        elif curDir == 2:
            areaMap[(curX,curY-1)] = '#'
            locationsVisited[(curX,curY-1)] = True
            #curDir = 3
        elif curDir == 3:
            areaMap[(curX-1,curY)] = '#'
            locationsVisited[(curX-1,curY)] = True
            #curDir = 1
        elif curDir == 4:
            areaMap[(curX+1,curY)] = '#'
            locationsVisited[(curX+1,curY)] = True
            #curDir = 2
    elif outputs[0] == 1:
        if curDir == 1:
            curY += 1
        elif curDir == 2:
            curY -= 1
        elif curDir == 3:
            curX -= 1
        elif curDir == 4:
            curX += 1
        areaMap[(curX,curY)] = '.'
        locationsVisited[(curX,curY)] = True
    elif outputs[0] == 2:
        if curDir == 1:
            curY += 1
        elif curDir == 2:
            curY -= 1
        elif curDir == 3:
            curX -= 1
        elif curDir == 4:
            curX += 1
        areaMap[(curX,curY)] = '*'
        repairFound = True
        print((curX,curY))
        break

    #printMap(areaMap,curX,curY)
    curDir = nextMove(areaMap,curX,curY,curDir,locationsVisited)
    inputParameters = [curDir]

printMap(areaMap,curX,curY)