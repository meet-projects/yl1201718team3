from turtle import *
import random
import math

tracer(1)
hideturtle()
colormode(255)

class SNAKE(Turtle):
	def __init__(self,xpos,ypos,dx,dy,radius):
		Turtle.__init__(self)

class BLOCKS(Turtle):
	def __init__(self,xpos,ypos):
		Turtle.__init__(self)
		self.shape("square")
		self.pu()
		self.goto(xpos,ypos)
		self.dy = 15
		self.height = 2
		self.shapesize(4)
		r = random.randint(0,225)
		g = random.randint(0,225)
		b = random.randint(0,225)
		color = (r,g,b)
		self.color(color)

	def move(self):
		current_y = self.ycor()
		new_y = current_y-self.dy

		buttom_side_ball = new_y-self.height/2

		self.goto(self,xcor(),new_y)
		if buttom_side_ball < -4000:
			self.goto(-400,-350)
			self.goto(-400,400)
			self.goto(0,400)

mainloop()