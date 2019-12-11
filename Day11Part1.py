from IntCode import runProgram

f = open('Day11Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

paintedPanels = {}
robotPosition = [0,0]
robotDirection = [0,1]

# Run Program
halt = False
waiting = False
ip = 0
relativeBase = 0

while not(halt):
    robotPositionTuple = (robotPosition[0],robotPosition[1])
    if robotPositionTuple in paintedPanels.keys():
        currentPaintColor = paintedPanels[robotPositionTuple]
    else:
        currentPaintColor = 0 #not painted yet so black

    inputParameters = [currentPaintColor]
    [program,ip,relativeBase,outputs,halt,waiting] = runProgram(program,ip,relativeBase,inputParameters,'Parameter',True)

    paintColor = outputs[0]
    turnDirection = outputs[1]

    # paint
    robotPositionTuple = (robotPosition[0],robotPosition[1])
    paintedPanels[robotPositionTuple] = paintColor

    # turn
    if turnDirection == 1: # right 90
        if robotDirection == [0,1]: # up
            robotDirection = [1,0] # right
        elif robotDirection == [1,0]: # right
            robotDirection = [0,-1] # down
        elif robotDirection == [0,-1]: # down
            robotDirection = [-1,0] # left
        elif robotDirection == [-1,0]: # left
            robotDirection = [0,1] # up
    elif turnDirection == 0: #left 90
        if robotDirection == [0,1]: # up
            robotDirection = [-1,0] # left
        elif robotDirection == [1,0]: # right
            robotDirection = [0,1] # up
        elif robotDirection == [0,-1]: # down
            robotDirection = [1,0] # right
        elif robotDirection == [-1,0]: # left
            robotDirection = [0,-1] # down

    # move
    robotPosition[0] += robotDirection[0]
    robotPosition[1] += robotDirection[1]

print(len(paintedPanels))
