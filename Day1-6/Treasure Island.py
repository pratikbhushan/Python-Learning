print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print('''Your mission is to find the treasure.\n''')

first_level = input("You're at a jungle fork. Do you go 'left' or 'right'?\n").lower()
if first_level == "left":
    second_level = input("You reach a murky river. Do you 'swim' or 'wait'?\n").lower()
    if second_level == "wait":
        third_level = input("Three doors appear: 'red', 'yellow', and 'blue'. Which one do you choose?\n").lower()
        if third_level == "yellow":
            print("You steped into the golden chamber.")
            print("Yay! you won the treasure!!")
        elif third_level == "red":
            print("Game over! You entered in the house full of fire!")
        elif third_level == "blue":
            print("Game Over! You were eaten by the monsters.")
        else:
            print("⚠️ Invalid choice. The temple rejects indecisive minds!")

    elif second_level == "swim":
        print("🦈 Oh no! You were eaten alive by river sharks. Game Over!")
    else:
        print("⚠️ You must choose a valid action. Game Over!")
elif first_level == "right":
    print("Fall off cliff – Game Over")
else:
    print("You didn't entered a valid input. Game over.")
