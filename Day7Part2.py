from IntCode import runProgram
from itertools import permutations
from copy import deepcopy

# Read IntCode
f = open('Day7Input.txt')
for line in f:
    program = line.split(',')
    program = [int(n) for n in program]
f.close()

ampAProgram = program[:]
ampBProgram = program[:]
ampCProgram = program[:]
ampDProgram = program[:]
ampEProgram = program[:]

programChainOrig = [ampAProgram,ampBProgram,ampCProgram,ampDProgram,ampEProgram]

# Run IntCode
perm = permutations([5,6,7,8,9])
maxOutput = 0
for phases in perm:
    programChain = deepcopy(programChainOrig)
    output = 0
    halt = [False,False,False,False,False]
    waiting = [False,False,False,False,False]
    ips = [0,0,0,0,0]
    currentProgram = 0
    phaseProvided = False
    while (False in halt):
        inputPhase = phases[currentProgram]
        if not(phaseProvided):
            inputParameters = [inputPhase,output]
        else:
            inputParameters = [output]
        [programChain[currentProgram],ips[currentProgram],programOutput,halt[currentProgram],waiting[currentProgram]] = runProgram(programChain[currentProgram],ips[currentProgram],inputParameters,'Parameter')
        output = int(programOutput[-1])
        currentProgram += 1
        if currentProgram == len(programChain):
            currentProgram = 0
            phaseProvided = True
    if output > maxOutput:
        maxOutput = output
print('Max Output: ' + str(maxOutput))