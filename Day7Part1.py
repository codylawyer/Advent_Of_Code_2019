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
perm = permutations([0,1,2,3,4])
maxOutput = 0
for phases in perm:
    programChain = deepcopy(programChainOrig)
    output = 0
    for i,program in enumerate(programChain):
        inputPhase = phases[i]
        [programChain[i],programOutput] = runProgram(programChain[i],[inputPhase,output])
        output = int(programOutput[0])
    if output > maxOutput:
        maxOutput = output
print('Max Output: ' + str(maxOutput))