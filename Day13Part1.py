from IntCode import runProgram

f = open('Day13Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

[program,ip,relativeBase,outputs,halt,waiting] = runProgram(program,0,0,[],'Parameter',False)
screen = {}
outputCount = 0
curX = 0
curY = 0
curVal = 0
for outputData in outputs:
    if outputCount == 0:
        curX = outputData
    elif outputCount == 1:
        curY = outputData
    elif outputCount == 2:
        curVal = outputData
    outputCount += 1
    if outputCount > 2:
        screen[(curX,curY)] = curVal
        outputCount = 0

blockCount = 0
for value in screen.values():
    if value == 2:
        blockCount += 1
print(blockCount)