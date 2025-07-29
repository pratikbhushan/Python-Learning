import random
print("___Welcome to Number Guesser___\n")
user_guess = int(input("Enter the number between 1 to 5 to make your guess:\n"))
orignal_number = random.randint(1, 5)

if user_guess > 5 or user_guess < 1:
    print("You entered an invalid guess.")

elif user_guess > orignal_number:
    print(f"Sorry your guess was little high. The number was {orignal_number}")

elif user_guess < orignal_number:
    print(f"Sorry your guess was little low. The number was {orignal_number}")

else:
    print(f"Yay!! you guess the correct number. The number was {orignal_number}")

