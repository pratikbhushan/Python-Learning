from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day20-21\Snake Game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\vishw\OneDrive\Desktop\Python learning\Projects\Day20-21\Snake Game\data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
        
