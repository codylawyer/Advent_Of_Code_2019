def updateGrid(grid,circuitNum,currentPosition,direction,axis):
    currentPosition = [currentPosition[0], currentPosition[1]]
    currentPosition[axis] += direction
    currentPosition = (currentPosition[0], currentPosition[1])
    if currentPosition in grid:
        if not(grid[currentPosition] == circuitNum):
            grid[currentPosition] = -1
    else:
        grid[currentPosition] = circuitNum
    return [grid,currentPosition]

f = open('Day3Input.txt')
circuits = []
for line in f:
    circuits.append(line.strip('\n').split(','))
f.close()

grid = {}

circuitNum = 1
for circuit in circuits:
    currentPosition = (0,0)
    grid[currentPosition] = 1
    for move in circuit:
        direction = move[0]
        distanceToMove = int(move[1:])
        if direction == 'R':
            for i in range(1,distanceToMove+1):
                [grid,currentPosition] = updateGrid(grid,circuitNum,currentPosition,1,0)
        elif direction == 'L':
            for i in range(1,distanceToMove+1):
                [grid,currentPosition] = updateGrid(grid,circuitNum,currentPosition,-1,0)
        elif direction == 'U':
            for i in range(1,distanceToMove+1):
                [grid,currentPosition] = updateGrid(grid,circuitNum,currentPosition,1,1)
        elif direction == 'D':
            for i in range(1,distanceToMove+1):
                [grid,currentPosition] = updateGrid(grid,circuitNum,currentPosition,-1,1)
    circuitNum += 1

minimumDistance = 99999999999999999999999
for point in grid.keys():
    if grid[point] == -1:
        if (abs(point[0]) + abs(point[1])) < minimumDistance:
            minimumDistance = (abs(point[0]) + abs(point[1]))

print(minimumDistance)
