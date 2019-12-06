from IntCode import runProgram

# Read IntCode
f = open('Day2Input.txt')
for line in f:
    program = line.split(',')
    program = [int(n) for n in program]
f.close()

# Run IntCode
program = runProgram(program)

print(program[0])