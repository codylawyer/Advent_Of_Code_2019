def runProgram(program,ip=0,inputs=[],inputMode='User',debug=False):
    halt = False
    waiting = False
    relativeBase = 0

    programHm = {}
    for i,val in enumerate(program):
        programHm[i] = val

    program = programHm
    outputs = []
    while not(halt) and not(waiting):
        [program,ip,relativeBase,inputs,outputs,halt,waiting] = doInstruction(program,ip,relativeBase,inputs,outputs,inputMode,debug)
        if debug:
            print(program)
    return [program,ip,relativeBase,outputs,halt,waiting]

def doInstruction(program,ip,relativeBase,inputs,outputs,inputMode,debug=False):
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
        return [program,ip,relativeBase,inputs,outputs,True,False]

    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        param1 = program[ip+1]
        param2 = program[ip+2]
        param3 = program[ip+3]

    elif opcode == 5 or opcode == 6:
        param1 = program[ip+1]
        param2 = program[ip+2]

    elif opcode == 3 or opcode == 4 or opcode == 9:
        param1 = program[ip+1]

    waiting = False
    # add
    if opcode == 1:
        program[writePosition(program,param3,param3Mode,relativeBase)] = int(getParam(program,param1,param1Mode,relativeBase) + getParam(program,param2,param2Mode,relativeBase))
        ip += 4
    # multiply
    elif opcode == 2:
        program[writePosition(program,param3,param3Mode,relativeBase)] = int(getParam(program,param1,param1Mode,relativeBase) * getParam(program,param2,param2Mode,relativeBase))
        ip += 4
    # store input
    elif opcode == 3:
        if inputMode == 'User': #we didn't pass any inputs so get from console
            inputValue = input('Input: ')
            if param1Mode == 0: 
                program[writePosition(program,param1,param1Mode,relativeBase)] = int(inputValue)
            elif param1Mode == 2:
                program[writePosition(program,param1,param1Mode,relativeBase)] = int(inputValue)
            ip += 2
        else: # input value is first value in inputs list
            if len(inputs) > 0:
                inputValue = inputs.pop(0)
                if param1Mode == 0: 
                    program[writePosition(program,param1,param1Mode,relativeBase)] = int(inputValue)
                elif param1Mode == 2:
                    program[writePosition(program,param1,param1Mode,relativeBase)] = int(inputValue)
                ip += 2
            else:
                waiting = True
    #output value
    elif opcode == 4:
        outputValue = getParam(program,param1,param1Mode,relativeBase)
        outputs.append(outputValue)
        print('Output:',outputValue)
        ip += 2
    #jump-if-true
    elif opcode == 5:
        if not(getParam(program,param1,param1Mode,relativeBase) == 0):
            ip = getParam(program,param2,param2Mode,relativeBase)
        else:
            ip += 3
    #jump-if-false
    elif opcode == 6:
        if getParam(program,param1,param1Mode,relativeBase) == 0:
            ip = getParam(program,param2,param2Mode,relativeBase)
        else:
            ip += 3
    #less than
    elif opcode == 7:
        if getParam(program,param1,param1Mode,relativeBase) < getParam(program,param2,param2Mode,relativeBase):
            program[writePosition(program,param3,param3Mode,relativeBase)] = 1
        else:
            program[writePosition(program,param3,param3Mode,relativeBase)] = 0
        ip += 4
    #equals
    elif opcode == 8:
        if getParam(program,param1,param1Mode,relativeBase) == getParam(program,param2,param2Mode,relativeBase):
            program[writePosition(program,param3,param3Mode,relativeBase)] = 1
        else:
            program[writePosition(program,param3,param3Mode,relativeBase)] = 0
        ip += 4
    # set relativeBase
    elif opcode == 9:
        relativeBase += getParam(program,param1,param1Mode,relativeBase)
        ip += 2
    # broken
    else:
        print('Invalid Opcode: ' + str(opcode))
        return [program,ip,relativeBase,inputs,outputs,True,False]

    return [program,ip,relativeBase,inputs,outputs,False,waiting]

def getParam(program,param,paramMode,relativeBase):
    if paramMode == 0: # position
        if param in program.keys():
            paramValue = program[param]
        else:
            program[param] = 0
            paramValue = program[param]
    elif paramMode == 1: # immediate
        paramValue = param
    elif paramMode == 2: # relative
        if (param+relativeBase) in program.keys():
            paramValue = program[param+relativeBase]
        else:
            program[param+relativeBase] = 0
            paramValue = program[param+relativeBase]
    return paramValue

def writePosition(program,param,paramMode,relativeBase):
    if paramMode == 0: # position
        paramValue = param
    elif paramMode == 1: # immediate
        paramValue = param
    elif paramMode == 2: # relative
        paramValue = param+relativeBase
    return paramValue