import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width = 600 , height=600)
screen.title("Snake Game")
screen.bgcolor("green")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)

game_is_on = True

if __name__ == "__main__":
    while game_is_on:
        screen.update()
        time.sleep(0.15)
        snake.move()

screen.mainloop()
