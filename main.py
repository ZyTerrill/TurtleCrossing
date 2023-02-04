import time
from turtle import Screen, Turtle
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

window = Screen()
window.bgcolor('green')
window.setup(width=600, height=600)
window.tracer(0)
Flag = True

road_draw = Turtle()
road_draw.hideturtle()
number_of_roads = 6
road_draw.penup()
road_draw.goto(-300, -200)
road_draw.shape('square')
road_draw.color('grey')
road_draw.pensize(60)
number_of_dashes = 770
dash = Turtle()
dash.hideturtle()
dash.penup()
dash.setheading(0)
dash.color('white')
dash.shape('square')
dash.pensize(2)
dash.goto(-300, -200)
dash.hideturtle()


def road_setup():
    for road in range(1, number_of_roads + 1):
        print(road_draw.pos())
        road_draw.pendown()
        road_draw.forward(600)
        road_draw.setheading(90)
        road_draw.penup()
        road_draw.forward(86)
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
            dash.forward(86)
            dash.setheading(180)
            dash.forward(600)
            dash.setheading(0)
        if dash.ycor() >= 250:
            break

road_setup()
screen_setup()

turt = Player()
window.listen()
window.onkey(turt.up, "Up")
window.onkey(turt.down, "Down")
window.onkey(turt.left, "Left")
window.onkey(turt.right, "Right")
win_rate = 1
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turt) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turt.reset_positions():
        turt.goto_start()
        scoreboard.increase_score()
        car_manager.level_up()


