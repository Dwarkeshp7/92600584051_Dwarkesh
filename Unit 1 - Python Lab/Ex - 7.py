"""7. Write a program to create a dictionary and demonstrate dictionary methods and iteration."""

student = {
    "name": "Dwarkesh",
    "age": 21,
    "course": "MCA",
    "skills": ["Python", "SQL"]
}

print(student)

print("\n",student.keys())
print("\n",student.values())

student.update({"age": 22, "city": "Rajkot"})
print("\nAfter update:",student)


removedcourse = student.pop("course")
print("\nAfter pop",student)


print("Iterating over keys:")
for key in student:
    print("  Key: ",key)


print("\nIterating over values:")
for value in student.values():
    print("  Value:",value)


print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(key ,":", value)
