import random
import math

#-Minesweeper game in Terminal

#-Check if the newly generated mine coordinates are the same as a previous mine
def alreadyAMineThere(minesPar, newMineCordsPar):
    for i in range(len(minesPar)):
        if minesPar[i] == newMineCordsPar: return True
    return False

#-Check if the point selected is a mine
def checkIfMinePoint(pointCordsPar, minesCordsPar):
    for i in range(len(minesCordsPar)):
        if pointCordsPar == minesCordsPar[i]:
            return True
    return False

#-Print out the mine field
def printOutArray(fieldPar):
    for i in range(len(field)):
        for j in range(len(field)):
            if j==0: row = fieldPar[i][j]
            else: row += " " + fieldPar[i][j]
        print(row)

#-Calculate the value of a field point by seeing how many mines are around it

#-Since we have the coordinates of the mienes, we can just calculate the distance between every mine and 
#the field point in question, and if the distance is less than 1.44 (we put this value because
#we are taking into consideration the points that are diagonal to the point in question, and the distance
#between two neighbouring diagonal points is square root of 2, which is around 1.41) then a mine is neighbouring
#that point and we add one to the value of the field point
def pointNumber(minesPar, pointPar):
    num = 0
    for i in range(len(minesPar)):
        distanceFromAMine = math.sqrt((int(minesPar[i][0])-int(pointPar[0]))**2 + (int(minesPar[i][1])-int(pointPar[1]))**2)
        if distanceFromAMine<1.44:
            num+=1
    return num
    
#-Return the surrounding points around a certain point
#-We do that by checking all surrounding points via the surroundingValues list of operations that
#we need to do to the x and y coordinates of the point in question, and we check if the values after 
#the operations are within the range of values that are in bounds of the field, so that we won't get an IndexError
def surroundingCoveredPoints(fieldPar,markedFieldPar, pointPar):
    surroundingPointsList = []
    surroundingZerosList = []
    surroundingValues = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(8):
        if (pointPar[0]+surroundingValues[i][0]>=0 and pointPar[1]+surroundingValues[i][1]>=0 and pointPar[0]+surroundingValues[i][0]<len(fieldPar) and pointPar[1]+surroundingValues[i][1]<len(fieldPar)):
            if (markedFieldPar[pointPar[0]+surroundingValues[i][0]][pointPar[1]+surroundingValues[i][1]]!="B" and fieldPar[pointPar[0]+surroundingValues[i][0]][pointPar[1]+surroundingValues[i][1]]=="X"):
                if (markedFieldPar[pointPar[0]+surroundingValues[i][0]][pointPar[1]+surroundingValues[i][1]]=='0'):
                    surroundingZerosList.append([pointPar[0]+surroundingValues[i][0],pointPar[1]+surroundingValues[i][1]])
                    continue
                surroundingPointsList.append([pointPar[0]+surroundingValues[i][0],pointPar[1]+surroundingValues[i][1]])
    return [surroundingZerosList,surroundingPointsList]
    

#-Replaces the covered field point with its value
def uncoverPoint(fieldPar, markedFieldPar, pointPar):
    newField = fieldPar
    newField[pointPar[0]][pointPar[1]] = markedFieldPar[pointPar[0]][pointPar[1]]
    return newField

#-When a zero field point is uncovered, all the surrounding points that are zeros and the points that have a bigger value than zero
#and are neighbouring those zeros will be uncovered, thus a special algorithm is needed for this "chain" of uncovering field points
def uncoverZerosChain(fieldPar,markedFieldPar,uncoveredPointPar):
    newField = fieldPar
    neighbouringPoint = surroundingCoveredPoints(fieldPar,markedFieldPar,uncoveredPointPar)
    for i in range(len(neighbouringPoint[0])):
        newField = uncoverPoint(fieldPar,markedFieldPar,neighbouringPoint[0][i])
    for i in range(len(neighbouringPoint[1])):
        newField = uncoverPoint(fieldPar,markedFieldPar,neighbouringPoint[1][i])
    otherZeros = neighbouringPoint[0]
    while len(otherZeros)!=0:
        surroundingTheZero = surroundingCoveredPoints(newField,markedFieldPar,otherZeros[0])
        for i in range(len(surroundingTheZero[0])):
            newField = uncoverPoint(newField,markedFieldPar,surroundingTheZero[0][i])
        for i in range(len(surroundingTheZero[1])):
            newField = uncoverPoint(newField,markedFieldPar,surroundingTheZero[1][i])
        otherZeros.remove(otherZeros[0])
        for i in range(len(surroundingTheZero[0])):
            otherZeros.append(surroundingTheZero[0][i])
    return newField

#-A function that checks if the remaining field points, flagged or not, are just mines, if yes
#then the player has won
def checkIfHasWon(fieldPar,markedFieldPar):
    for i in range(len(fieldPar)):
        for j in range(len(fieldPar)):
            if fieldPar[i][j] == "X" and markedFieldPar[i][j] != "B" or fieldPar[i][j]=="F" and markedField[i][j]!="B":
                return False
    return True

#-Take input from user
field = []
lengthOfField = int(input("Insert the length of the field:"))
numberOfMines = int(input("Insert the number of mines:"))
for i in range(lengthOfField):
    field.append([])
    for j in range(lengthOfField):
        field[i].append("X")

#-Create mines
minesCords = []
for i in range(numberOfMines):
    while True:
        xCor = random.randint(0,lengthOfField-1)
        yCor = random.randint(0,lengthOfField-1)
        if not alreadyAMineThere(minesCords,[xCor,yCor]):
            minesCords.append([xCor,yCor])
            break

#-Mark the field with the mines and the free fields with its numbers
markedField = []
for i in range(lengthOfField):
    markedField.append([])
    for j in range(lengthOfField):
        if checkIfMinePoint([i,j],minesCords):
            markedField[i].append("B")
        else:
            markedField[i].append(str(pointNumber(minesCords,[i,j])))

#-Gameplay
flaggedMines = 0
while True:
    printOutArray(field)
    #-Taking the desicion of the player
    desicion = input("Flag/Unflag/Uncover:")
    desicion = desicion.split(" ")
    coordinates = desicion[1].split(",")
    coordinates[0] = int(coordinates[0]) - 1
    coordinates[1] = int(coordinates[1]) - 1
    #-Check if the input coordinates are out of bound
    if coordinates[0]>=lengthOfField or coordinates[1]>=lengthOfField:
        print("That point is out of bounds!")
    #-If the desicion is to flag a field, first we check if the field is covered, because we can't flag an open field,
    #then, we check via the marked field if the player has flagged a mine, if so we add to the flaggedMines counter
    if desicion[0] == "Flag":
        if field[coordinates[0]][coordinates[1]] != "X":
            print("You can't flag an open point")
        else:
            field[coordinates[0]][coordinates[1]] = "F"
            if checkIfMinePoint(coordinates,minesCords):
                flaggedMines += 1
    #-This will return the point to being uncovered, if the chosen point is a flagged point
    #it will unflag it, and if there is a mine on that flagged point, it will subtract from the flaggedMines counter
    elif desicion[0] == "Unflag":
        if field[coordinates[0]][coordinates[1]] == "F": 
            field[coordinates[0]][coordinates[1]] = "X"
            if markedField[coordinates[0]][coordinates[1]]=="B":
                flaggedMines -= 1
        else: print("That point is not flagged")
    #-This will uncover the field, there are four cases
    #1. If the point value is a number bigger than one, than we just uncover the chosen point
    #2. If the point value is zero, than we do the zeros chain uncovering funcion
    #3. If the point we uncovered is flagged, we restart since we don't want to uncover a flagged point
    #4. If the point is a bomb, it's game over
    elif desicion[0] == "Uncover":
        if checkIfMinePoint(coordinates,minesCords):
            print("YOU UNCOVERED A MINE!!! GAME OVER")
            for i in range(len(field)):
                for j in range(len(field)):
                    if checkIfMinePoint([i,j],minesCords) and field[i][j]=="X":
                        field[i][j] = "B"
            printOutArray(field)
            numOfMinesGuessed = 0
            if flaggedMines==1:
                print("You flagged 1 mine")
            else:
                print("You flagged "+str(numOfMinesGuessed)+" mines")
            break
        elif field[coordinates[0]][coordinates[1]]=="F":
            print("You can't uncover a flagged point, you have to unflag it first")
        elif int(markedField[coordinates[0]][coordinates[1]]) >= 1:
            field[coordinates[0]][coordinates[1]] = markedField[coordinates[0]][coordinates[1]]
        else:
            field = uncoverZerosChain(field, markedField, coordinates)
    #This checks if the player has won using the function check if has won
    if checkIfHasWon(field, markedField):
        printOutArray(field)
        print("YOU WON!")
        break
