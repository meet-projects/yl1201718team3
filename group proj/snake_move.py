from turtle import *
import random #we'll need this later in the lab.
square_size=20
start_length=5


#intialize lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
color_snake_list=["blue","green","black","yellow","brown","pink","lightblue","purple","gray","orange"]

#set up positions (x,y) of boxes that make up the snake.
snake= clone()
snake.shape("square")

#hide thee turtle object (it's an arrow - we don't need to see it)
hideturtle()

#draw a snake at the start of the game with a for loop.
#for loop should use range() and count up to the number of pieces.
#in the snake (i.e. start_length).
for snake_draw in range(start_length):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    #add square_size to x_pos. where does x_pos point  to now?
    #you're right
    x_pos+=square_size

    my_pos=(x_pos,y_pos) #store position variables in a tuple
    snake.goto(x_pos,y_pos) #move snake to new (x,y)

    #append the new position tuple to pos_list
    pos_list.append(my_pos)
    #save the stamp id! you'll need to erase it later. than append it to stamp_list.
    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)
################################################################################
#make sure you pay attention to upper and lower case.
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100 #update snake position after this many milliseconds

SPACEBAR="space" #careful,it's not supposed to be capitalized

UP=0
LEFT=1
DOWN=2
RIGHT=3

SPACEBAR="Space"

direction=UP

TOP_EDGE=250
BOTTOM_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def left():
    global direction
    direction= LEFT
    print("you pressed the left key!")
def right():
    global direction
    direction= RIGHT
    print("you pressed the right key!")
onkeypress(left,LEFT_ARROW)
onkeypress(right,RIGHT_ARROW)
listen()

def move_snake():
    my_pos=snake.pos()        
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + square_size, y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - square_size, y_pos)
        print("you moved left")
    
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps,food_pos,SCORE
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind]) #remove eaten food        
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!!!!!")
        make_food()

        randomColor = random.choice(color_snake_list)
        snake.color(randomColor)

    else:        
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
#grab position of snake
    new_pos=snake.pos()

    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! game over!!!!!:(")
        
    
    elif new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! game over!!!!!:(")
            
    turtle.ontimer(move_snake,TIME_STEP)
mainloop()