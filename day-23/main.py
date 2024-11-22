import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

timmy = Player()
screen.listen()
screen.onkey(timmy.move , "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

if __name__ == "__main__":
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move()

        for car in car_manager.cars:
            if timmy.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

        if timmy.ycor()>280:
            timmy.reset_position()
            car_manager.increase_speed()
            scoreboard.increase_score()

screen.mainloop()