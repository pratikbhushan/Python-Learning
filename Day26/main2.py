# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Pratik"
# new_list = [letter for letter in name]
# print(new_list)

# store = range(1,5)
# range_list = [n*2 for n in store]
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

