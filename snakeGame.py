from microbit import *
import random

#Snake game for BBC microbit
#Copy this code into https://python.microbit.org/v/3 to test it out

#-Moves the entire snake
#-It does that by turning off the light of the current position of the certain part of
#the body and turning on the light that is in the direction of the movement of that part 
#of the body
#-The turning points array is taken and the position of every part of the snake
#is changed accordingly to their direction of movement. If a part of the body 
#is met with a turning point, its direction of movement will change respectively
def moveSnake(snake,turningPoints):
    for i in range(len(snake)):
        for j in range(len(turningPoints)):
            try:
                if snake[i][0]==turningPoints[j][0] and snake[i][1]==turningPoints[j][1]:
                    snake[i][2] = turningPoints[j][2]
                    if i+1 == len(snake):
                        turningPoints.remove(turningPoints[j])
            except:
                IndexError
        display.set_pixel(snake[i][0],snake[i][1],0)
        try:
            snake[i][0] += snake[i][2][0]
            snake[i][1] += snake[i][2][1]
        except IndexError:
            return 0
        try:
            display.set_pixel(snake[i][0],snake[i][1],9)
        except ValueError:
            return 0

#-Spawns food
def spawnFood():
    while True:
        x = random.randint(0,4)
        y = random.randint(0,4)
        if (display.get_pixel(x,y) == 0):
            display.set_pixel(x,y,5)
            return [x,y]
        else:
            continue

#-Checks if the food has been eaten, if true then we add a new part to the body of the snake
#that has the same direction of movement as the last snake, and its placed behind the last part
#of the snake, in the opposite direction of the direction of movement of the last part of the snake
def checkIfFoodEaten(snk,foodCords):
    if snk[0][0]==foodCords[0] and snk[0][1]==foodCords[1]:
        isFood = False
        snk.append([snk[-1][0]-snk[-1][2][0],snk[-1][1]-snk[-1][2][1],snk[-1][2]])
        return False
    return True

#-Checks if the snake has hit its self. It does that by checking
#if the coordinates of the head are equal to any other coordinates of the body, and if
#yes than its game over
def checkIfHitSelf(snk):
    for i in range(len(snk)):
        try:
            if snk[0][0]==snk[i+1][0] and snk[0][1]==snk[i+1][1]:
                return True
        except:
            IndexError
    return False
        
mainSnake = [[0,4,[0,-1]]]
turnPoints = []
numberOfTurnPoints = 0
countdown = 3
foodPos = []
food = False
win = False

#-A three second countdown
while countdown!=0:
    display.show(countdown)
    sleep(1000)
    countdown -= 1
display.clear()
display.set_pixel(0,4,9)

#-Gameplay
while True:
    #-If the parts of the body is equal to the maximum number of pixels on the screen
    #(5x5), that means that the snake has filled all of the screen, which means that
    #the player has won
    if len(mainSnake)==25:
        win = True
        break
    #-Checks if there's food on the screen, if not then it spawns a new one
    if not food:
        foodPos = spawnFood()
        food = True
    #-The programm is frozen less and less as the length of the snake grows
    sleep(1000-(len(mainSnake)-1)*36)
    #-When the player presses the right or left button, we create a turning point
    #where the head is at the moment of pressing. Then at that point we make a 
    #directional change to the vector of movement for every single part of the snake
    #-After the last part of the snake has passed the turning point, that point is deleted
    if button_a.was_pressed():
        numberOfTurnPoints += 1
        turnPoints.append([mainSnake[0][0],mainSnake[0][1],[]])
        if mainSnake[0][2]==[0,-1]:
            turnPoints[-1][2] = [-1,0]
        elif mainSnake[0][2]==[1,0]:
            turnPoints[-1][2] = [0,-1]
        elif mainSnake[0][2]==[0,1]:
            turnPoints[-1][2] = [1,0]
        elif mainSnake[0][2]==[-1,0]:
            turnPoints[-1][2] = [0,1]
    elif button_b.was_pressed():
        numberOfTurnPoints += 1
        turnPoints.append([mainSnake[0][0],mainSnake[0][1],[]])
        if mainSnake[0][2]==[0,-1]:
            turnPoints[-1][2] = [1,0]
        elif mainSnake[0][2]==[1,0]:
            turnPoints[-1][2] = [0,1]
        elif mainSnake[0][2]==[0,1]:
            turnPoints[-1][2] = [-1,0]
        elif mainSnake[0][2]==[-1,0]:
            turnPoints[-1][2] = [0,-1]
    #-If this function return 0, that means that the snake has hit a wall, or it has
    if moveSnake(mainSnake,turnPoints)==0:
        break
    #-We check if the food has been eaten, and set the boolean "food" accordingly
    food = checkIfFoodEaten(mainSnake,foodPos)
    if food:
        display.set_pixel(foodPos[0],foodPos[1],5)
    #-This checks if the head has hit a part of the snake
    if checkIfHitSelf(mainSnake):
        break

#-If the win boolean is true, the screen will display a "W", if not, an "L"
if win:
    display.show("W")
else:
    display.show("L")