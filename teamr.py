from turtle import *
import math
from random import *
r= Turtle()
colormode(255)
tracer(0)

def randomRed():
    #By rishil patel
    red = (randint(100,255),0,0)
    return red
def randomBlue():
    #By rishil patel
    blue = (0,0,randint(100,255))
    return blue
def randomGreen():
    #By rishil patel
    green = (0,randint(100,255),0)
    return green
def randomYellow():
    #By rishil patel
    yellow = (randint(150,255),randint(150,255),0)
    return yellow
def randomOrange():
    #By rishil patel
    orange = (255,randint(100,200),0)
    return orange
def randomPurple():
    #By rishil patel
    purple = (randint(100,255),0,randint(100,255))
    return purple

def drawCircle(centerX,centerY,radius,color):
    #By rishil patel
    r.penup()
    r.goto(centerX,centerY)
    r.setheading(0)
    r.forward(radius)
    r.left(90)
    r.fillcolor(color)
    r.begin_fill()
    r.pendown()
    r.pencolor("black")
    for i in range(360):
        r.forward(2*math.pi*(radius/360))
        r.left(1)
    r.end_fill()

def createRipple():
    #By rishil Patel
    r.setheading(270) #face south
    for i in range(180): #create a half circle
        r.forward(1)
        r.right(1)
def createWaves():
    #By rishil Patel
    xcoordinate = r.xcor()
    ycoordinate = r.ycor()
    r.penup()
    r.goto(randint(-450,450),randint(-400,400)) #top right corner
    r.pencolor("blue")
    r.fillcolor("blue")
    r.begin_fill()
    r.pendown()
    for i in range(4): #create 4 ripples
        createRipple()
    r.setheading(270)
    r.forward(700) #go to bottom left corner
    r.left(90)
    r.forward(1200) #go to bottom right corner
    r.left(90)
    r.forward(700)
    # r.goto(xcoordinate+475,ycoordinate-200) #go to top right corner
    r.end_fill()

def drawLand():
    #By rishil Patel
    r.penup()
    r.goto(-500,200)
    r.pencolor("light green") #color of the land
    r.begin_fill()
    r.fillcolor("light green")
    r.pendown()
    r.right(90)
    r.forward(800)
    r.left(90)
    r.forward(1000) #goes to the wave's edge
    r.left(90)
    r.forward(800)
    r.left(90)
    r.forward(1000) #goes to the wave's edge
    r.end_fill() #fills half the page with the land
def drawOneSeaweed():
    #By rishil patel
    r.pencolor("black")
    r.fillcolor(randomGreen())
    r.begin_fill()


    diameter = 20 #make a semicircle
    for i in range(10):
        r.circle((diameter/2), 180,)
        r.left(90)
        r.forward(diameter)
        r.forward(-diameter)
        r.right(90)

        r.circle((-diameter/2), 180) #make another semicircle but in the opposite direction so that it does not form a complete circle
        r.right(90)
        r.forward(diameter)
        r.forward(-diameter)
        r.left(90)
        position = r.ycor()
    if position > 170: #stop seaweed if it goes above the waves
        r.penup()
        r.end_fill()
    r.end_fill()

def drawAllSeaweed(): #repeats drawoneseaweed function
    #By rishil patel
    for i in range(1):
        r.penup()
        r.goto(randint(-450,450),randint(-400,400))
        r.setheading(0)
        drawOneSeaweed()

def drawOneFish():
    #By rishil patel
    r.penup()
    r.goto(randint(-450,450),randint(-400,400))
    r.pendown()
    colors = [randomRed(),randomGreen(),randomBlue(),randomYellow(),randomOrange(),randomPurple()]
    r.fillcolor(choice(colors)) #random fill color
    r.begin_fill()
    r.left(60)
    number = 50
    number = number/100 #divides the number by 100 to make the fish body smaller
    for i in range(120):

        r.forward(number)
        r.right(1)
    r.right(60)
    for i in range(120):

        r.forward(number) #Goes to position to make the tail
        r.right(1)
    r.right(60)
    for i in range(120):

        r.forward(number)
        r.right(1)
    r.forward(30*number) #draws fish tail (makes the tail proportional to the fish body)
    r.left(150)
    r.forward(50*number)
    r.left(150)
    r.forward(30*number)
    r.end_fill()
    r.right(60)


def drawBird():
  #by Shayan Manoharan
  r.penup()
  r.fillcolor(0,0,0)
  r.goto(randint(-450,450),randint(200,400))
  r.begin_fill()
  r.pencolor("black")
  r.pendown()
  r.setheading(0)
  for i in range(30):
    r.forward(1)
    r.right(2)
  r.setheading(45)
  for i in range(30):
    r.forward(1)
    r.right(2)
  r.left(170)
  for i in range(30):
    r.forward(1)
    r.left(2)
  r.setheading(135)
  for i in range(30):
    r.forward(1)
    r.left(2)
  r.penup()
  r.end_fill()



def drawStickPerson():
  #by sangeev p
  r.penup()
  r.setheading(0)
  r.goto(randint(-450,450),randint(-400,200))
  r.pencolor("black")
  r.fillcolor(0,0,0)
  r.begin_fill()
  r.pendown()
  r.circle(10)
  r.end_fill()
  r.right(90)
  r.forward(5)
  r.right(90)
  r.forward(10)
  r.right(180)
  r.forward(25)
  r.right(180)
  r.forward(15)
  r.left(90)
  r.forward(20)
  r.right(60)
  r.forward(15)
  r.right(180)
  r.forward(15)
  r.right(60)
  r.forward(15)

def drawBoat():
  #by Shayan Manoharan
  r.penup()
  r.goto(randint(-450,450),randint(-400,400))
  r.setheading(0)
  r.fillcolor("black")
  r.begin_fill()
  r.pendown()
  r.forward(100)
  r.right(90)
  for i in range(180):
    r.forward(.85)
    r.right(1)
  r.end_fill()
  r.right(90)
  r.forward(45)
  r.left(90)
  r.forward(70)
  r.right(90)
  r.begin_fill()
  r.fillcolor("blue")
  for i in range(120):
    r.right(1)
    r.forward(.6)
  r.right(65)
  r.forward(30)
  r.end_fill()

def drawKite():
  #by Shayan Manoharan
  r.penup()
  r.goto(randint(-450,450),randint(-400,400))
  r.fillcolor(randint(0,255),randint(0,255),randint(0,255))
  r.begin_fill()
  r.pendown()
  r.setheading(135)
  for i in range(4):
    r.forward(30)
    r.right(90)
  r.setheading(240)
  r.end_fill()
  for i in range(2):
    r.forward(10)
    r.left(90)
    r.forward(10)
    r.right(90)

def drawBalloon():
  #by Shayan Manoharan
  r.penup()
  r.goto(randint(-450,450),randint(-400,400))
  r.fillcolor(randint(0,255),randint(0,255),randint(0,255))
  r.begin_fill()
  r.pendown()
  r.setheading(180)
  for i in range(360):
    r.forward(2)
    r.right(5)
  r.setheading(270)
  r.end_fill()
  r.forward(50)

def drawCloud():
  #by Shayan Manoharan
  r.penup()
  r.goto(randint(-450,450),randint(-400,400))
  r.fillcolor(255,255,255)
  r.begin_fill()
  r.pendown()
  r.setheading(180)
  r.forward(180)
  for i in range(4):
    r.setheading(90)
    for i in range(310):
      r.right(.5)
      r.forward(.2)
  r.setheading(270)
  r.forward(40)
  r.end_fill()
  r.penup()

def drawSubmarine():
    #by Brandon Mikesell
    r.setheading(200)
    r.goto(randint(-450,450),randint(-400,400))
    r.fillcolor("yellow")
    r.begin_fill()
    for i in range(180):
        r.right(.2)
        r.forward(.7)
    r.setheading(158)
    for i in range(120):
        r.right(1.2)
        r.forward(.5)
    for i in range(205):
        r.right(.2)
        r.forward(.7)
    r.end_fill()
    r.setheading(270)
    r.forward(13)
    r.setheading(226)
    for i in range(60):
        r.right(.5)
        r.forward(.4)
    for i in range(60):
        r.right(-.5)
        r.forward(-.4)
    r.setheading(270)
    r.forward(20)
    r.setheading(180)
    r.fillcolor(200,0,200)
    r.begin_fill()
    for i in range(23):
        r.right(1.5)
        r.forward(1)
    r.end_fill()
    for i in range(23):
        r.right(-1.5)
        r.forward(-1)
    r.setheading(90)
    r.forward(50)
    r.setheading(180)
    r.fillcolor(200,0,200)
    r.begin_fill()
    for i in range(23):
        r.left(1.5)
        r.forward(1)
    for i in range(2):
        r.left(1.5)
        r.forward(1)
    r.end_fill()
    for i in range(24):
        r.left(-1.5)
        r.forward(-1)
    r.setheading(270)
    r.forward(20)
    r.setheading(0)
    r.forward(5)
    r.setheading(270)
    r.forward(2.5)
    r.setheading(90)
    r.fillcolor(200,200,200)
    r.begin_fill()
    for i in range(280):
        r.right(1.5)
        r.forward(.1)
    r.setheading(90)
    for i in range(15):
        r.right(1.2)
        r.forward(1)
    r.setheading(285)
    for i in range(15):
        r.right(1.1)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.forward(7)
    r.pendown()
    r.fillcolor(200,200,200)
    r.begin_fill()
    for i in range(15):
        r.right(1.2)
        r.forward(1)
    r.setheading(105)
    for i in range(15):
        r.right(1.1)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.forward(2)
    r.setheading(180)
    r.forward(1)
    r.pendown()
    r.setheading(180)
    r.forward(6)
    r.penup()
    r.forward(30)
    r.setheading(270)
    r.forward(1)
    r.pendown()
    r.fillcolor("white")
    r.begin_fill()
    for i in range(360):
        r.right(1)
        r.forward(.1)
    r.end_fill()
    r.penup()
    r.setheading(0)
    r.forward(3)
    r.pendown()
    r.setheading(270)
    for i in range(360):
        r.right(1)
        r.forward(.15)
    for i in range(2):
        r.penup()
        r.setheading(180)
        r.forward(40)
        r.pendown()
        r.setheading(270)
        r.fillcolor("white")
        r.begin_fill()
        for i in range(360):
            r.right(1)
            r.forward(.1)
        r.end_fill()
        r.penup()
        r.setheading(0)
        r.forward(3)
        r.pendown()
        r.setheading(270)
        for i in range(360):
            r.right(1)
            r.forward(.15)
    r.penup()
    r.setheading(0)
    r.forward(2)
    r.setheading(90)
    r.forward(30)
    r.pendown()
    r.fillcolor(0,150,250)
    r.begin_fill()
    r.setheading(80)
    r.forward(10)
    r.setheading(356)
    r.forward(40)
    r.setheading(280)
    r.forward(10)
    r.end_fill()
    r.forward(-10)
    r.fillcolor(0,150,250)
    r.begin_fill()
    r.setheading(356)
    r.forward(5)
    r.setheading(85)
    r.forward(5)
    r.setheading(175)
    r.forward(15)
    r.setheading(85)
    r.forward(8)
    r.setheading(350)
    r.forward(4)
    r.setheading(85)
    r.forward(4)
    r.setheading(175)
    r.forward(8)
    r.setheading(260)
    r.forward(4)
    r.setheading(356)
    r.forward(2)
    r.setheading(260)
    r.forward(8)
    r.setheading(175)
    r.forward(10)
    r.setheading(85)
    r.forward(12)
    for i in range(10):
        r.left(10)
        r.forward(1)
    r.setheading(260)
    r.forward(5)
    r.setheading(356)
    for i in range(4):
        r.right(.3)
        r.forward(1)
    r.setheading(269)
    r.forward(12)
    r.setheading(175)
    r.forward(18)
    r.setheading(269)
    r.forward(6)
    r.setheading(356)
    r.forward(4)
    r.end_fill()
    r.penup()
    r.setheading(180)
    r.forward(50)
    r.setheading(270)
    r.forward(22)
    r.pendown()
    r.setheading(287)
    r.fillcolor(0,150,250)
    r.begin_fill()
    for i in range(18):
        r.right(2)
        r.forward(2)
    r.end_fill()


def drawStar():
  #by Shayan Manoharan
  r.penup()
  r.goto(randint(-450,450),randint(-400,400))
  r.fillcolor(0,0,0)
  r.begin_fill()
  r.pendown()
  r.setheading(0)
  for i in range(5):
    r.forward(30)
    r.left(360/5)
    r.forward(30)
    r.right(720/5)
  r.end_fill()
def drawSunWithRays():
    #By rishil patel
    drawCircle(450,400,100,randomYellow())
    r.right(90)
    drawOneRay()
    r.penup()
    for i in range(3):
        for i in range(90):
            r.forward(2*math.pi*(100/360))
            r.right(1)
        r.left(90)
        r.pendown()
        drawOneRay()
        r.penup()
def drawOneRay():
    #By rishil patel
    r.begin_fill()
    r.fillcolor(randomYellow())
    r.forward(50)
    r.left(90)
    r.forward(10)
    r.left(90)
    r.forward(50)
    r.left(90)
    r.forward(10)
    r.end_fill()
def drawWindTurbine():
	#by Brandon Mikesell
    r.goto(randint(-450,450),randint(-400,400))
    r.setheading(0)
    r.fillcolor(150,150,126)
    r.begin_fill()
    for i in range(27):
        r.left(2.5)
        r.forward(1)
    r.setheading(140)
    for i in range(24):
        r.left(2.5)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.setheading(180)
    r.forward(5)
    r.setheading(270)
    r.forward(1)
    r.setheading(0)
    r.pendown()
    r.fillcolor(180,180,180)
    r.begin_fill()
    for i in range(360):
        r.right(1)
        r.forward(0.15)
    r.end_fill()
    r.setheading(80)
    r.fillcolor(200,100,100)
    r.begin_fill()
    for i in range(75):
        r.right(0.25)
        r.forward(1)
    r.setheading(270)
    for i in range(77):
        r.right(0.4)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.setheading(270)
    r.forward(14)
    r.setheading(0)
    r.forward(1)
    r.pendown()
    r.setheading(310)
    r.fillcolor(200,100,100)
    r.begin_fill()
    for i in range(75):
        r.right(0.4)
        r.forward(1)
    r.setheading(135)
    for i in range(78):
        r.right(0.4)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.setheading(180)
    r.forward(7.5)
    r.setheading(90)
    r.forward(10)
    r.pendown()
    r.setheading(180)
    r.fillcolor(200,100,100)
    r.begin_fill()
    for i in range(55):
        r.left(0.4)
        r.forward(1)
    r.setheading(354)
    for i in range(55):
        r.left(0.4)
        r.forward(1)
    r.end_fill()
    r.penup()
    r.setheading(0)
    r.forward(14)
    r.setheading(270)
    r.forward(26)
    r.pendown()
    r.fillcolor(150,120,0)
    r.begin_fill()
    r.forward(80)
    r.setheading(340)
    r.forward(6)
    r.setheading(90)
    r.forward(70)
    r.end_fill()
    r.penup()
    r.forward(26.5)
    r.pendown()
    r.fillcolor(180,180,180)
    r.begin_fill()
    r.forward(8)
    r.end_fill()
    r.penup()
    r.forward(-104.5)
    r.pendown()
    r.fillcolor(150,120,0)
    r.begin_fill()
    r.setheading(40)
    r.forward(8)
    r.setheading(90)
    r.forward(56)
    r.setheading(120)
    r.forward(10)
    r.end_fill()
    r.forward(-10)
    r.penup()
    r.setheading(90)
    r.forward(25)
    r.pendown()
    r.fillcolor(150,120,0)
    r.begin_fill()
    r.forward(21)
    r.setheading(200)
    r.forward(12)
    r.end_fill()
    r.forward(-6)
    r.setheading(270)
    r.forward(13)

def tester():
    #By rishil patel
    xcoordinate = r.xcor()
    ycoordinate = r.ycor()
    createWaves()
    colors = [randomRed(),randomGreen(),randomBlue(),randomYellow(),randomOrange(),randomPurple()]
    drawCircle(randint(-450,450),randint(-400,400),50,choice(colors))
    drawAllSeaweed()
    drawOneFish()
    drawBird()
    drawStickPerson()
    drawBoat()
    drawKite()
    drawBalloon()
    drawCloud()
    drawSubmarine()
    drawStar()
    drawSunWithRays()
    drawWindTurbine()
def randomWhite():
    #By Shayan Manoharan
    White = (randint(250,255))
    return White
def randomBlack():
    #By Shayan Manoharan
    Black = (randint(0,5))
    return Black
def randomTan():
    #By Shayan Manoharan
    Tan = (randint(205,210), randint(175,180),randint(135,140))
    return Tan
def randomBrown():
    #By Shayan Manoharan
    Brown = (randint(135,140), randint(65,70),randint(15,20))
    return Brown
def randomPink():
    #By Shayan Manoharan
    Pink = (randint(250,255), randint(190,195),randint(200,205))
    return Pink

def drawBuilding():
    #by Brandon
    r.fillcolor(126,126,126)
    r.begin_fill()
    r.setheading(0)
    r.forward(80)
    r.setheading(90)
    r.forward(240)
    r.setheading(180)
    r.forward(80)
    r.setheading(270)
    r.forward(240)
    r.end_fill()
    r.penup()
    r.setheading(0)
    r.forward(10)
    r.setheading(90)
    r.forward(230)
    for i in range(9):
        r.fillcolor("yellow")
        r.pendown()
        r.begin_fill()
        r.setheading(270)
        r.forward(15)
        r.setheading(0)
        r.forward(10)
        r.setheading(90)
        r.forward(15)
        r.setheading(180)
        r.forward(10)
        r.end_fill()
        r.penup()
        r.setheading(270)
        r.forward(25)
    r.penup()
    r.setheading(0)
    r.forward(25)
    r.setheading(90)
    r.forward(225)
    for i in range(8):
        r.fillcolor("yellow")
        r.pendown()
        r.begin_fill()
        r.setheading(270)
        r.forward(15)
        r.setheading(0)
        r.forward(10)
        r.setheading(90)
        r.forward(15)
        r.setheading(180)
        r.forward(10)
        r.end_fill()
        r.penup()
        r.setheading(270)
        r.forward(25)
    r.penup()
    r.setheading(0)
    r.forward(25)
    r.setheading(90)
    r.forward(200)
    for i in range(9):
        r.fillcolor("yellow")
        r.pendown()
        r.begin_fill()
        r.setheading(270)
        r.forward(15)
        r.setheading(0)
        r.forward(10)
        r.setheading(90)
        r.forward(15)
        r.setheading(180)
        r.forward(10)
        r.end_fill()
        r.penup()
        r.setheading(270)
        r.forward(25)
    r.penup()
    r.setheading(180)
    r.forward(27)
    r.setheading(270)
    r.forward(5)
    r.fillcolor(90,60,30)
    r.pendown()
    r.begin_fill()
    r.forward(-20)
    r.setheading(0)
    r.forward(15)
    r.setheading(270)
    r.forward(20)
    r.end_fill()
def randomLightRed():
    #By Shayan Manoharan
    LightRed = (randint(0,127),0,0)
    return LightRed
def randomDarkRed():
    #By Shayan Manoharan
    DarkRed = (randint(127,255),0,0)
    return DarkRed
def randomLightBlue():
    #By Shayan Manoharan
    LightBlue = (0,(randint(0,127),0)
    return LightBlue
def randomDarkBlue():
    #By Shayan Manoharan
    DarkBlue = (0,(randint(127,255),0)
    return DarkBlue
def randomLightGreen():
    #By Shayan Manoharan
    LightGreen = (0,0,(randint(0,127))
    return LightGreen
def randomDarkGreen():
    #By Shayan Manoharan
    DarkGreen = (0,0,randint(127,255))
    return DarkGreen
def isValidNumber(myNumber):
    #By rishil patel
    myNumber = int(myNumber)
    if myNumber == 1 or myNumber == 2 or myNumber == 3:
        return True
    else:
        return False
def countryScene():
    #By rishil patel
    drawLand()
    drawBird()
    drawSunWithRays()
    drawStickPerson()
def mainFunction():
    #By rishil patel
    print("Which scene would you like? Type either 1 for city, 2 for country, or 3 for underwater")
    userInput = input()
    userInput = int(userInput)
    isValidNumber(userInput)
    if userInput == 1:
        cityScene()
    if userInput == 2:
        countryScene()
    if userInput == 3:
        underwaterScene()
    if isValidNumber(userInput) == False:
        print("Not a valid number 1-3")
from turtle import *
tracer(0)
r = Turtle()
def drawRoad():
  r.penup()
  r.goto(100,0)
  r.fillcolor(100,100,100)
  r.pendown()
  r.begin_fill()
  r.left(90)
  r.forward(500)
  r.right(90)
  r.forward(100)
  r.right(90)
  r.forward(500)
  r.right(90)
  r.forward(100)
  r.right(180)
  r.forward(35)
  r.left(90)
  r.end_fill()


def drawPavementMarker():
  r.fillcolor(225,150,100)
  r.penup()
  r.forward(55)
  r.right(90)
  r.begin_fill()
  r.pendown()
  r.forward(30)
  r.left(90)
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.left(90)
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.left(90)
  r.end_fill()
  r.penup()
  r.forward(150)
  r.pendown()
  r.begin_fill()
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.left(90)
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.end_fill()
  r.left(90)
  r.penup()
  r.forward(150)
  r.pendown()
  r.begin_fill()
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.left(90)
  r.forward(100)
  r.left(90)
  r.forward(30)
  r.end_fill()

drawRoad()
drawPavementMarker()
#made by Sanjeev

mainFunction()





update()
