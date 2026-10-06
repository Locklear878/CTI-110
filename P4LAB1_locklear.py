# CTI-110
# P4LAB1
# Turtle
# 10/6/26

# set up yout turtle
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("skyblue") #change this if you want

t = turtle.Turtle() #variable "t" now hold our turtle
#set these to your preference
t.color("blue")
t.shape("turtle")
t.pencolor("blue")
t.fillcolor("purple")
t.pensize("3")

# Draw with t (your code here)
sides = 4
angle = 360 / sides
length = 100
# example 1
with t.fill():
    while sides > 0:
        t.forward(length)
        t.right(angle)
        sides = sides - 1

# example 2
t.teleport(-200, 0)
sides = 4
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

# put a roof on the house
sides = 3
t.fillcolor("black")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()
    
t.teleport(0, 0)
sides = 3
t.fillcolor("yellow")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()
    
t.teleport(200, 0)
sides = 4
t.fillcolor("purple")
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()
sides = 3
t.fillcolor("green")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()
    
# put a star
t.penup()
t.goto(-250, 180)
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

# End - keep window open
turtle.done()
