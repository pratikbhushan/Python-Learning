print("-"*3 + "Restraunt Bill Splitter" + "-"*3)

item_name = input("\nWhat is the name of the Dish?\n")
total_bill = input("What is the total amount of the Bill?\n")
num_people = input("How many people are splitting the Bill?\n")
tip_percentage = input("What tip percentage would you like to add? (e.g., 10 or 15)\n" )
print("\n")

print("-"*3 + "Your Bill Summary" + "-"*3)
print(f"\nDish Ordered: {item_name}")
print(f"Total Bill: Rs. {total_bill}")
print(f"Number of people splitting: {num_people}")
print(f"Suggested Tip: {tip_percentage}%\n")

print("Thank You for your visit!")

