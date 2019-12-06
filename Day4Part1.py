def validPassword(password):
    adjacentDigits = False
    alwaysIncreasing = True
    passwordString = str(password)
    for i in range(0,len(passwordString)-1):
        if passwordString[i] == passwordString[i+1]:
            adjacentDigits = True
        if passwordString[i] > passwordString[i+1]:
            alwaysIncreasing = False
    return (adjacentDigits and alwaysIncreasing)

minPassword = 108457
maxPassword = 562041

validPasswords = 0
for password in range(minPassword,maxPassword+1):
    if validPassword(password):
        validPasswords += 1

print(validPasswords)
