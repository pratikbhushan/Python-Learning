import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_chose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

print("\nYour Choice:\n")

if user_chose == 0:
    print(rock)
elif user_chose == 1:
    print(paper)
elif user_chose == 2:
    print(scissors)
else:
    print("Invalid choice!! Game over...")
    exit()

print("\nComputer Choice:\n")

computer_chose = [rock, paper, scissors]
c_choice = random.choice(computer_chose)
print(c_choice)

if user_chose == 0 and c_choice == rock:
    print("Draw!!")
if user_chose == 0 and c_choice == paper:
    print("You lose!!")
if user_chose == 0 and c_choice == scissors:
    print("You Won!!")

if user_chose == 1 and c_choice == rock:
    print("You Won!!")
if user_chose == 1 and c_choice == paper:
    print("Draw!!")
if user_chose == 1 and c_choice == scissors:
    print("You lose!!")

if user_chose == 2 and c_choice == rock:
    print("You lose!!")
if user_chose == 2 and c_choice == paper:
    print("You won!!")
if user_chose == 2 and c_choice == scissors:
    print("Draw!!")

