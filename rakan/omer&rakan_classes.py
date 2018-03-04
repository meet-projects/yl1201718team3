from turtle import *
import turtle
import time
import random
# colormode(255)
hideturtle()
tracer(0)


# is every thing good tell me (rakan) 28/2/2018


FIXED_RADUIS = 1
FIXED_COLOR="Blue"
game = True
screen_width = 200
screen_height = 0
right_border = -100
left_border = 100
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

	# def add_tail(x,y):
	# 	# if food=True
	# 	newtail = tail_circle(FIXED_COLOR,FIXED_RADUIS)
	# 	newtail.goto(x, y-self.radius)
	# 	self.tails.append(newtail)

	def move_head(self,x,y):
		xpos = self.xcor()
		self.goto(x,0)
		if xpos+self.radius > left_border or xpos-self.radius < right_border:
			print("BORDER ALERT")
			
			new_xpos = self.xcor()
			self.goto(new_xpos,0)
		for i in range(len(self.tails)):
			if i > 0:
				self.tails[i].move_tail(((self.tails[0]).xcor()),((self.tails[0]).ycor())-10)
			if i < 1.01 : 
				self.tails[1].move_tail(MY_HEAD.xcor(), MY_HEAD.ycor())
			

	# def tail_foolow(self):
	# 	for i in range(len(tails)):
	# 		i.move_tail()
	# 		print(i)

	
MY_HEAD = head_circle( "Red", 0 , 50 , FIXED_RADUIS)

# head_circle = Ball 
# tt = head_circle(FIXED_COLOR,0,0,FIXED_RADUIS)


class tail_circle(head_circle):
	def __init__ (self,color,radius,x,y):
		head_circle.__init__(self,color,x,y,radius)
		self.color = color
		self.fillcolor(color)
		self.shape("circle")
		self.shapesize(radius)
		self.pu()
		self.goto(x,y)
		self.tails = []
		# self.tail_foolow()

	def maketail():
		pass

	def move_tail(self,x,y):
		xpos = self.xcor()
		ypos = self.ycor()
		half_x = (x-xpos)/2
		self.goto( half_x ,y-self.radius*10)
		if half_x+self.radius > left_border or half_x-self.radius < right_border:
			print("BORDER ALERT")
			# self.goto(xpos,ypos)
			print(half_x)

	def tail_foolow(self):
		self.tails[0].move_tail(MY_HEAD.xcor(), MY_HEAD.ycor())
		for i in range(len(self.tails)-1):
			if i > 1:
				self.tails[i].move_tail(((self.tails[0]).xcor()),((self.tails[0]).ycor())-10)
			# if i < 1.01 : 
			# 	self.tails[1].move_tail(MY_HEAD.xcor(), MY_HEAD.ycor())
		# print("hellow")

	def add_tail(self,x,y):
		# if food=True
		newtail = tail_circle(FIXED_COLOR,FIXED_RADUIS,x,y)
		newtail.goto(x, y-self.radius*10)
		self.tails.append(newtail)
		print(self.tails[0])
		print(len(self.tails))
		print(self.tails)

MY_TAIL = tail_circle(FIXED_COLOR,FIXED_RADUIS,0,FIXED_RADUIS-20)
# MY_TAIL.tail_foolow()
MY_TAIL.add_tail(0,-FIXED_RADUIS*2-30)

MY_TAIL.add_tail(0,-FIXED_RADUIS*3-10)
# MY_TAIL.add_tail(0,-)

# print(tails[])

def movearound(event):

	X1 = (event.x - screen_width - 75)
	Y1 = screen_height - event.y
	# if MY_HEAD.xcor()+MY_HEAD.radius > left_border:
	# 	MY_HEAD.goto(left_border-MY_HEAD.radius,0)
	# elif MY_HEAD.xcor()-MY_HEAD.radius < right_border:
	# 	MY_HEAD.goto(right_border+MY_HEAD.radius,0)	
	# else:
	MY_HEAD.move_head(X1,Y1)




def movearound(event):

	X1 = (event.x - screen_width - 75)
	Y1 = screen_height - event.y
	if MY_HEAD.xcor()+MY_HEAD.radius > left_border:
		MY_HEAD.goto(left_border-MY_HEAD.radius,0)
	elif MY_HEAD.xcor()-MY_HEAD.radius < right_border:
		MY_HEAD.goto(right_border+MY_HEAD.radius,0)	
	else:
		MY_HEAD.move_head(X1,Y1)

		# if right_side_ball > 199:
		# 	print("r.border")

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



while game == True:
 	# if screen_width != __init (turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
 		# screen_width = __int__ (turtle.getcanvas().winfo_width()/2)
		# screen_height = __int__ (turtle.getcanvas().winfo_height()/2)
	MY_TAIL.tail_foolow()
	# newtail.tail_foolow()
	turtle.getscreen().update()




	




	
turtle.mainloop()