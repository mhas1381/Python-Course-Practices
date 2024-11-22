from turtle import Turtle

with open('data.txt', mode='r') as file:
    highest_score = file.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = int(highest_score)
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score}  Highest Score = {self.highest_score}", align="center",
                   font=('Arial', 14, 'normal'))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open("data.txt", mode='w') as f:
            f.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write(arg="Game Over", align="center" , font=('Arial', 14, 'normal'))
