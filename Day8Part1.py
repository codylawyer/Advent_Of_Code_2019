f = open('Day8Input.txt')
for line in f:
    imageData = line.strip('/n')
    imageData = [int(n) for n in imageData]
f.close()

imageWidth = 25
imageHeight = 6
imageLayers = int(len(imageData)/(imageHeight*imageWidth))

imageDataLayers = []
pixelCount = 0
minZeros = 9999999999999
checksum = 0
for i in range(0,imageLayers):
    currentLayer = []
    zerosCount = 0
    onesCount = 0
    twosCount = 0
    for j in range(0,imageHeight):
        currentRow = []
        for k in range(0,imageWidth):
            pixel = imageData[pixelCount]
            if pixel == 0:
                zerosCount += 1
            elif pixel == 1:
                onesCount += 1
            elif pixel == 2:
                twosCount += 1

            currentRow.append(pixel)
            pixelCount += 1
        currentLayer.append(currentRow)
    if zerosCount < minZeros:
        minZeros = zerosCount
        checksum = onesCount * twosCount

    imageDataLayers.append(currentLayer)

print(checksum)