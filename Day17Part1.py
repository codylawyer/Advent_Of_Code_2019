from IntCode import runProgram

def getSumOfAlignmentParameters(scaffolds):
    sumOfAlignmentParameters = 0
    for scaffold in scaffolds.keys():
        x = scaffold[0]
        y = scaffold[1]
        if scaffolds.get((x,y-1), False) and scaffolds.get((x+1,y), False) and scaffolds.get((x,y+1), False) and scaffolds.get((x-1,y), False):
            sumOfAlignmentParameters += x*y
    return sumOfAlignmentParameters

f = open('Day17Input.txt')
for line in f:
    program = line.strip('\n').split(',')
    program = [int(n) for n in program]
f.close()

ip = 0
relativeBase = 0
halt = False
inputParameters = []

while not(halt):
    [program,ip,relativeBase,outputs,halt,waiting] = runProgram(program,ip,relativeBase,inputParameters,'Parameter',False)

    scaffolds = {}
    x = 0
    y = 0
    for output in outputs:
        if output == 35: # scaffold
            scaffolds[(x,y)] = 1
            pass
        elif output == 46: # dot
            pass
        elif output == 10: #new line
            x = -1
            y += 1
        else: # robot
            scaffolds[(x,y)] = 1
        x += 1

    screen = ''.join(map(chr,outputs))

    print(screen)
    print(getSumOfAlignmentParameters(scaffolds))

    