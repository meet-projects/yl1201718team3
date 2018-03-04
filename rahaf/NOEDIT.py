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
blocks_num=8
RUNNING=True
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
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
FOOD_list=[]
blockxpos=[-400,-200,-100,100,200,400]

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
		self.speed(0.000000000000000000000000000000001)
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
		self.speed(0.00001)
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


#FUNCTIONS

def make_blocks():
	for i in range(blocks_num):
		global me,me2
		x= random.choice(blockxpos)
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
			y=300
			number=random.randint(1,20)
			i.goto(x,y)



#FOOD
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

def make_food():
	for b in range(FOOD_NUM):
		m=random.randint(0,3)

		if m==0:
			x=0
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
			block1=BLOCK(300,300,2)
			block=BLOCK(-300,300,2)
			block_list.append(block1)
			block_list.append(block)
		if m==1:
			x=300
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
			block=BLOCK(0,300,2)
			block_list.append(block)
			block=BLOCK(-300,300,2)
			block_list.append(block)
		if m==2:
			x=-300
			y=300
			food=Food(x,y)
			FOOD_list.append(food)
			block=BLOCK(0,300,2)
			block_list.append(block)
			block=BLOCK(300,300,2)
			block_list.append(block)
		if m==3:
			block=BLOCK(0,300,2)
			block_list.append(block)
			block=BLOCK(300,300,2)
			block_list.append(block)
			block=BLOCK(-300,300,2)
			block_list.append(block)
			
			

def move_food():

	for i in FOOD_list:
		i.movef()


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
MY_HEAD.add_tail(0,-FIXED_RADUIS*2-30)
MY_HEAD.add_tail(0,-FIXED_RADUIS*3-10)
MY_HEAD.add_tail(0,-FIXED_RADUIS*3-10)

def collisioin():
	for i in BLOCKS:

		d1 = MY_HEAD.shapesize()[0]*10+(i.shapesize()[0])*10
		d2 = math.pow((MY_HEAD.xcor()-i.xcor()),2)+math.pow((MY_HEAD.ycor()-i.ycor()),2)
		if (d1>=math.sqrt(d2)):
			return(True)
		else:
			return(False)
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
		while RUNNING==True:
			stop=True
			c=0
        	
			make_food()
			if len(block_list)<35:
				make_blocks()
			else:
				move_me()
			MY_HEAD.tail_follow()
			turtle.getscreen().update()

			while stop==True:
				move_blocks()
				move_food()
				c+=1
				if c==10:
					stop=False
					update()
					



	elif xclick>=-75  and xclick<=75  and yclick> -92 and yclick <= -73:

		turtle.clear()
		screen.bgcolor("light blue")
		turtle.penup()

        


    
		goto(0, screenMaxY - 100)
		color('black')
		write(" Description about the game:", align="center", font=("Arial",25))
		goto(0, screenMaxY - 150)
		write("you start with 4 balls", align="center", font=("Arial",15))
		goto(0,screenMaxY- 200)
		write("through your path you will have a number  of balls with random numbers", align="center", font=("Arial",15))
		goto(0,screenMaxY-250)
		write("your goal must be eating as much balls as you can.", align="center", font=("Arial",15))
		goto(0,screenMaxY-300)
		write("However; the trick is to eat the ball with highest number in order to get your snake as tall as you can", align="center", font=("Arial",15))
		goto(0,screenMaxY-350)
		write("your next mission is to pass through a block of squares that have random numbers ", align="center", font=("Arial",15))
		goto(0,screenMaxY-400)
		write("you must target the block with the lowest number because in this game the blocks are your enemy ,due to their roll which is against your will to keep your snake alive ", align="center", font=("Arial",15))
		goto(0,screenMaxY-450)
		write("when you bump into one of the squares ", align="center", font=("Arial",15))
		goto(0,screenMaxY-500)
		write("here, both of you will have a competition ", align="center", font=("Arial",15))
		goto(0,screenMaxY-550)
		write("each one of you will start losing its soliders who are the numbers until one of you run out of its soliders ", align="center", font=("Arial",15))
		goto(0,screenMaxY-600)
		write("if you win you will continue your path but if you lose (GAME OVER) :-0", align="center", font=("Arial",15))
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