from turtle import *
import turtle
import random
import math
import time
turtle.colormode(255)

blocks_num=5
block_list=[]
xposes=[-90,-50,-10,30,50,90]
class BLOCK(Turtle):
	def __init__(self,x,y,number):
		Turtle.__init__(self)
		self.shape("square")
		self.pu()
		self.x=x
		self.y=y
		self.dy=5
		self.height=2
		self.shapesize(2)
		r=random.randint(0,225)
		g=random.randint(0,225)
		b=random.randint(0,225)
		color=(r,g,b)
		self.color(color)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		current_y=self.ycor()
		new_y=current_y-self.dy
		new_x=current_x
		buttom_side_ball=new_y-self.height
		self.goto(new_x,new_y)

for i in range(blocks_num):
	x=random.choice(xposes)
	y=300
	number=random.randint(1,20)
	block=BLOCK(x,y,number)
	block_list.append(block)

def move_blocks():

	for i in block_list:
		i.move(400,400)
while True:
	move_blocks()



mainloop()