from IntCode import runProgram

f = open('Day13Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

ip = 0
relativeBase = 0
halt = False
inputParameters = [0]

screen = {}
score = 0
curX = 0
curY = 0
curVal = 0
ballX = 0
ballY = 0
paddleX = 0
paddleY = 0

while not(halt):
    [program,ip,relativeBase,outputs,halt,waiting] = runProgram(program,ip,relativeBase,inputParameters,'Parameter',False)

    outputCount = 0
    for outputData in outputs:
        if outputCount == 0:
            curX = outputData
        elif outputCount == 1:
            curY = outputData
        elif outputCount == 2:
            curVal = outputData
            if curVal == 4:
                ballX = curX
                ballY = curY
            if curVal == 3:
                paddleX = curX
                paddleY = curY
        outputCount += 1
        if outputCount > 2:
            if (curX == -1) and (curY == 0):
                score = curVal
            else:
                screen[(curX,curY)] = curVal
            outputCount = 0

    if ballX < paddleX:
        inputParameters = [-1]
    elif ballX == paddleX:
        inputParameters = [0]
    elif ballX > paddleX:
        inputParameters = [1]

print(score)