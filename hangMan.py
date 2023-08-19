import turtle
gT = turtle.Turtle()
gT.pencolor("black")

#Graphics and Hangman Logic--------

#Hangman Graphics
def goMidPen():
  gT.penup()
  gT.goto(0,0)

def goBackPen(mltp):
  gT.penup()
  gT.goto(5*mltp,5*mltp)


def standOne(goBackBool,multplyr):
  gT.penup()
  gT.goto(-4*multplyr,-5*multplyr)
  gT.pendown()
  gT.goto(-2*multplyr,-5*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def standTwo(goBackBool,multplyr):
  gT.penup()
  gT.goto(-3*multplyr,-5*multplyr)
  gT.pendown()
  gT.goto(-3*multplyr,5*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def standThree(goBackBool,multplyr):
  gT.penup()
  gT.goto(-3*multplyr,5*multplyr)
  gT.pendown()
  gT.goto(3*multplyr,5*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def standFour(goBackBool,multplyr):
  gT.penup()
  gT.goto(-3*multplyr,4*multplyr)
  gT.pendown()
  gT.goto(-2*multplyr,5*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return

def ropeTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,5*multplyr)
  gT.pendown()
  gT.goto(3*multplyr,4*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def headTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(2*multplyr,4*multplyr)
  gT.pendown()
  gT.goto(4*multplyr,4*multplyr)
  gT.goto(4*multplyr,2*multplyr)
  gT.goto(2*multplyr,2*multplyr)
  gT.goto(2*multplyr,4*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def leftEyeTurtle(goBackBool,multplyr,fillColor):
  gT.penup()
  gT.goto(2.25*multplyr,3.75*multplyr)
  gT.pendown()
  gT.fillcolor(fillColor)
  gT.begin_fill()
  gT.goto(2.75*multplyr,3.75*multplyr)
  gT.goto(2.75*multplyr,3.25*multplyr)
  gT.goto(2.25*multplyr,3.25*multplyr)
  gT.goto(2.25*multplyr,3.75*multplyr)
  gT.end_fill()
  if goBackBool==True:
    goBackPen(multplyr)
  return
def rightEyeTurtle(goBackBool,multplyr,fillColor):
  gT.penup()
  gT.goto(3.25*multplyr,3.75*multplyr)
  gT.pendown()
  gT.fillcolor(fillColor)
  gT.begin_fill()
  gT.goto(3.75*multplyr,3.75*multplyr)
  gT.goto(3.75*multplyr,3.25*multplyr)
  gT.goto(3.25*multplyr,3.25*multplyr)
  gT.goto(3.25*multplyr,3.75*multplyr)
  gT.end_fill()
  if goBackBool==True:
    goBackPen(multplyr)
  return
def noseTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,3.2*multplyr)
  gT.pendown()
  gT.goto(3*multplyr,2.75*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def mouthTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(2.25*multplyr,2.3*multplyr)
  gT.pendown()
  gT.goto(3.75*multplyr,2.3*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def bodyTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,2*multplyr)
  gT.pendown()
  gT.goto(3*multplyr,-2*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def leftArmTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,1*multplyr)
  gT.pendown()
  gT.goto(2*multplyr,-1*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def rightArmTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,1*multplyr)
  gT.pendown()
  gT.goto(4*multplyr,-1*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def leftLegTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,-2*multplyr)
  gT.pendown()
  gT.goto(2*multplyr,-4*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return
def rightLegTurtle(goBackBool,multplyr):
  gT.penup()
  gT.goto(3*multplyr,-2*multplyr)
  gT.pendown()
  gT.goto(4*multplyr,-4*multplyr)
  if goBackBool==True:
    goBackPen(multplyr)
  return

def hangStand(goBackBool,multplyr):
  standOne(goBackBool,multplyr)
  standTwo(goBackBool,multplyr)
  standThree(goBackBool,multplyr)
  standFour(goBackBool,multplyr)

def clearBoard(multplyr,count):
  gT.pencolor("white")
  time_ = 1
  for i in range(count):
    if time_==1:
      ropeTurtle(False,multplyr)
    if time_==2:
      headTurtle(False,multplyr)
    if time_==3:
      leftEyeTurtle(False,multplyr,"white")
    if time_==4:
      rightEyeTurtle(False,multplyr,"white")
    if time_==5:
      noseTurtle(False,multplyr)
    if time_==6:
      mouthTurtle(False,multplyr)
    if time_==7:
      bodyTurtle(False,multplyr)
    if time_==8:
      leftArmTurtle(False,multplyr)
    if time_==9:
      rightArmTurtle(False,multplyr)
    if time_==10:
      leftLegTurtle(False,multplyr)
    if time_==11:
      rightLegTurtle(False,multplyr)
    time_ += 1
  hangStand(False,multplyr)
  goBackPen(multplyr)
  gT.pencolor("black")
  gT.fillcolor("black")

#Hang Logic

def hangTheMan(times,multplyr,prtCount):
  for i in range(times):
    if prtCount==1:
      ropeTurtle(True,multplyr)
      continue
    if prtCount==2:
      headTurtle(True,multplyr)
      continue
    if prtCount==3:
      leftEyeTurtle(True,multplyr,"black")
      continue
    if prtCount==4:
      rightEyeTurtle(True,multplyr,"black")
      continue
    if prtCount==5:
      noseTurtle(True,multplyr)
      continue
    if prtCount==6:
      mouthTurtle(True,multplyr)
      continue
    if prtCount==7:
      bodyTurtle(True,multplyr)
      continue
    if prtCount==8:
      leftArmTurtle(True,multplyr)
      continue
    if prtCount==9:
      rightArmTurtle(True,multplyr)
      continue
    if prtCount==10:
      leftLegTurtle(True,multplyr)
      continue
    if prtCount==11:
      rightLegTurtle(True,multplyr)
      continue

#--------

novRed = "\n"

def hideWord():
  for i in range(100):
    print("|")
  print(novRed)

def gameOn(dashed,word,tableMult,gubBuk,gubZbo):
  hangStand(False,tableMult)
  goBackPen(tableMult)
  partCount = 0
  while True:
    for pl in range(numOfPlayers-1):
      playerInput = input(player + str(pl+1) + ":")
      print(novRed)
      if len(playerInput)==1:
        hangWordSplit = list(word)
        if playerInput in hangWordSplit:
          shownLetters = 0
          for i in range(len(dashed)):
            if playerInput==hangWordSplit[i]:
              if playerInput==dashed[i]:
                shownLetters += 1
              dashedTempList = list(dashed)
              dashedTempList[i] = hangWordSplit[i]
              dashed = ''.join(dashedTempList)
          guessedLetters = 0
          for m in range(len(word)):
            if playerInput==word[m]:
              guessedLetters += 1
          guessedLetters -= shownLetters
          if guessedLetters==1:
            print(player + str(pl+1) + " погоди една буква:")
            print(novRed)
            print(dashed)
            print(novRed)
          if guessedLetters>1:
            print(player + str(pl+1) + " погоди " + str(guessedLetters) + " букви.")
            print(novRed)
            print(dashed)
            print(novRed)
          if guessedLetters==0 and shownLetters==1:
            print("Таа буква е веќе откирена. Нема друга.")
            print(novRed)
            print(dashed)
            print(novRed)
            #Hang The Man
            for g in range(gubBuk):
              partCount += 1
              hangTheMan(1,tableMult,partCount)
            if partCount==11 or partCount>11:
              print("Измислувачот победи. Човекот е целосно обесен.")
              print(novRed)
              print("Зборот беше - "+word)
              print(novRed)
          if guessedLetters==0 and shownLetters>1:
            print("Таа буква ги откри сите исти букви. Нема други.")
            print(novRed)
            print(dashed)
            print(novRed)
            #Hang The Man
            for l in range(gubBuk):
              partCount += 1
              hangTheMan(1,tableMult,partCount)
            if partCount==11 or partCount>11:
              print("Измислувачот победи. Човекот е целосно обесен.")
              print(novRed)
              print("Зборот беше - "+word)
              print(novRed)
              clearBoard(tableMult,11)
              return
          for j in range(len(dashed)):
            if dashed[j]=="-":
              break
            if (j+1)==len(dashed) and dashed[j]!="-":
              if guessedLetters==1:
                print(player + str(pl+1) + " ја погоди последната буква и победи.")
              elif guessedLetters>1:
                print(player + str(pl+1) + " ги погоди последните" + guessedLetters + " букви и победи.")
              print(novRed) 
              print(word)
              print(novRed)
              clearBoard(tableMult,partCount)
              return
        if playerInput not in hangWordSplit:
          print(player + str(pl+1) + " не погоди буква од зборот")
          print(novRed)
          #Hang The Man
          for k in range(gubBuk):
            partCount += 1
            hangTheMan(1,tableMult,partCount)
          if partCount==11 or partCount>11:
            print("Измислувачот победи. Човекот е целосно обесен.")
            print(novRed)
            print("Зборот беше - "+word)
            print(novRed)
            clearBoard(tableMult,11)
            return
          print(dashed)
          print(novRed)
          
      if len(playerInput)>1:
        if playerInput == word:
          print(player + str(pl+1) + " го погоди зборот и победи!")
          print(novRed)
          clearBoard(tableMult,partCount)
          return
        if playerInput != word:
          print(player + str(pl+1) + " не го погоди зборот.")
          print(novRed)
          #Hang The Man
          for s in range(gubZbo):
            partCount+=1
            hangTheMan(1,tableMult,partCount)
          if partCount==11 or partCount>11:
            print("Измислувачот победи. Човекот е целосно обесен.")
            print(novRed)
            print("Зборот беше - "+word)
            print(novRed)
            clearBoard(tableMult,11)
            return
          print(dashed)
          print(novRed)

userIn = ""
again = None

#Gameplay
while True:
  if again!=True:
    userIn = input("Играј? д|н:")
    print(novRed)
  if again==True:
    userIn = input("Играј пак? д|н:")
    print(novRed)

  if userIn=="д":
    player = "Играч Број "
    if again!=True:
      numOfPlayers = int(input("Број на играчи:"))
      print(novRed)
      tableMult = int(input("Големина на бесилката (x?):"))
      print(novRed)
      gubenjeBukva = int(input("Делови да се цртаат за погрешна буква:"))
      print(novRed)
      gubenjeZbor = int(input("Делови да се цртаат за погрешен збор:"))
      print(novRed)
    gameIn = input("Збор на Измислувачот:")
    print(novRed)
    word = gameIn
    dashed = ""
    for i in range(len(gameIn)):
      dashed += "-"
    
    hideWord()
    tempDashedList = list(dashed)
    tempDashedList[0] = word[0]
    tempDashedList[-1] = word[-1]
    dashed = ''.join(tempDashedList)
    print(dashed)
    print(novRed)

    
    gameOn(dashed,word,tableMult,gubenjeBukva,gubenjeZbor)
    goMidPen()

  again = True
  if userIn=="н":
    goMidPen()
    break
