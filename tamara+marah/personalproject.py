import turtle
import time
turtle.setup(700,700)


from turtle import *
screen = Screen()
turtle.penup()

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

def mainMenu():
    screen.bgcolor("black")
    goto(0, screenMaxY - 200)
    color('white')
    write("Snake Rush", align="center", font=("courier",50))
    goto(0, screenMaxY - 215)
    write("CoOl GaMe WiTh CoOl FeAtUrEs...YoU hAvE tO pLaY iT!", align="center")
    turtle.showturtle()
    goto(0,screenMaxY- 350)
    write("Play game",align="center",font=("courier",20))
    goto(0,screenMaxY-400)
    write("Score table",align="center",font=("courier",20))
    goto(0,screenMaxY-450)
    write("How to play", align="center",font=("courier",20))
    turtle.register_shape("nina.gif")
    turtle.shape("nina.gif")
    turtle.goto(-200, -200)
    turtle.stamp()
    turtle.register_shape("nina.gif")
    turtle.shape("nina.gif")
    turtle.goto(200,-200)
    turtle.stamp()
    

    turtle.register_shape("lol.gif")
    turtle.shape("lol.gif")
    turtle.goto(200, 200)
    turtle.stamp()
    turtle.register_shape("lol.gif")
    turtle.shape("lol.gif")
    turtle.goto(200,200)
    turtle.stamp()


    turtle.register_shape("kay.gif")
    turtle.shape("kay.gif")
    turtle.goto(-200, 200)
    turtle.stamp()
    turtle.register_shape("kay.gif")
    turtle.shape("kay.gif")
    turtle.goto(-200,200)
    turtle.stamp()



    turtle.register_shape("ror.gif")
    turtle.shape("ror.gif")
    turtle.goto(-200, -200)
    turtle.stamp()
    turtle.register_shape("ror.gif")
    turtle.shape("ror.gif")
    turtle.goto(-200,-200)
    turtle.stamp()

    


    



    #turtle.getscreen().clearscreen()




















xclick=0
yclick = 0
mainMenu()
mainloop()