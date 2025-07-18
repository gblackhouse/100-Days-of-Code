from turtle import Screen, Turtle
import time
from snake import Snake
screen = Screen()
turtle = Turtle()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


snake_game = True
while snake_game:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()