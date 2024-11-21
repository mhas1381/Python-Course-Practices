from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()

ball = Ball()
screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)



if __name__ == "__main__":
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        # collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.x_bounce()

        # ball goes of the bound
        if ball.xcor() > 380:
            ball.reset_position()
            ball.reset_speed()
            scoreboard.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            ball.reset_speed()
            scoreboard.r_point()

screen.mainloop()
