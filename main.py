"""
First download national anthem and save it in the same folder as "anthem.mp3"
Else code will not work.
"""

import turtle
from pygame import mixer

ws = turtle.Screen()
ws.title("Indian Flag")

mixer.init()
mixer.music.load('anthem.mp3')
mixer.music.play()

flagTurtle = turtle.Turtle()
flagTurtle.speed(300)

# Making sky
flagTurtle.penup()
flagTurtle.goto(0, -100)
flagTurtle.left(180)
flagTurtle.begin_fill()
flagTurtle.fillcolor("#b1f9fc")
flagTurtle.pendown()
flagTurtle.forward(800)
flagTurtle.right(90)
flagTurtle.forward(500)
flagTurtle.right(90)
flagTurtle.forward(1600)
flagTurtle.right(90)
flagTurtle.forward(500)
flagTurtle.right(90)
flagTurtle.forward(800)
flagTurtle.end_fill()

# Making ground
flagTurtle.penup()
flagTurtle.goto(0, -400)
flagTurtle.begin_fill()
flagTurtle.pencolor("#e8c8a7")
flagTurtle.fillcolor("#e8c8a7")
flagTurtle.pendown()
flagTurtle.forward(800)
flagTurtle.right(90)
flagTurtle.forward(300)
flagTurtle.right(90)
flagTurtle.forward(1600)
flagTurtle.right(90)
flagTurtle.forward(300)
flagTurtle.right(90)
flagTurtle.forward(800)
flagTurtle.end_fill()

flagTurtle.speed(3)
# First Rectangle
flagTurtle.penup()
flagTurtle.right(90)
flagTurtle.goto(-180, 200)
flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("orange")
flagTurtle.pencolor("orange")
flagTurtle.forward(90)
flagTurtle.right(90)
flagTurtle.forward(400)
flagTurtle.right(90)
flagTurtle.forward(90)
flagTurtle.right(90)
flagTurtle.forward(400)
flagTurtle.end_fill()

# Second Rectangle
flagTurtle.begin_fill()
flagTurtle.fillcolor("white")
flagTurtle.pencolor("white")
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.end_fill()

# Third Rectangle
flagTurtle.begin_fill()
flagTurtle.fillcolor("green")
flagTurtle.pencolor("green")
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.end_fill()

# Pole
flagTurtle.begin_fill()
flagTurtle.fillcolor("black")
flagTurtle.pencolor("black")
flagTurtle.left(180)
flagTurtle.forward(270)
flagTurtle.circle(10, 180)
flagTurtle.forward(520)
flagTurtle.left(90)
flagTurtle.forward(20)
flagTurtle.left(90)
flagTurtle.forward(250)
flagTurtle.left(180)
flagTurtle.forward(250)
flagTurtle.end_fill()

# Stand 1
flagTurtle.begin_fill()
flagTurtle.fillcolor("brown")
flagTurtle.right(90)
flagTurtle.forward(70)
flagTurtle.circle(25, 90)
flagTurtle.left(90)
flagTurtle.forward(170)
flagTurtle.left(90)
flagTurtle.circle(25, 90)
flagTurtle.forward(50)
flagTurtle.end_fill()

# Stand 2
flagTurtle.penup()
flagTurtle.left(90)
flagTurtle.forward(25)
flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("brown")
flagTurtle.right(90)
flagTurtle.forward(90)
flagTurtle.circle(25, 90)
flagTurtle.left(90)
flagTurtle.forward(210)
flagTurtle.left(90)
flagTurtle.circle(25, 90)
flagTurtle.forward(70)
flagTurtle.end_fill()

# Ashok Chakra
# Outer Circle
flagTurtle.pencolor("#000080")
flagTurtle.penup()
flagTurtle.goto(-20, 155)
flagTurtle.forward(2)
flagTurtle.left(90)
flagTurtle.begin_fill()
flagTurtle.fillcolor("#000080")
flagTurtle.pendown()
flagTurtle.circle(42)
flagTurtle.end_fill()
# Middle Circle
flagTurtle.penup()
flagTurtle.left(90)
flagTurtle.forward(2)
flagTurtle.right(90)
flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("white")
flagTurtle.circle(40)
flagTurtle.end_fill()
flagTurtle.penup()
# Sticks
i = 0
while i < 24:
    flagTurtle.goto(20, 155)
    flagTurtle.right(15)
    flagTurtle.pendown()
    flagTurtle.forward(40)
    flagTurtle.penup()
    i += 1
# Inner Circle
flagTurtle.penup()
flagTurtle.goto(30, 155)
flagTurtle.left(180)
flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("#000080")
flagTurtle.circle(10)
flagTurtle.end_fill()
flagTurtle.penup()

# My Name
flagTurtle.pencolor("black")
flagTurtle.goto(200, -230)
style = ('Courier', 90, 'normal')
flagTurtle.write('Saksham', font=style, align='center')

# Finishing
turtle.hideturtle()
flagTurtle.hideturtle()
turtle.done()
