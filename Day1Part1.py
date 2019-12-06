import math
f = open('Day1Input.txt')

totalFuel = 0
for line in f:
    mass = int(line)
    totalFuel += math.floor(mass/3.0) - 2
print(totalFuel)

f.close()