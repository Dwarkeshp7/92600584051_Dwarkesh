"""7. Write a program to demonstrate list dictionary and set comprehensions. """

squares = [x ** 2 for x in range(1,6)]

cubes_dict = {x : x ** 3 for x in range(1,4)}

letters = {char for char in "banana"}

print(squares)
print(cubes_dict)
print(letters)
