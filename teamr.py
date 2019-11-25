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

    r.penup()
    r.goto(475,200) #top right corner
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
    r.goto(475,200) #go to top right corner
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
    r.forward(((360/math.pi)*4)+60) #goes to the wave's edge
    r.left(90)
    r.forward(800)
    r.left(90)
    r.forward(((360/math.pi)*4)+60) #goes to the wave's edge
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
        r.goto(100,0)
        drawOneSeaweed()
        
def drawOneFish():
    #By rishil patel
    r.penup()
    r.goto(300,0)
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
  r.goto(0,300)
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
  r.goto(-50,230)
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
  r.goto(250,190)
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
  r.goto(-250,350)
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
  r.goto(-150,300)
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
  r.goto(300,300)
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
  r.goto(-225,250)
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


createWaves()
drawLand()
drawAllSeaweed()
drawOneFish()
drawBird()
drawBoat()
drawKite()
drawBalloon()
drawStickPerson()
drawCloud()
drawStar()



update()
