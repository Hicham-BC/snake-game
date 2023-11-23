from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 18, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNEMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNEMENT, font=FONT)