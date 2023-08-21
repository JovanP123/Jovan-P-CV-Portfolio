import turtle
pen = turtle.Turtle()
pen.speed(100)
import math
class cords:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def degToRad(deg):
    return deg*(math.pi/180)
def distanceBetweenPoints(cords1,cords2):
    return math.sqrt((cords2.x-cords1.x)**2+(cords2.y-cords1.y)**2)

def drawX(catLen):
    pen.penup()
    pen.goto(catLen,catLen)
    pen.pendown()
    pen.goto(-catLen,-catLen)
    pen.penup()
    pen.goto(-catLen,catLen)
    pen.pendown()
    pen.goto(catLen,-catLen)
    pen.penup()
    pen.goto(0,0)
    
def twoDRotationAroundOrigin(startingPoint, angle):
    return cords(startingPoint.x*math.cos(degToRad(angle))-startingPoint.y*math.sin(degToRad(angle)),startingPoint.x*math.sin(degToRad(angle))+startingPoint.y*math.cos(degToRad(angle)))

def drawCircleAtCords(center,radius):
    pen.penup()
    pen.goto(center.x,center.y-radius)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

def movedAwayFromCenterNewPosition(newWorldAngle, oldCords, summedDistanceToNewPoint):
    if newWorldAngle==90:
        newWorldAngle=89
    elif newWorldAngle==270:
        newWorldAngle=269
    tgA = math.tan(degToRad(newWorldAngle))
    rdcl1 = oldCords.y-tgA*oldCords.x
    rdcl2 = 1+tgA**2
    x1 = (-tgA*rdcl1+math.sqrt(tgA**2*rdcl1**2-rdcl2*(rdcl1**2-summedDistanceToNewPoint**2)))/rdcl2
    x2 = (-tgA*rdcl1-math.sqrt(tgA**2*rdcl1**2-rdcl2*(rdcl1**2-summedDistanceToNewPoint**2)))/rdcl2
    y1 = tgA*x1 + rdcl1
    y2 = tgA*x2 + rdcl1
    if newWorldAngle<=90 and (x1>=0 and y1>=0):
        return cords(x1,y1)
    else:
        return cords(x2,y2)
    if newWorldAngle<=180 and newWorldAngle>90 and (x1<=0 and y1>=0):
        return cords(x1,y1)
    else:
        return cords(x2,y2)
    if newWorldAngle<=270 and newWorldAngle>180 and (x1<=0 and y1<=0):
        return cords(x1,y1)
    else:
        return cords(x2,y2)
    if newWorldAngle<360 and newWorldAngle>270 and (x1>=0 and y1<=0):
        return cords(x1,y1)
    else:
        return cords(x2,y2)
def distancingFunction(x,it):
    return it-x/it

#MAIN FUNCTION
def drawFlowerPattern(fraction,iterations):
    pen.clear()
    xLineLen = 5
    drawX(xLineLen)
    crclRadius = 5
    halfXHorizontalLength = (xLineLen*math.sqrt(2))/4+xLineLen*2
    moveAwayCoef = 1/1.0005
    currentPoint = cords(halfXHorizontalLength+moveAwayCoef,0)
    angleFraction = 360 * fraction
    angleSum = 0
    passedIterations = 0
    drawCircleAtCords(currentPoint,crclRadius)
    angleSum += angleFraction
    while passedIterations!=iterations:
        currentPoint = twoDRotationAroundOrigin(currentPoint,angleFraction)
        drawCircleAtCords(currentPoint,crclRadius)
        angleSum += angleFraction
        if angleSum>=360:
            angleSum -= 360
            passedIterations += 1
            currentPoint = movedAwayFromCenterNewPosition(angleSum,currentPoint,(distanceBetweenPoints(currentPoint,cords(0,0))+halfXHorizontalLength))#old setup - distanceBetweenPoints(currentPoint,cords(0,0))+halfXHorizontalLength
    pen.goto(0,0)
