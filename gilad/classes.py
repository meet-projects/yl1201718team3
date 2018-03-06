from turtle import *
import random

class BALL(Turtle):
	def __init__(self,xpos,ypos,dx,dy,radius):
		Turtle.__init__(self)
		self.pu()
		self.goto(xpos,ypos)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.shape("circle")
		self.shapesize(radius/10)

	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx
		new_y = current_y + self.dy

		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		up_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius

		self.goto(new_x,new_y)
		if right_side_ball>=screen_width or left_side_ball<=-screen_width:
			self.dx = -self.dx
		if bottom_side_ball<=-screen_height or up_side_ball>=screen_height:
			self.dy = -self.dy


class BLOCK(Turtle):
	def __init__(self,x,y,number):
		Turtle.__init__(self)
		self.shape("square")
		self.pu()
		self.x=x
		self.y=y
		self.goto(x,y)
		self.dy=15
		self.height=2
		self.shapesize(4)
		
	def move(self):
		current_x=self.xcor()
		current_y=self.ycor()
		new_y=current_y-self.dy
		new_x=current_x
		
		buttom_side_ball=new_y-self.height
		
		self.goto(new_x,new_y)
		if buttom_side_ball<-400:
			self.goto(-400,-350)
			self.goto(-400,400)
			self.goto(0,400)

a=BLOCK(0,0,5)
a.move()
mainloop()