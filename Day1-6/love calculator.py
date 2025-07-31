import random
print("___Welcome to Love Calculator___")
user_name = input("Enter your name: ")
crush_name = input("Enter your crush name: ")
love_score = random.randint(1, 100)
print(f"The love score between {user_name} and {crush_name} is {love_score}%")
if love_score > 80:
    print("You guys are made for each other.")
elif love_score >= 50 and love_score < 80:
    print("There's a potential.")
elif love_score < 50:
    print("You guys are just friends.")
