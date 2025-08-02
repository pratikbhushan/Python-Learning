import art
import os

print(art.logo)

bid_memory = {}
program_continue = True
while program_continue:

    name = input("What is your name?: ")
    bid_amount = int(input("What is your Bid?: ₹"))
    bid_memory[name] = bid_amount
    user_choice = input("Are there any other bidders? Type 'Yes' or 'No'.").lower()
    if user_choice == "no":
        program_continue = False
        winner = max(bid_memory, key=bid_memory.get)
        max_amount = bid_memory[winner]
        print(f"The winner is {winner} with the bid amount of ₹{max_amount}.")
    elif user_choice == "yes":
        os.system('cls')
        program_continue = True







