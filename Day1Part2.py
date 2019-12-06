import math

def fuelNeeded(mass,fuelAmount):
    fuel = math.floor(mass/3.0) - 2
    if fuel < 0:
        fuel = 0
    fuelAmount += fuel

    if fuel > 0:
        fuelAmount = fuelNeeded(fuel,fuelAmount)
    
    return fuelAmount

f = open('Day1Input.txt')

totalFuel = 0
for line in f:
    mass = int(line)
    fuelForThisModule = fuelNeeded(mass,0)
    totalFuel += fuelForThisModule
print(totalFuel)

f.close()