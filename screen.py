from turtle import Turtle, Screen


road_draw = Turtle()
number_of_roads = 6
road_draw.penup()
road_draw.goto(-300, -200)
road_draw.shape('square')
road_draw.color('grey')
road_draw.pensize(60)
road_draw.hideturtle()
number_of_dashes = 770
dash = Turtle()
dash.penup()
dash.setheading(0)
dash.color('white')
dash.shape('square')
dash.pensize(2)
dash.goto(-300, -200)
dash.hideturtle()




def road_setup():
    for road in range(1, number_of_roads + 1):
        road_draw.hideturtle()
        road_draw.pendown()
        road_draw.forward(600)
        road_draw.setheading(90)
        road_draw.penup()
        road_draw.forward(80)
        road_draw.setheading(180)
        road_draw.forward(600)
        road_draw.setheading(0)


def screen_setup():
    for dash_count in range(1, min(number_of_dashes + 1, number_of_roads * 88)):
        dash.pendown()
        dash.forward(10)
        dash.penup()
        dash.forward(20)
        if dash.xcor() >= 300:
            dash.setheading(90)
            dash.forward(80)
            dash.setheading(180)
            dash.forward(600)
            dash.setheading(0)
        if dash.ycor() >= 250:
            break
