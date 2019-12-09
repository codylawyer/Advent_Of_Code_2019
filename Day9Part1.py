from IntCode import runProgram
from itertools import permutations
from copy import deepcopy

# Read IntCode
f = open('Day9Input.txt')
for line in f:
    program = line.split(',')
    program = [int(n) for n in program]
f.close()

ip = 0
halt = False
waiting = True

[program,memory,ip,programOutput,halt,waiting] = runProgram(program,ip=0,inputs=[2],inputMode='Parameter',debug=False)