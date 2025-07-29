print("Welcome to Mad Libs!")
print("Please give me some words to form a funny story.")

adjective = input("Please enter an adjective:\n")
noun = input("Please enter a noun:\n")
verb = input("Please enter a verb:\n")
verb_ing = input("Please enter a verb ending in -ing:\n")
place = input("Please enter a place:\n")
plural_noun  = input("Please enter a plural noun :\n")
body_part = input("Please enter a body part:\n")

story = f'''One sunny morning, a {adjective} {noun} decided to take a walk in the place.
Suddenly, they saw a another {adjective} {plural_noun} {verb_ing} by the {body_part}.
The {noun} felt very {adjective} and decided to {verb} with them.
It was the most {adjective} adventure ever!'''

print(story)
 
