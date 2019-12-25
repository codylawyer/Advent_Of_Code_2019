def cut(deck,increment):
    topDeck = deck[0:increment]
    bottomDeck = deck[increment:]
    deck = bottomDeck + topDeck
    return deck

def deal(deck,increment):
    if increment == 0:
        deck.reverse()
    else:
        newDeck = [None for i in range(0,len(deck))]
        currentPosition = 0
        while len(deck) > 0:
            newDeck[currentPosition] = deck.pop(0)
            currentPosition += increment
            if currentPosition > len(newDeck):
                currentPosition = currentPosition%len(newDeck)
        deck = newDeck
    return deck

f = open('Day22Input.txt')
instructions = []
for line in f:
    instruction = line.strip('\n').split(' ')
    if instruction[0] == 'deal':
        if instruction[2] == 'new':
            instructions.append(['deal',int(0)])
        if instruction[2] == 'increment':
            instructions.append(['deal',int(instruction[3])])
    elif instruction[0] == 'cut':
        instructions.append(['cut',int(instruction[1])])
f.close()

deck = [x for x in range(0,119315717514047)]
for instruction in instructions:
    if instruction[0] == 'deal':
        deck = deal(deck,instruction[1])
    elif instruction[0] == 'cut':
        deck = cut(deck,instruction[1])
print(deck[2019])