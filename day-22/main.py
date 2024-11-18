from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))

ball = Ball()
screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)



if __name__ == "__main__" :
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ball.move()
        if ball.ycor()>280:
            ball.bounce()



screen.mainloop()
