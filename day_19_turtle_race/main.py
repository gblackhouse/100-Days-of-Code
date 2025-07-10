from operator import length_hint
from turtle import Turtle, Screen
import random

racing = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    racing = True

while racing:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! the {winning_color} turtle was the winner")
                    racing = False
                else:
                    print(f"You've lost! the {winning_color} turtle was the winner")
                    racing = False
            random_speed = random.randint(0, 10)
            turtle.forward(random_speed)

screen.exitonclick()

