import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
# t.colormode(255)
# for _ in range(15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
# def draw_shape(num_shapes):
#     angle = 360 / num_shapes
#     for _ in range(num_shapes):
#         tim.fd(50)
#         tim.rt(angle)
#
# for shape_sides in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides)

# colors = ["tan", "yellow", "salmon", "chocolate", "deep pink", "MediumVioletRed", "green", "OrangeRed",
#            "brown"]
# directions = [0, 90, 180, 270, 360]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.fd(25)
#     tim.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)






















screen = t.Screen()
screen.exitonclick()