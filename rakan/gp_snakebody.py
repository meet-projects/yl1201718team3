from turtle import *
import turtle
import time
import random
colormode(255)
hideturtle()
tracer(0)


# is every thing good tell me (rakan) 28/2/2018


FIXED_RADUIS = 1
FIXED_COLOR="Blue"
game = True
screen_width = 200
screen_height = 0
class head_circle(Turtle):
	def __init__ (self,color,x,y,radius):
		Turtle.__init__(self)
		self.pu()
		self.color = color
		self.x = x
		self.y = y
		self.radius= radius
		self.shape("circle")
		self.shapesize(radius)
		self.tails=[]

	def add_tail():
		newtail = tail_circle()
		self.tails.append(newtail)

	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		# top_side_ball = new_y + self.r
		# bottom_side_ball = new_y - self.r
		self.goto(new_x,self.y)

		# if top_side_ball > height:
		# 	self.dy = - self.dy

		# elif bottom_side_ball < -height:
		# 	self.dy = -self.dy

		if left_side_ball < -199 or right_side_ball > 199:
			print("l.border")

		if right_side_ball > 199:
			print("r.border")

	
MY_HEAD = head_circle( "Blue", 0 , 0 , FIXED_RADUIS)
# head_circle = Ball 
# tt = head_circle(FIXED_COLOR,0,0,FIXED_RADUIS)


class tail_circle(Turtle):
	def __init__ (self,color,radius):
		self.color = color
		self.shape("circle")
		self.shapesize(radius)

	def maketail():
		pass

	def movearound(event):
		X1 = (event.x - screen_width)
		Y1 = screen_height - event.y
		MY_HEAD.goto(X1,0) 
	# MY_HEAD.goto(-X1,0)
	turtle.getcanvas().bind("<Motion>", movearound)
	turtle.listen()



while game == True:
 	# if screen_width != __init (turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
 		# screen_width = __int__ (turtle.getcanvas().winfo_width()/2)
		# screen_height = __int__ (turtle.getcanvas().winfo_height()/2)
	turtle.getscreen().update()



	
turtle.mainloop()












