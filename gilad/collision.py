import math
from turtle import *
from ballagario import Ball
from ballagario import Square

SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)

def collisioin(ball,square):
	d1 = ball.shapesize()[0]*10+(square.shapesize()[0])*10
	d2 = math.pow((ball.xcor()-square.xcor()),2)+math.pow((ball.ycor()-square.ycor()),2)
	if (d1>=math.sqrt(d2)):
		return(True)
	else:
		return(False)

ball = Ball(0,-100,3,3,50)
ball.color("Red")
square = Square(0,0,1,1)

def movearound(event):  
	ball.xpos = event.x - SCREEN_WIDTH
	ball.ypos = SCREEN_HEIGHT - event.y
	ball.goto(ball.xpos,ball.ypos)

d = clone()
d.pu()
d.goto(-200,-200)
while True:
	ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	a=collisioin(ball,square)
	if a==True:
		d.write ("collisoin")
	else:
		d.clear()
mainloop()