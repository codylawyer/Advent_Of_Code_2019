def validPassword(password):
    adjacentDigits = False
    alwaysIncreasing = True
    groupOfTwoAdjacentDigits = False
    currentRun = 1
    passwordString = str(password)
    for i in range(0,len(passwordString)-1):
        if passwordString[i] == passwordString[i+1]:
            adjacentDigits = True
            currentRun += 1
        else:
            if currentRun == 2:
                groupOfTwoAdjacentDigits = True
            currentRun = 1
        if passwordString[i] > passwordString[i+1]:
            alwaysIncreasing = False
        if i == 4:
            if currentRun == 2:
                groupOfTwoAdjacentDigits = True

    return (adjacentDigits and alwaysIncreasing and groupOfTwoAdjacentDigits)

minPassword = 108457
maxPassword = 562041

validPasswords = 0
for password in range(minPassword,maxPassword+1):
    if validPassword(password):
        validPasswords += 1

print(validPasswords)
