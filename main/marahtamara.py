import turtle
import time
SLEEP=0.00000007
turtle.setup(700,700)
turtle.ht()

from turtle import *
screen = Screen()
turtle.penup()

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

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


def check_click():
    print(xclick, " ", yclick)
    if xclick >= -75 and xclick <= 75 and yclick > 0 and yclick <= 35:
        turtle.clear()
        screen.bgcolor("light blue")
        turtle.shape("ma8ah.gif")
        goto(-300,screenMaxY-50)
        turtle.stamp()

        
    #elif xclick>= -75 and xclick<= 75 and yclick>-46 and yclick<= -22:
       # print("score is on")
        #turtle.ht()
        #goto(-200,screenMaxY-50)
        #write("How to play", align="center",font=("Ariel",20))


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

        # turtle.onscreenclick(variables)
        # time.sleep(SLEEP)



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
        # turtle.ht()  

    # turtle.ontimer(check_click, 100)



    
# check_click()







mainloop()












    #turtle.register_shape("nina.gif")
    #turtle.shape("nina.gif")
    #turtle.goto(-200, -200)
    #turtle.stamp()
    #turtle.register_shape("nina.gif")
    #turtle.shape("nina.gif")
    #turtle.goto(200,-200)
    #turtle.stamp()
