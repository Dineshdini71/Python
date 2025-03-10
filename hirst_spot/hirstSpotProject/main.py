# import colorgram
#
# rgb_colors = []
# img_colors = colorgram.extract('image.jpg', 30)
# for color in img_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.ht()
color_list= [(155, 80, 50), (21, 29, 67), (194, 153, 134), (37, 104, 164), (246, 219, 69), (121, 165, 192), (157, 67, 100), (171, 155, 161), (24, 50, 128), (65, 24, 40), (67, 30, 16), (118, 189, 151), (119, 31, 53), (223, 85, 51), (20, 88, 37), (196, 82, 118), (126, 32, 15), (58, 126, 50), (56, 125, 209), (16, 64, 36), (10, 86, 106), (253, 216, 0), (175, 167, 54), (210, 181, 188), (73, 174, 111), (226, 177, 166)]
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_of_count = 100
for dot_count in range(1, number_of_count + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)
        print(dot_count)










screen = turtle_module.Screen()
screen.exitonclick()