from turtle import Turtle

positions = [0, -20, -40]
distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in positions:
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position, 0)
            self.snake.append(snake_part)

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part - 1].xcor()
            new_y = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def extend(self):
        last_part = self.snake[-1]
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(last_part.position())
        self.snake.append(new_part)
