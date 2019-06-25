# All of the imports

import turtle
import math
import time
import random

# The Screen

wn = turtle.Screen()
wn.title("Avoid The Squares: by F6Studios")
wn.setup(width=900, height=1000)
wn.bgcolor("black")
wn.tracer(0)

# Bottom Border Color
border_color_1 = turtle.Turtle()
border_color_1.speed(0)
border_color_1.shape("square")
border_color_1.color("orange")
border_color_1.shapesize(stretch_wid=0.25, stretch_len=40)
border_color_1.penup()
border_color_1.goto(0, -400)

# Bottom Border Color
border_color_2 = turtle.Turtle()
border_color_2.speed(0)
border_color_2.shape("square")
border_color_2.color("orange")
border_color_2.shapesize(stretch_wid=0.25, stretch_len=40)
border_color_2.penup()
border_color_2.goto(0, 400)

# Random Coords for the BadNPCs
playerB_randY = random.randint(-200, 350)
playerB_randX = random.randint(-350, 350)
playerC_randY = random.randint(-350, 350)
playerC_randX = random.randint(-350, 350)
playerD_randY = random.randint(-350, 350)
playerD_randX = random.randint(-350, 350)

# Left Border Color
border_color_3 = turtle.Turtle()
border_color_3.speed(0)
border_color_3.shape("square")
border_color_3.color("orange")
border_color_3.shapesize(stretch_wid=40.25, stretch_len=0.25)
border_color_3.penup()
border_color_3.goto(-400, 0)

# Right Border Color
border_color_4 = turtle.Turtle()
border_color_4.speed(0)
border_color_4.shape("square")
border_color_4.color("orange")
border_color_4.shapesize(stretch_wid=40.25, stretch_len=0.25)
border_color_4.penup()
border_color_4.goto(400, 0)

# Timer
timer = turtle.Turtle()
timer.speed(0)
timer.color("white")
timer.penup()
timer.hideturtle()
timer.goto(0, 410)
timer.shapesize(stretch_len=20, stretch_wid=20)

#By F6Studios
at = turtle.Turtle()
at.speed(0)
at.color("white")
at.penup()
at.hideturtle()
at.goto(0, -475)
at.shapesize(stretch_len=20, stretch_wid=20)
at.write("By F6Studios", align="center", font=("Courier", 24, "bold"))

#Game Over
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("white")
gameover.penup()
gameover.hideturtle()
gameover.goto(0, -200)
gameover.shapesize(stretch_len=20, stretch_wid=20)
gameover.hideturtle()

# Player
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("blue")
player_a.shapesize(stretch_wid=3, stretch_len=3)
player_a.penup()
player_a.goto(0, -350)

# Bad NPC
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("red")
player_b.shapesize(stretch_wid=2, stretch_len=2)
player_b.penup()
player_b.sety(playerB_randY)
player_b.setx(playerB_randX)
player_b.dx = 3.0
player_b.dy = 2.5

# Bad NPC 2
player_c = turtle.Turtle()
player_c.speed(0)
player_c.shape("square")
player_c.color("red")
player_c.shapesize(stretch_wid=2, stretch_len=2)
player_c.penup()
player_c.goto(0, 3000)
player_c.dx = 0.0
player_c.dy = 0.0

# Bad NPC 3
player_d = turtle.Turtle()
player_d.speed(0)
player_d.shape("square")
player_d.color("red")
player_d.shapesize(stretch_wid=2, stretch_len=2)
player_d.penup()
player_d.goto(0, 3000)
player_d.dx = 0.0
player_d.dy = 0.0

# Move Functions
def player_a_left():
    x = player_a.xcor()
    x -= 20
    player_a.setx(x)

def player_a_right():
    x = player_a.xcor()
    x += 20
    player_a.setx(x)

def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)


# Collision
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 50:
        return True    
    else:
        return False


# Keyboard Bindings - wn is the var i have for the window screen
wn.listen()
wn.onkeypress(player_a_left, "a")
wn.onkeypress(player_a_left, "Left")
wn.onkeypress(player_a_right, "d")
wn.onkeypress(player_a_right, "Right")
wn.onkeypress(player_a_up, "w")
wn.onkeypress(player_a_up, "Up")
wn.onkeypress(player_a_down, "s")
wn.onkeypress(player_a_down, "Down")

# This makes it so that the standard FPS is 180 so that the objects move the same speed
startTime = time.time()
now = startTime
interval = 20
fps = 180
timeInterval = int(1000 / fps)
myTimeMilliSec = timeInterval

# Main Loop
while True:
    wn.update()
    now = time.time() - startTime
    nowIntMilliSec = int(now * 1000)

    if (nowIntMilliSec > myTimeMilliSec):
        myTimeMilliSec = myTimeMilliSec + timeInterval

        TimeString = "Time: " + str(int(now))
        #imeString = "NrTimes: " + str(int(nrTimes))
        timer.clear()
        timer.write(TimeString, align="center", font=("Courier", 48, "bold"))


        # Bad NPC 2 - Border Bounces
        if int(now) == 19:
            player_c.dx = 4
            player_c.dy = 3.5
            player_c.setx(playerC_randX)
            player_c.sety(playerC_randY)
        if now > 20:
            player_c.sety(player_c.ycor() + player_c.dy)
            player_c.setx(player_c.xcor() + player_c.dx)
            if player_c.ycor() < -380:
                player_c.sety(-380)
                player_c.dy *= -1
            
            if player_c.ycor() > 380:
                player_c.sety(380)
                player_c.dy *= -1

            if player_c.xcor() < -380:
                player_c.setx(-380)
                player_c.dx *= -1

            if player_c.xcor() > 380:
                player_c.setx(380)
                player_c.dx *= -1


        # Bad NPC 3 - Border Bounces
        if int(now) == 39:
            player_d.dx = 5
            player_d.dy = 4.5
            player_d.setx(playerD_randX)
            player_d.sety(playerD_randY)
        if now > 40:
            player_d.sety(player_d.ycor() + player_d.dy)
            player_d.setx(player_d.xcor() + player_d.dx)
            if player_d.ycor() < -380:
                player_d.sety(-380)
                player_d.dy *= -1
            
            if player_d.ycor() > 380:
                player_d.sety(380)
                player_d.dy *= -1

            if player_d.xcor() < -380:
                player_d.setx(-380)
                player_d.dx *= -1

            if player_d.xcor() > 380:
                player_d.setx(380)
                player_d.dx *= -1


        player_b.sety(player_b.ycor() + player_b.dy)
        player_b.setx(player_b.xcor() + player_b.dx)
        # Bad NPC 1 - Border Bounces
        if player_b.ycor() < -380:
            player_b.sety(-380)
            player_b.dy *= -1
        
        if player_b.ycor() > 380:
            player_b.sety(380)
            player_b.dy *= -1

        if player_b.xcor() < -380:
            player_b.setx(-380)
            player_b.dx *= -1

        if player_b.xcor() > 380:
            player_b.setx(380)
            player_b.dx *= -1
        # Player Border
        if player_a.ycor() < -365:
            player_a.sety(-365)

        if player_a.ycor() > 365:
            player_a.sety(365)

        if player_a.xcor() > 365:
            player_a.setx(365)

        if player_a.xcor() < -365:
            player_a.setx(-365)

        # Bad NPCs and Player Collision
        if isCollision(player_a, player_b):
            player_a.setposition(0, 450)
            gameover.write("Game Over", align="center", font=("Courier", 48, "bold"))
            time.sleep(2)
            print("Game Over!")
            print(TimeString)
            break

        if isCollision(player_a, player_c):
            player_a.setposition(0, 450)
            gameover.write("Game Over", align="center", font=("Courier", 48, "bold"))
            time.sleep(2)
            print("Game Over!")
            print(TimeString)
            break

        if isCollision(player_a, player_d):
            player_a.setposition(0, 450)
            gameover.write("Game Over", align="center", font=("Courier", 48, "bold"))
            time.sleep(2)
            print("Game Over!")
            print(TimeString)
            break

        if isCollision(player_b, player_c):
            player_b.dx *= -1
            player_b.dy *= -1
            player_c.dx *= -1
            player_c.dy *= -1

        if isCollision(player_b, player_d):
            player_b.dx *= -1
            player_b.dy *= -1
            player_d.dx *= -1
            player_d.dy *= -1

        if isCollision(player_c, player_d):
            player_d.dx *= -1
            player_d.dy *= -1
            player_c.dx *= -1
            player_c.dy *= -1

        # Little easter-egg at the end