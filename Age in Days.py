print("___Find your Age in Days___\n")
user_age = int(input("Write the year in which you were born: "))
current_year = int(input("Write the year in which you wanna check your age: "))

result = (current_year - user_age)*365

print(f"You are approxemately {result} days old.")