from turtle import *
import turtle
import random
import math
import time

#VARIABLES
me=8
SLEEP=0.00375
me2=1
FOOD_NUM=1
RUNNING=True
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
FOOD_list=[]
xposes=[-400,-300,-200,-100,0,100,200,300,400,500]
class Food(Turtle):
	def __init__ (self,x,y):
		Turtle.__init__(self)
		self.hideturtle()
		self.shape("circle")
		self.pu()
		self.x=x
		self.y=y
		self.goto(x,y)
		self.dy=15
		self.radius=10
		self.shapesize(10/10)
		self.color("red")
		self.showturtle()
	def move(self):
		current_x=self.xcor()
		current_y=self.ycor()
		new_y=current_y-self.dy
		new_x=current_x
		buttom_side_ball=new_y-self.height
		self.goto(new_x,new_y)
def make_food():
	for i in range(FOOD_NUM):
		global me,me2
		x= random.choice(xposes)
		for i in range blo
		#block 6
		if me==-2:
			x1=x
			me=-3
		#block 5
		if me==0:
			x1=x
			me=-1
		#block 4
		if me==2:
			x1=x
			me=1
		#block 3
		if me==4:
			x1=x
			me=3
		#block 2
		if me==6:
			x1=x
			me=5
		#block1
		if me==8:
			x1=x
			me=7
		if me2==0:
			global x1
			while x1==x:
				x= random.choice(xposes)
				me-=1

		y=300
		number=random.randint(1,20)
		block=Food(x,y,number)
		FOOD_list.append(block)
		me2=0

def move_blocks():

	for i in FOOD_list:
		i.move()




while RUNNING==True:
	stop=True
	c=0
	make_blocks()
	while stop==True:
		move_blocks()
		c+=1
		if c==10:
			stop=False
		getscreen().update()
		time.sleep(SLEEP)


mainloop()