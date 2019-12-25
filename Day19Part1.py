from IntCode import runProgram
from copy import deepcopy

f = open('Day19Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

initProgram = deepcopy(program)
outputArea = ''
pointsAffected = 0
for x in range(0,50):
    for y in range(0,50):
        inputParameters = [x,y]
        ip = 0
        relativeBase = 0
        halt = False
        while not(halt):
            [program,ip,relativeBase,outputs,halt,waiting] = runProgram(initProgram,ip,relativeBase,inputParameters,'Parameter',False)
            if outputs[0] == 1:
                outputArea += '#'
                pointsAffected += 1
            else:
                outputArea += '.'
    outputArea += '\n'

print(pointsAffected)

    