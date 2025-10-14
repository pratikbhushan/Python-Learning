# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 21)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()


color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 
232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):    
    tim.dot(15, random.choice(color_list))
    tim.forward(30) 

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()