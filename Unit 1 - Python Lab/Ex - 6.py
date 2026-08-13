"""6. Write a program to illustrate the use of tuples and sets with basic operations."""

fruits = ("apple", "banana", "cherry", "orange", "kiwi")
print("First element:",fruits[0])
print("Last element:",fruits[-1])
print("Slicing (middle 3):",fruits[1:4])


numbers = {1, 2, 2, 3, 4, 4, 5}
print("Original set:",numbers)

numbers.add(6)
numbers.remove(1)
numbers.discard(5) 

print("Set After Modify  :",numbers)
