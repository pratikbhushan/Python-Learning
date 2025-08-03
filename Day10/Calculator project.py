import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    should_continue = True
    first_num = float(input("Enter your first number: "))

    while should_continue:
        math_oper = input("+\n-\n*\n/\nPick an operation: ")
        second_num = float(input("Enter your second number: "))

        result = operators[math_oper](n1=first_num, n2=second_num)

        print(f"{first_num} {math_oper} {second_num} = {result}")

        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if user_choice == "y":
            first_num = result
        else:
            should_continue = False
            os.system("cls")
            calculator()

calculator()