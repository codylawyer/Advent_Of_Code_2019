def countOrbits(orbits,obj,count):
    if orbits[obj] == 'COM':
        return count+1
    else:
        count += 1
        count = countOrbits(orbits,orbits[obj],count)
    return count
    
orbits = {}
f = open('Day6Input.txt')
for line in f:
    orbit = line.strip('\n').split(')')
    orbits[orbit[1]] = orbit[0]
f.close()

numOrbits = 0
for key in orbits.keys():
    numOrbits += countOrbits(orbits,key,0)
print(numOrbits)