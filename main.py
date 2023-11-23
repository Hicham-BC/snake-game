from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#99B080")
screen.title("Welcome to The Snake Game")
screen.tracer(0)

snake = Snake()
food =  Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 9:
        snake.extend()
        food.relocate()
        score.increase_score()
    
    wall_collision = [snake.head.xcor() > 295, snake.head.xcor() < -295, snake.head.ycor() > 295, snake.head.ycor() < -295]

    if any(wall_collision):
        score.game_over()
        game_on = False

    for part in snake.body[1:]:
        if snake.head.distance(part) < 5:
            score.game_over()
            game_on = False

screen.exitonclick()