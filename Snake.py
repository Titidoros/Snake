import turtle
import time
import random

delay = 0.1
score = 0
Wi = 600
He = 600

#screen
wn = turtle.Screen()
wn.title("Snake by titi")
wn.bgcolor("light green")
wn.setup(width=Wi, height=He)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = [] 

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()


#Function
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
def pause():
    head.direction ="pause"
def move() :
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "pause":
        x = head.xcor()
        head.setx(x)

#keyboard bindings
def key():
    wn.listen()
    wn.onkeypress(go_up, "z")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "q")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(pause, "space")

#border
def border():
    if head.ycor() > He/2 or head.ycor() < He/-2 or head.xcor() > Wi/2 or head.xcor() < Wi/-2:
        pen.write("You lose", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        head.goto(0, 0)
        pen.clear()
        head.direction = "stop"
        #hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        #clear the segments list
        segments.clear()

#food collision
def collision():
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(Wi/-2, Wi/2)
        y = random.randint(He/-2, He/2)
        food.goto(x, y)
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
    #move the end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

# check for head collision with body
def bodycol():
    for segment in segments:
        if segment.distance(head) < 20:
            pen.write("You lose", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            head.goto(0, 0)
            pen.clear()
            head.direction = "stop"
        #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        #clear the segments list
            segments.clear()


#main game loop
while True:
    wn.update()
    collision()
    move()
    time.sleep(delay)
    border()
    bodycol()
    key()
    #wn.mainloop() breaks the while if not in # seems useless