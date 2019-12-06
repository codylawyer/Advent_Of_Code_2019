def findTransfersFromTo(orbits,start,destination):
    path1 = findPathToCOM(orbits,'YOU',[])
    path2 = findPathToCOM(orbits,'SAN',[])

    transfers = 0
    nearestCommonPoint = None
    for transfer in path1:
        if transfer in path2:
            nearestCommonPoint = transfer
            break
        else:
            transfers += 1

    for transfer in path2:
        if transfer == nearestCommonPoint:
            break
        else:
            transfers += 1
    
    return transfers

def findPathToCOM(orbits,location,path):
    nextStep = orbits[location]
    path.append(nextStep)
    if nextStep == 'COM':
        return path
    else:
        path = findPathToCOM(orbits,nextStep,path)
    return path
    
orbits = {}
f = open('Day6Input.txt')
for line in f:
    orbit = line.strip('\n').split(')')
    orbits[orbit[1]] = orbit[0]
f.close()

print(findTransfersFromTo(orbits,'YOU','SAN'))