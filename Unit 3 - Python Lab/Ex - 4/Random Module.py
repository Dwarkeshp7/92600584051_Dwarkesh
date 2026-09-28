# 4. Write a program to generate random numbers using random module. 

import random

print("--- Generating Random Numbers ---")

# 1. Generate a random floating-point number between 0.0 and 1.0
print("Random float between 0.0 and 1.0:", random.random())

# 2. Generate a random integer between a specific range (inclusive)
# Example: Rolling a 6-sided die (1 to 6)
print("Random integer between 1 and 6:", random.randint(1, 6))

# 3. Generate a random floating-point number between a specific range
print("Random float between 10.5 and 50.5:", random.uniform(10.5, 50.5))

# 4. Pick a random item from a list
fruits = ["Apple", "Banana", "Cherry", "Orange"]
print("Randomly selected fruit from the list:", random.choice(fruits))
