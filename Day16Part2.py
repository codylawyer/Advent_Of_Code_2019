def genPattern(size):
    basePattern = [0, 1, 0, -1]
    fullPattern = []
    for num in basePattern:
        for i in range(0,size):
            fullPattern.append(num)
    return fullPattern

def fft(inputSequence,phases):
    pattern = [0, 1, 0, -1]
    for phase in range(0,phases):
        outputSequence = inputSequence
        for i in range(0,len(inputSequence)):
            patternPosition = 0
            patternCount = i+1
            outputValue = 0
            for j in range(i,len(inputSequence)):
                if ((patternCount) % (i+1)) == 0:
                    patternPosition += 1
                    patternCount = 0
                outputValue += inputSequence[j]*pattern[patternPosition%len(pattern)]
                patternCount += 1
            outputValue = abs(outputValue)%10
            outputSequence[i] = outputValue
        inputSequence = outputSequence
    return outputSequence


f = open('Day16Input.txt')
for line in f:
    line = line.strip('\n')
    inputSequence = [int(n) for n in line]*1000
f.close()

offsetString = ''
for i in range(0,7):
    offsetString += str(inputSequence[i])
offset = int(offsetString)
print(offset)

outputSequence = fft(inputSequence,100)

outString = ''
for i in range(offset+1,offset+9):
    outString += str(outputSequence[i])
print(outString)