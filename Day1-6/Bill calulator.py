print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = float(input("How much tip would you like to give? 10%, 12% or 15% just write the number.\n"))
people = int(input("How many people to split the bills?\n"))

each_person_cost = ((total_bill * (tip/100)) + total_bill)/people
individual_cost = round(each_person_cost, 2)

print(f"Each person need to pay: ${individual_cost}")
