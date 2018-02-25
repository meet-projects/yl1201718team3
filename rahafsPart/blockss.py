from turtle import *
import turtle
import random
import math
import time
turtle.colormode(255)
turtle.hideturtle()
turtle.pu()
turtle.goto(0,300)
turtle.tracer(0)
me=8
SLEEP=0.0065
me2=1
blocks_num=6
RUNNING=True
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
block_list=[]
xposes=[-400,-300,-200,-100,0,100,200,300,400,500]
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
def make_blocks():
	for i in range(blocks_num):
		global me,me2
		x= random.choice(xposes)
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
		block=BLOCK(x,y,number)
		block_list.append(block)
		me2=0

def move_blocks():

	for i in block_list:
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