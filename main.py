# Use of the turtle module to creat a Hirst style paiting, generating a random paint with random colours from a list

import turtle as t
import random
screen = t.Screen()
t.colormode(255)
cleyton = t.Turtle()
cleyton.shape("circle")
cleyton.speed("fastest")
cleyton.hideturtle()

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
              (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121),
              (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
              (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
              (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

position_2 = -250
lines = 10
while lines > 0:
    cleyton.penup()
    cleyton.goto(-250, position_2)
    lines -= 1
    position_2 += 50
    for _ in range(10):
        cleyton.color(random.choice(color_list))
        cleyton.stamp()
        cleyton.penup()
        cleyton.forward(50)
        cleyton.pendown()


screen.exitonclick()
