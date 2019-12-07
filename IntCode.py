def runProgram(program,ip,inputs=[],inputMode='User',debug=False):
    halt = False
    waiting = False
    outputs = []
    while not(halt) and not(waiting):
        [program,ip,inputs,outputs,halt,waiting] = doInstruction(program,ip,inputs,outputs,inputMode,debug)
        if debug:
            print(program)
    return [program,ip,outputs,halt,waiting]

def doInstruction(program,ip,inputs,outputs,inputMode,debug=False):
    opcode = program[ip]

    opcodeString = str(opcode)
    if len(opcodeString) == 1:
        param1Mode = 0
        param2Mode = 0
        param3Mode = 0
        opcode = int(opcodeString)
    elif len(opcodeString) == 2:
        param1Mode = 0
        param2Mode = 0
        param3Mode = 0
        opcode = int(opcodeString)
    elif len(opcodeString) == 3:
        param1Mode = int(opcodeString[0])
        param2Mode = 0
        param3Mode = 0
        opcode = int(opcodeString[1:])
    elif len(opcodeString) == 4:
        param1Mode = int(opcodeString[1])
        param2Mode = int(opcodeString[0])
        param3Mode = 0
        opcode = int(opcodeString[2:])
    elif len(opcodeString) == 5:
        param1Mode = int(opcodeString[2])
        param2Mode = int(opcodeString[1])
        param3Mode = int(opcodeString[0])
        opcode = int(opcodeString[3:])

    if opcode == 99:
        return [program,ip,inputs,outputs,True,False]

    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        param1 = program[ip+1]
        param2 = program[ip+2]
        param3 = program[ip+3]
        if param1Mode == 0:
            param1Value = program[param1]
        elif param1Mode == 1:
            param1Value = param1
        if param2Mode == 0:
            param2Value = program[param2]
        elif param2Mode == 1:
            param2Value = param2
        if param3Mode == 0:
            param3Value = param3
        elif param3Mode == 1:
            param3Value = param3
        if debug:
            print(opcodeString,param1Value,param2Value,param3Value)
    elif opcode == 5 or opcode == 6:
        param1 = program[ip+1]
        param2 = program[ip+2]
        if param1Mode == 0:
            param1Value = program[param1]
        elif param1Mode == 1:
            param1Value = param1
        if param2Mode == 0:
            param2Value = program[param2]
        elif param2Mode == 1:
            param2Value = param2
        if debug:
            print(opcodeString,param1Value,param2Value)
    elif opcode == 3 or opcode == 4:
        param1 = program[ip+1]
        if param1Mode == 0:
            param1Value = program[param1]
        elif param1Mode == 1:
            param1Value = param1
        if debug:
            print(opcodeString,param1Value)

    waiting = False
    # add
    if opcode == 1:
        program[param3Value] = int(param1Value + param2Value)
        ip += 4
    # multiply
    elif opcode == 2:
        program[param3Value] = int(param1Value * param2Value)
        ip += 4
    # store input
    elif opcode == 3:
        if inputMode == 'User': #we didn't pass any inputs so get from console
            inputValue = input('Input: ')
            program[param1] = int(inputValue)
            ip += 2
        else: # input value is first value in inputs list
            if len(inputs) > 0:
                inputValue = inputs.pop(0)
                program[param1] = int(inputValue)
                ip += 2
            else:
                waiting = True
        
    #output value
    elif opcode == 4:
        outputValue = param1Value
        outputs.append(outputValue)
        print('Output:',outputValue)
        ip += 2
    #jump-if-true
    elif opcode == 5:
        if not(param1Value == 0):
            ip = param2Value
        else:
            ip += 3
    #jump-if-false
    elif opcode == 6:
        if param1Value == 0:
            ip = param2Value
        else:
            ip += 3
    #less than
    elif opcode == 7:
        if param1Value < param2Value:
            program[param3Value] = 1
        else:
            program[param3Value] = 0
        ip += 4
    #equals
    elif opcode == 8:
        if param1Value == param2Value:
            program[param3Value] = 1
        else:
            program[param3Value] = 0
        ip += 4
    # broken
    else:
        print('Invalid Opcode: ' + str(opcode))
        return [program,ip,inputs,outputs,True,False]

    return [program,ip,inputs,outputs,False,waiting]