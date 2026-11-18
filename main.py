import scoreboard
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("Snake game")

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = 1
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -300
        or snake.head.ycor() > 300 or snake.head.ycor() < -280):
        game_is_on = 0
        scoreboard.game_over()
















screen.exitonclick()

