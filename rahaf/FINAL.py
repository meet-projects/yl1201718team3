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
turtle.setup(700,700)
me=8
SLEEP1=0.5
me2=1
FOOD_NUM=1
timer=500
blocks_num=1
RUNNING=True
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
b=0
screen = Screen()
turtle.penup()

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2
FIXED_RADUIS = 1
FIXED_COLOR="Blue"
game = True
screen_width = 200
screen_height = 0
right_border = -100
left_border = 100


#LISTS
block_list=[]
#FOOD_list=[]
blockxpos=[-300,-200,-100,100,200,400]

#appearence

screen.bgcolor("lightblue")
goto(0, screenMaxY - 200)
color('black')
write("Snack Rush!!", align="center", font=("Arial",50))
goto(0, screenMaxY - 215)
write("CoOl GaMe WiTh CoOl FeAtUrEs...YoU hAvE tO pLaY iT!", align="center")
turtle.showturtle()
goto(0,screenMaxY- 350)
write("Play game",align="center",font=("Ariel",20))
goto(0,screenMaxY-450)
write("How to play", align="center",font=("Ariel",20))

turtle.ht()
xclick=0
yclick = 0

def variables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print((xclick, yclick))
    check_click()

turtle.register_shape("ma8ah.gif")

turtle.onscreenclick(variables)




#BLOCKS
class BLOCK(Turtle):
	def __init__(self,x,y,number):
		Turtle.__init__(self)
		self.hideturtle()
		self.shape("square")
		self.pu()
		self.x=x
		self.y=y
		self.goto(x,y)
		self.dy=7
		self.height=1.8
		self.shapesize(1.8*2)
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


#FUNCTIONS

def make_blocks():
	for i in range(blocks_num):
		global me,me2
		x= random.choice(blockxpos)
		y=300
		block=BLOCK(x,y,9)
		block_list.append(block)

def move_blocks():
	for i in block_list:
		i.move()
		
def move_me():
	for i in block_list:
		current_x=i.xcor()
		current_y=i.ycor()
		new_y=current_y-(i.dy)
		new_x=current_x
		buttom_side_ball=new_y-i.height
		if buttom_side_ball > 300:
			global me,me2
			x= random.choice(blockxpos)
			y=300
			number=random.randint(1,20)
			i.goto(x,y)



#FOOD


class head_circle(Turtle):
	def __init__ (self,color,x,y,radius):
		Turtle.__init__(self)
		self.pu()
		self.color = color
		self.fillcolor(self.color)
		self.x = x
		self.y = y
		self.radius= radius
		self.shape("circle")
		self.shapesize(radius)
		self.goto(x,0)
		self.tails = []

	def add_tail(self,x,y):
		# if food=True
		newtail = tail_circle(FIXED_COLOR,FIXED_RADUIS,x,y)
		newtail.goto(x, y-self.radius*10)
		self.tails.append(newtail)
		print(self.tails[0])
		print(len(self.tails))
		print(self.tails)

	def move_head(self,x,y):
		xpos = self.xcor()
		self.goto(x,0)

	def tail_follow(self):
		moved = True
		# while moved:
		# 	print(moved)
		for i in range(len(self.tails)):
			if i > 0:
				moved = self.tails[i].move_tail(((self.tails[i-1]).xcor()),((self.tails[i-1]).ycor())-10)
			else:
				moved = self.tails[0].move_tail(self.xcor(), self.ycor())

class tail_circle(Turtle):
	def __init__ (self,color,radius,x,y):
		head_circle.__init__(self,color,x,y,radius)
		self.color = color
		self.fillcolor(color)
		self.shape("circle")
		self.shapesize(radius)
		self.pu()
		self.goto(x,y)
		# self.tails = []
		# self.tail_foolow()

	def maketail():
		pass

	def move_tail(self,x,y):
		moved = False
		xpos = self.xcor()
		ypos = self.ycor()
		half_x = (x-xpos)/3.0
		if half_x == 0:
			half_x = 1
		self.goto(half_x+xpos ,y-self.radius*10)
			# moved = True
		return moved

MY_HEAD = head_circle( "Red", 0 , -300 , FIXED_RADUIS)

def collisioin():
	for i in block_list:

		rec_top=i.ycor()+((i.shapesize()[0]/2)*20)
		rec_right=i.xcor()+((i.shapesize()[0]/2)*20)
		rec_bottom=i.ycor()-((i.shapesize()[0]/2)*20)
		rec_left=i.xcor()-((i.shapesize()[0]/2)*20)

		ball_top=MY_HEAD.ycor()+(MY_HEAD.shapesize()[0]/2)*20
		ball_right=MY_HEAD.xcor()+(MY_HEAD.shapesize()[0]/2)*20
		ball_bottom=MY_HEAD.ycor()-(MY_HEAD.shapesize()[0]/2)*20
		ball_left=MY_HEAD.xcor()-(MY_HEAD.shapesize()[0]/2)*20
		if (ball_top>= rec_bottom and ball_right>= rec_left and ball_bottom<= rec_top and ball_left<= rec_right):
			print("collision")
			i.ht()
			block_list.remove(i)
			return(True)
		else:
			print("no")
			return(False)
def printTime():
    #timer function:
    global timer
    turtle.clear()
    turtle.write(timer,font=("Courier",20,"normal"))
    timer=timer-1
def movearound(event):

	X1 = (event.x - screen_width - 75)
	Y1 = screen_height - event.y
	MY_HEAD.move_head(X1,Y1)


turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
def check_click():
	print(xclick, " ", yclick)
	if xclick >= -75 and xclick <= 75 and yclick > 0 and yclick <= 35:
		turtle.clear()
		screen.bgcolor("light blue")
		turtle.shape("ma8ah.gif")
		goto(-300,screenMaxY-50)
		turtle.stamp()
		RUNNING=True
		
		while RUNNING==True and timer>-1:
			global b
			stop=True
			c=0
			printTime()
			if len(block_list)<1:
				make_blocks()
				if c==0:
					b=b+1
					

					MY_HEAD.add_tail(0,-FIXED_RADUIS*2-30)
					#MY_HEAD.add_tail(0,-FIXED_RADUIS*3-10)
					#MY_HEAD.add_tail(0,-FIXED_RADUIS*3-10)
					c=10
			else:
				move_me()
			#while stop==True:
			while c<10:
				MY_HEAD.tail_follow()
				c+=2
				if c==2 or c==4 or c==6 or c==8:
					move_blocks()
				d= collisioin()
				if d==True:
					pass

				getscreen().update()
					#RUNNING=False
		if RUNNING==False or timer==-1:
			global b 
			turtle.clear()
			turtle.write("Time is up, you earned "+str(b)+" points!",align="Center",font=("Courier", 20,"bold"))

	elif xclick>=-75  and xclick<=75  and yclick> -92 and yclick <= -73:

		turtle.clear()
		screen.bgcolor("light blue")
		turtle.penup()

        


    
		goto(0, screenMaxY - 100)
		color('black')
		write(" Description about the game:", align="center", font=("Arial",25))
		goto(0, screenMaxY - 150)
		write("you start with 2 balls", align="center", font=("Arial",15))
		goto(0,screenMaxY- 200)
		write("through your path you will see blocks falling ", align="center", font=("Arial",15))
		goto(0,screenMaxY-250)
		write("your goal must be eating as much blocks as you can.", align="center", font=("Arial",15))
		goto(0,screenMaxY-300)
		write("when you bump into one of the squares ", align="center", font=("Arial",15))
		goto(0,screenMaxY-350)
		write("here, the block is eaten and another one falls ", align="center", font=("Arial",15))
		goto(0,screenMaxY-400)
		write("Play with your friends and try to see who gets the highest score and challenge them!!! BB :-0", align="center", font=("Arial",15))
		print("how to play is on")


		# turtle.register_shape("ma8ah.gif")
		turtle.shape("ma8ah.gif")
		goto(-300,screenMaxY-50)
		turtle.stamp()

	elif xclick>= -324 and xclick<= -272 and yclick>276 and yclick<= 328:

		turtle.clear()
		turtle.ht()
		screen.bgcolor("lightblue")
		goto(0, screenMaxY - 200)
		color('black')
		write("Snack Rush!!", align="center", font=("Arial",50))
		goto(0, screenMaxY - 215)
		write("CoOl GaMe WiTh CoOl FeAtUrEs...YoU hAvE tO pLaY iT!", align="center")
		# turtle.showturtle()
		goto(0,screenMaxY- 350)
		write("Play game",align="center",font=("Ariel",20))
		goto(0,screenMaxY-450)
		write("How to play", align="center",font=("Ariel",20))  






mainloop()