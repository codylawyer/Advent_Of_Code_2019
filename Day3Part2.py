def updateGrid(grid,circuitNum,moveNum,currentPosition,direction,axis):
    currentPosition = [currentPosition[0], currentPosition[1]]
    currentPosition[axis] += direction
    currentPosition = (currentPosition[0], currentPosition[1])
    if currentPosition in grid:
        if not(grid[currentPosition][0] == circuitNum):
            data = grid[currentPosition]
            data[0] = -1
            data[circuitNum] = moveNum
            grid[currentPosition] = data
    else:
        data = [circuitNum, 0, 0]
        data[circuitNum] = moveNum
        grid[currentPosition] = data
    return [grid,currentPosition]

f = open('Day3Input.txt')
circuits = []
for line in f:
    circuits.append(line.strip('\n').split(','))
f.close()

grid = {}
for circuitNum, circuit in enumerate(circuits,start=1):
    currentPosition = (0,0)
    grid[currentPosition] = [1,0,0]
    moveNum = 0
    for move in circuit:
        direction = move[0]
        distanceToMove = int(move[1:])
        if direction == 'R':
            for i in range(1,distanceToMove+1):
                moveNum += 1
                [grid,currentPosition] = updateGrid(grid,circuitNum,moveNum,currentPosition,1,0)
        elif direction == 'L':
            for i in range(1,distanceToMove+1):
                moveNum += 1
                [grid,currentPosition] = updateGrid(grid,circuitNum,moveNum,currentPosition,-1,0)
        elif direction == 'U':
            for i in range(1,distanceToMove+1):
                moveNum += 1
                [grid,currentPosition] = updateGrid(grid,circuitNum,moveNum,currentPosition,1,1)
        elif direction == 'D':
            for i in range(1,distanceToMove+1):
                moveNum += 1
                [grid,currentPosition] = updateGrid(grid,circuitNum,moveNum,currentPosition,-1,1)

minimumMoves = 99999999999999999999999
for point in grid.keys():
    if grid[point][0] == -1:
        if (grid[point][1] + grid[point][2]) < minimumMoves:
            minimumMoves = (grid[point][1] + grid[point][2])

print(minimumMoves)
