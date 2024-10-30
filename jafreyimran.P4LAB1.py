import turtle

screen = turtle.Screen()
screen.title("Square and Triangle with Turtle Graphics")
pen = turtle.Turtle()
pen.color("blue")
side_length = 100
for _ in range(4):
    pen.forward(side_length)
    pen.right(90)
pen.penup()
pen.goto(150, 0)
pen.pendown()
pen.color("green")
for _ in range(3):
    pen.forward(side_length)
    pen.right(120)
pen.hideturtle()
turtle.done()
