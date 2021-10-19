from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 500)

all_turtle = []
colors = ["red", "blue", "pink", "yellow", "green"]
coordinate = [(-200, 0), (-200, 30), (-200, 60), (-200, -30), (-200, -60)]
player_turtle = screen.textinput("Turtle Racing", "Choose the turtle do you want to bet on")
winner_turtle = None

for i in range(0, 5):
    all_turtle.append(Turtle())
    all_turtle[i].shape("turtle")
    all_turtle[i].color(f"{colors[i]}")
    all_turtle[i].penup()
    all_turtle[i].goto(coordinate[i][0], coordinate[i][1])

game_is_on = True

while game_is_on:
    for turtle in all_turtle:
        turtle.forward(randint(10, 20))
        if turtle.xcor() > 200:
            winner_turtle = turtle.color()[0]
            game_is_on = False
            break


if player_turtle == winner_turtle:
    print("Congratulations!")
print(f"{winner_turtle} turtle won!")

screen.exitonclick()
