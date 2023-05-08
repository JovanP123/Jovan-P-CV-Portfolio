import random
import math

#Minesweeper game

#Check if the newly generated mine coordinates are the same as a previous mine
def alreadyAMineThere(minesPar, newMineCordsPar):
    for i in range(len(minesPar)):
        if minesPar[i] == newMineCordsPar: return True
    return False

#Check if the point selected is a mine
def checkIfMinePoint(pointCordsPar, minesCordsPar):
    for i in range(len(minesCordsPar)):
        if pointCordsPar == minesCordsPar[i]:
            return True
    return False

#Print out the mine field
def printOutArray(fieldPar):
    for i in range(len(field)):
        for j in range(len(field)):
            if j==0: row = fieldPar[i][j]
            else: row += " " + fieldPar[i][j]
        print(row)

#Calculate the value of a field point by seeing how many mines are around it
def pointNumber(minesPar, pointPar):
    num = 0
    for i in range(len(minesPar)):
        distanceFromAMine = math.sqrt((int(minesPar[i][0])-int(pointPar[0]))**2 + (int(minesPar[i][1])-int(pointPar[1]))**2)
        if distanceFromAMine<1.44:
            num+=1
    return num
    
#Return the surrounding points around a certain point
#(the algorithm could be faster but it would take more space to code)
def surroundingPoints(fieldPar,markedFieldPar, pointPar):
    surroundingPointsList = []
    surroundingZeros = []
    for i in range(len(fieldPar)):
        for j in range(len(fieldPar)):
            if math.sqrt((i-pointPar[0])**2+(j-pointPar[1])**2) < 1.44 and markedFieldPar[i][j]!='0' and fieldPar[i][j]=="X" and markedFieldPar[i][j]!="B":
                surroundingPointsList.append([i,j])
            elif math.sqrt((i-pointPar[0])**2+(j-pointPar[1])**2) < 1.44 and markedFieldPar[i][j]=='0' and fieldPar[i][j]=="X" and markedFieldPar[i][j]!="B":
                surroundingZeros.append([i,j])
    return [surroundingZeros,surroundingPointsList]

#Replaces the covered field point with its value
def uncoverPoint(fieldPar, markedFieldPar, pointPar):
    newField = fieldPar
    newField[pointPar[0]][pointPar[1]] = markedFieldPar[pointPar[0]][pointPar[1]]
    return newField

#When a zero field point is uncovered, all the surrounding points that are zeros and the points that have a bigger value than zero
#and are neighbouring those zeros will be uncovered, thus a special algorithm is needed for this "chain" of uncovering
def uncoverZerosChain(fieldPar,markedFieldPar,uncoveredPointPar):
    newField = fieldPar
    neigbhouringPoint = surroundingPoints(fieldPar,markedFieldPar,uncoveredPointPar)
    for i in range(len(neigbhouringPoint[0])):
        newField = uncoverPoint(fieldPar,markedFieldPar,neigbhouringPoint[0][i])
    for i in range(len(neigbhouringPoint[1])):
        newField = uncoverPoint(fieldPar,markedFieldPar,neigbhouringPoint[1][i])
    otherZeros = neigbhouringPoint[0]
    while len(otherZeros)!=0:
        surroundingTheZero = surroundingPoints(newField,markedFieldPar,otherZeros[0])
        for i in range(len(surroundingTheZero[0])):
            newField = uncoverPoint(newField,markedFieldPar,surroundingTheZero[0][i])
        for i in range(len(surroundingTheZero[1])):
            newField = uncoverPoint(newField,markedFieldPar,surroundingTheZero[1][i])
        otherZeros.remove(otherZeros[0])
        for i in range(len(surroundingTheZero[0])):
            otherZeros.append(surroundingTheZero[0][i])
    return newField

#A function that checks if the remaining field points, flagged or not, are just bombs, if yes
#then the player has won
def checkIfHasWon(fieldPar,markedFieldPar):
    for i in range(len(fieldPar)):
        for j in range(len(fieldPar)):
            if fieldPar[i][j] == "X" and markedFieldPar[i][j] != "B" or fieldPar[i][j]=="F" and markedField[i][j]!="B":
                return False
    return True

#Take input from user
field = []
lengthOfField = int(input("Insert the length of the field:"))
numberOfMines = int(input("Insert the number of mines:"))
for i in range(lengthOfField):
    field.append([])
    for j in range(lengthOfField):
        field[i].append("X")

#Create mines
minesCords = []
for i in range(numberOfMines):
    while True:
        xCor = random.randint(0,lengthOfField-1)
        yCor = random.randint(0,lengthOfField-1)
        if not alreadyAMineThere(minesCords,[xCor,yCor]):
            minesCords.append([xCor,yCor])
            break

#Mark the field with the mines and the free fields with its numbers
markedField = []
for i in range(lengthOfField):
    markedField.append([])
    for j in range(lengthOfField):
        if checkIfMinePoint([i,j],minesCords):
            markedField[i].append("B")
        else:
            markedField[i].append(str(pointNumber(minesCords,[i,j])))

#Gameplay
flaggedBombs = 0
while True:
    printOutArray(field)
    #Taking the desicion of the player
    desicion = input("Flag/Unflag/Uncover:")
    desicion = desicion.split(" ")
    coordinates = desicion[1].split(",")
    coordinates[0] = int(coordinates[0]) - 1
    coordinates[1] = int(coordinates[1]) - 1
    #Check if the input coordinates are out of bound
    if coordinates[0]>=lengthOfField or coordinates[1]>=lengthOfField:
        print("That point is out of bounds!")
    #If the desicion is to flag a field, first we check if the field 
    if desicion[0] == "Flag":
        if field[coordinates[0]][coordinates[1]] != "X":
            print("You can't flag an open field")
        else:
            field[coordinates[0]][coordinates[1]] = "F"
            if checkIfMinePoint(coordinates,minesCords):
                flaggedBombs += 1
    elif desicion[0] == "Unflag":
        if field[coordinates[0]][coordinates[1]] == "F": 
            field[coordinates[0]][coordinates[1]] = "X"
            if markedField[coordinates[0]][coordinates[1]]=="B":
                flaggedBombs -= 1
        else: print("That field is not flagged")
    if desicion[0] == "Uncover":
        if checkIfMinePoint(coordinates,minesCords):
            print("YOU UNCOVERED A MINE!!! GAME OVER")
            for i in range(len(field)):
                for j in range(len(field)):
                    if checkIfMinePoint([i,j],minesCords) and field[i][j]=="X":
                        field[i][j] = "B"
            printOutArray(field)
            numOfMinesGuessed = 0
            if flaggedBombs==1:
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
    if checkIfHasWon(field, markedField):
        printOutArray(field)
        print("YOU WON!")
        break