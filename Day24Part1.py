def parseState(state):
    xSize = 5
    x = 0
    y = 0
    grid = {}
    for val in state:
        grid[(x,y)] = val
        x += 1
        if x == xSize:
            x = 0
            y += 1
    return grid

def countAdjacentBugs(grid):
    adjacentBugs = {}
    for loc in grid.keys():
        bugCount = 0 
        if grid.get((loc[0],loc[1]-1),'.') == '#':
            bugCount += 1
        if grid.get((loc[0]+1,loc[1]),'.') == '#':
            bugCount += 1
        if grid.get((loc[0],loc[1]+1),'.') == '#':
            bugCount += 1
        if grid.get((loc[0]-1,loc[1]),'.') == '#':
            bugCount += 1
        adjacentBugs[loc] = bugCount
    return adjacentBugs

def updateGrid(grid,adjacentBugs):
    newGrid = {}
    for loc,val in grid.items():
        numAdjacentBugs = adjacentBugs[loc]
        if val == '.':
            if numAdjacentBugs == 1 or numAdjacentBugs == 2:
                newGrid[loc] = '#'
            else:
                newGrid[loc] = '.'
        elif val == '#':
            if numAdjacentBugs == 1:
                newGrid[loc] = '#'
            else:
                newGrid[loc] = '.'
    return newGrid

def encodeState(grid,printFlag):
    outputString = ''
    state = ''
    i = 0
    for val in grid.values():
        outputString += val
        state += val
        i += 1
        if i == 5:
            outputString += '\n'
            i = 0
    if printFlag:
        print(outputString)
    return state

def scoreState(state):
    score = 0
    for i,val in enumerate(state):
        if val == '#':
            score += 2**i
    return score

f = open('Day24Input.txt')
state = ''
for line in f:
    state += line.strip('\n')

states = {}
while True:
    states[state] = True
    grid = parseState(state)
    adjacentBugs = countAdjacentBugs(grid)
    grid = updateGrid(grid,adjacentBugs)
    state = encodeState(grid,False)
    if state in states.keys():
        break

score = scoreState(state)
print(score)