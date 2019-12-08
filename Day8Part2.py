from PIL import Image

f = open('Day8Input.txt')
for line in f:
    imageData = line.strip('\n')
    imageData = [int(n) for n in imageData]
f.close()

imageWidth = 25
imageHeight = 6
imageLayers = int(len(imageData)/(imageHeight*imageWidth))

imageOutput = ''
for i in range(0,imageHeight):
    for j in range(0,imageWidth):
        imageOutput += '2'

pixelCount = 0
for i in range(0,imageLayers):
    newImageOutput = ''
    for j in range(0,imageHeight):
        for k in range(0,imageWidth):
            pixel = imageData[pixelCount]
            if imageOutput[pixelCount%(imageWidth*imageHeight)] == '2':
                newImageOutput += str(pixel)
            else:
                newImageOutput += imageOutput[pixelCount%(imageWidth*imageHeight)]
            pixelCount += 1
    imageOutput = newImageOutput

actualImage = Image.new('1', (imageWidth,imageHeight), color=0)
pix = actualImage.load()

pixelCount = 0
for i in range(0,imageHeight):
    for j in range(0,imageWidth):
        pix[j, i] = int(imageOutput[pixelCount])
        pixelCount += 1
actualImage.show()