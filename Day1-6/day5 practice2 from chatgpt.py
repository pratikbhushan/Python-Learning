temperatures = [32, 35, 29, 40, 30, 28, 31]

# Find the highest temperature
# AND also print its index in the list (i.e., which day it happened)

highest = temperatures[0]
for maximum in temperatures:
    if maximum > highest:
        highest = maximum
print(highest)