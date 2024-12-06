import turtle

from pyparsing import srange
import ball
import random
import math
from seven_segments_proc import Num
import time

class balldb():
    def __init__(self):
        self.ball = []
        self.border = border()

    def create(self, ball_num):
        b = border()
        for i in range(ball_num):
            # size = random.uniform(0.01, 0.1) * b.canvas_width
            size = 0.05 * b.canvas_width
            x = (random.randint(int(-1*b.canvas_width + size), int(b.canvas_width - size)))
            y = (random.randint(int(-1*b.canvas_height + size), int(b.canvas_height - size)))
            vx = (2*random.uniform(-1.0, 1.0))
            vy = (2*random.uniform(-1.0, 1.0))
            ball_color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            mass =  (4/3) * math.pi * (size**3) * 2
            tball = ball.ball(x=x, y=y, vx=vx, vy=vy, size=size, color=ball_color, mass=mass)
            self.ball.append(tball)

class border():
    def __init__(self):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

class run():
    def __init__(self, num_ball):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.num = num_ball
        self.ballset =  balldb()
        self.ballset.create(self.num)
        self.dt = 0.5
        self.border = self.ballset.border
        self.digit = Num((255, 0, 0))
        
    def run(self):
        x = 0
        start = time.time()
        self.digit.draw(x)
        while (True):
            turtle.clear()
            self.border.draw_border()
            for i in self.ballset.ball:
                i.draw_ball() 
                i.update_ball_velocity(self.border.canvas_width,self.border.canvas_height)
                i.move_ball(self.dt)
            end = time.time()
            self.digit.draw(x)
            if end - start >= 0.2:
                x += 1
                start = time.time()
            if x > 9:
                x = 0
            turtle.update()

# num_balls = int(input("Number of balls to simulate: "))
num_balls = 5
st = run(num_balls)
st.run()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
