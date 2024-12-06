import turtle

class Num():
    def __init__(self, color):
        self.pensize = 10
        self.color = color
        self.delay = 0.2

    def draw(self, digit):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(0, 0)
        turtle.pensize(10)
        turtle.color(self.color)
        if digit == 0:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.penup()

        if digit == 1:
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

        if digit == 2:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.penup()

        if digit == 3:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()

        if digit == 4:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.penup()

        if digit == 5:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.penup()

        if digit == 6:
            self.draw(5)
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()
        
        if digit == 7:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()

        if digit == 9:
            self.draw(5)
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()

    def clear(self):
        turtle.clear()

    def my_delay(self):
        import time
        start =  time.time()
        while time.time() - start < self.delay:
            pass

