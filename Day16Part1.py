def genPattern(size):
    basePattern = [0, 1, 0, -1]
    fullPattern = []
    for num in basePattern:
        for i in range(0,size):
            fullPattern.append(num)
    return fullPattern

def fft(inputSequence,phases):
    for phase in range(0,phases):
        outputSequence = []
        for i in range(0,len(inputSequence)):
            pattern = genPattern(i+1)
            offset = pattern.pop(0)
            pattern.append(offset)

            outputValue = 0
            for j in range(0,len(inputSequence)):
                outputValue += inputSequence[j]*pattern[j%len(pattern)]
            outputValue = abs(outputValue)%10
            outputSequence.append(outputValue)
        inputSequence = outputSequence
    return outputSequence


f = open('Day16Input.txt')
for line in f:
    line = line.strip('\n')
    inputSequence = [int(n) for n in line]
f.close()
outputSequence = fft(inputSequence,100)
outString = ''
for i in range(0,8):
    outString += str(outputSequence[i])
print(outString)