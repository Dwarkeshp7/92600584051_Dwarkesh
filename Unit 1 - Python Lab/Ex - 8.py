"""8. Write a program to explain mutable and immutable objects in Python."""

x = 10
print("x value:", x)
print("x memory address (ID):", id(x))

x = x + 5
print("Updated x value:", x)
print("New x memory address (ID):", id(x))

print("------------------------")

text = "Hello"
print("string:", text)
print("string ID:", id(text))

print("------------------------")

my_list = [1, 2, 3]
print("list contents:", my_list)
print("list memory address (ID):", id(my_list))

my_list.append(4)
print("Updated list contents:", my_list)
print("New list memory address (ID):", id(my_list))

print("------------------------")

list_a = [10, 20]
list_b = list_a

print("list_a :", list_a)
print("list_b :", list_b)
print("Are they pointing to the same object?", id(list_a) == id(list_b))

print("------------------------")

list_b.append(30)
print("After modifying list_b:")
print("list_b:", list_b)
print("list_a:", list_a)








