from turtle import *
import turtle
import random
import math
import time

#VARIABLES
turtle.colormode(255)
turtle.hideturtle()
turtle.pu()
turtle.goto(0,300)
turtle.tracer(0)
me=8
SLEEP=0.065
me2=1
FOOD_NUM=1
blocks_num=8
RUNNING=True
SCREEN_WIDTH=400
SCREEN_HEIGHT=400

#LISTS
block_list=[]
FOOD_list=[]
<<<<<<< HEAD
xposes=[-300,-200,-100,0,100,200,300,400]
me_x_poses=[-300,-200,-100,0,100,200,300,400]
difference=[]
=======
blockxpos=[-400,-200,-100,100,200,400]
>>>>>>> 4e27dda7208fc8ad84826d3b1f6c3d0333f4b4fe

#CLASS
class BLOCK(Turtle):
	def __init__(self,x,y,number):
		Turtle.__init__(self)
		self.hideturtle()
		self.shape("square")
		self.pu()
		self.x=x
		self.y=y
		self.goto(x,y)
		self.dy=15
		self.height=2
		self.shapesize(4)
		r=random.randint(0,225)
		g=random.randint(0,225)
		b=random.randint(0,225)
		color=(r,g,b)
		self.color(color)
		self.showturtle()
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
	def movef(self):
		current_x=self.xcor()
		current_y=self.ycor()
		new_y=current_y-self.dy
		new_x=current_x
		buttom_side_ball=new_y-self.radius
		self.goto(new_x,new_y)
<<<<<<< HEAD
def make_food():
	for b in range(FOOD_NUM):
		global difference,me_x_poses
		for a in block_list:
			if a.xcor() not in me_x_poses:
				difference.append(a)
		if(len(difference) > 0):
			x= random.choice(difference)
			y=300
			block=Food(x,y)
			FOOD_list.append(block)
def move_food():
=======

def make_food():
	for b in range(FOOD_NUM):
		m=random.randint(0,3)

		if m==0:
			x=0
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
		if m==1:
			x=300
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
		if m==2:
			x=-300
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
		if m==3:
			pass

def move_food():

	for i in FOOD_list:
		i.movef()
>>>>>>> 4e27dda7208fc8ad84826d3b1f6c3d0333f4b4fe

	for i in FOOD_list:
		i.movef()


#FUNCTIONS

#FUNCTIONS

def make_blocks():
	for i in range(blocks_num):
		global me,me2
		x= random.choice(blockxpos)
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
				x= random.choice(blockxpos)
				me-=1

		y=300
		number=random.randint(1,20)
		block=BLOCK(x,y,number)
		block_list.append(block)
		me2=0

def move_blocks():
	for i in block_list:
		i.move()
		
def move_me():
	for i in block_list:
		current_x=i.xcor()
		current_y=i.ycor()
		new_y=current_y-i.dy
		new_x=current_x
		buttom_side_ball=new_y-i.height
		if buttom_side_ball > 300:
			global me,me2
			x= random.choice(blockxpos)
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
					x= random.choice(blockxpos)
					me-=1

			y=300
			number=random.randint(1,20)
			i.goto(x,y)


while RUNNING==True:
	stop=True
	c=0
	if len(block_list)<35:
		make_blocks()
	else:
		move_me()
	make_food()
	while stop==True:
		move_blocks()
		move_food()
		c+=1
		if c==10:
			stop=False
		update()
		time.sleep(SLEEP)


mainloop()