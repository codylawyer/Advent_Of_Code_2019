from IntCode import runProgram

# Read IntCode
f = open('Day2Input.txt')
for line in f:
    program = line.split(',')
    program = [int(n) for n in program]
f.close()

# Run IntCode
noun = 20
verb = 3
program[1] = noun
program[2] = verb
program = runProgram(program)

print(100*noun+verb)