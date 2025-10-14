# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]

table.add_row(["Charizard", "Fire"])
table.add_row(["Bulbasaur", "Earth"])
table.add_row(["Pikachu", "Electric"])

table.align = "l"

print(table)