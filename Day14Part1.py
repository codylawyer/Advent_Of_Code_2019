import math
def findRequirements(outputChemical,amountNeeded,oreRequired,reactions,excessChemicals):
    for reaction in reactions:
        reactionInputs = reaction[0]
        reactionOutput = reaction[1]
        if reactionOutput[1] == outputChemical:
            if reactionInputs[0][1] == 'ORE':
                numReactions = math.ceil(amountNeeded/reactionOutput[0])
                chemicalGenerated = numReactions*reactionOutput[0]

                if chemicalGenerated-amountNeeded > 0:
                    excessChemical = [chemicalGenerated-amountNeeded,reactionOutput[1]]
                    excessFound = False
                    for existingExcessChemicals in excessChemicals:
                        if excessChemical[1] == existingExcessChemicals[1]:
                            excessFound = True
                            existingExcessChemicals[0] += excessChemical[0]
                    if not(excessFound):
                        excessChemicals.append(excessChemical)
                
                oreRequired = reactionInputs[0][0]*numReactions
                return oreRequired,excessChemicals
            else:
                numReactions = math.ceil(amountNeeded/reactionOutput[0])
                for reactionInput in reactionInputs:
                    amountRequired = reactionInput[0]*numReactions
                    remainingExcessChemicals = []
                    for excessChemical in excessChemicals:
                        if reactionInput[1] == excessChemical[1]:
                            newAmountRequired = amountRequired-excessChemical[0]
                            excessChemical[0] += -amountRequired
                            amountRequired = newAmountRequired
                        if excessChemical[0] > 0:
                            remainingExcessChemicals.append(excessChemical)

                    if amountRequired > 0:
                        newOreRequired,excessChemicals = findRequirements(reactionInput[1],amountRequired,0,reactions,remainingExcessChemicals)
                        oreRequired += newOreRequired

                chemicalGenerated = numReactions*reactionOutput[0]
                if chemicalGenerated-amountNeeded > 0:
                    excessChemical = [chemicalGenerated-amountNeeded,reactionOutput[1]]
                    excessFound = False
                    for existingExcessChemicals in excessChemicals:
                        if excessChemical[1] == existingExcessChemicals[1]:
                            excessFound = True
                            existingExcessChemicals[0] += excessChemical[0]
                    if not(excessFound):
                        excessChemicals.append(excessChemical)
                
    
    return oreRequired,excessChemicals

f = open('Day14Input.txt')
reactions = []
for line in f:
    reaction = line.strip('\n').split('=>')
    reactionInputs = reaction[0].split(',')
    allInputs = []
    for reactionInput in reactionInputs:
        newInput = reactionInput.split(' ')
        parsedInput = []
        for val in newInput:
            if not(val == ''):
                parsedInput.append(val)
        allInputs.append([int(parsedInput[0]),parsedInput[1]])
    reactionInputs = allInputs
    reactionOutput = reaction[1].split(' ')
    reactionOutput = [int(reactionOutput[1]),reactionOutput[2]]
    reactions.append([reactionInputs,reactionOutput])
f.close()

oreRequired,excessChemicals = findRequirements('FUEL',1,0,reactions,[])
print(oreRequired)