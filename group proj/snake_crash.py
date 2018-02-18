from turtle import *
import turtle
import time
import random
import math 

color

xposes=[-90,-50,-10,30,50,90]
def Random_Charactaristics():
    global x,y,number
    x = random.choice(xposes)
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color = (r,g,b)
    #number = random.randint(int(0.50*snake),int(1.25*snake))
Random_Charactaristics()
print (x)


