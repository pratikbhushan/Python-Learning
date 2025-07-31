heights = [152, 180, 176, 190, 165, 174]

# Find the shortest height using a loop

shortest = heights[0]
for minimum in heights:
    if minimum < shortest:
        shortest = minimum

print(shortest)