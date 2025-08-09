import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

def play_game():
    lives = 0
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        lives = 10
        print("You have 10 lives to make the guess.")
    elif difficulty == "hard":
        lives = 5
        print("You have 5 lives to make the guess.")

    continue_game = True
    while continue_game:
        user_guess = int(input("Make a guess: "))

        if lives == 1:
            print(f"You lose! The answer was {random_number}")
            print("Rerun the program to play again.")
            exit()
        if user_guess > random_number:
            lives -= 1
            print(f"Too high! Guess again. You have {lives} lives left.")
        elif user_guess < random_number:
            lives -= 1
            print(f"Too Low! Guess again. You have {lives} lives left.")
        elif user_guess == random_number:
            print(f"Yay! You won the game.. The answer was {random_number}")
            print("Rerun the program to play again.")
            exit()



play_game()