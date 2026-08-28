"""6. Write a program to iterate over lists strings and dictionaries using loops."""

fruits = ["Apple","Banana","Cherry"]

for fruit in fruits:
    print(fruit)

print("---------------")

word = "Dwarkesh"

for letters in word:
    print(letters)

print("---------------")

car = {

    "Tata" : "Altroz",
    "Colour" : "Black",
    "Model" : "Top"

}

for key in car:
    print(key)

print("---------------")

for value in car.values():
    print(value)

print("---------------")

for key,value in car.items():
    print("Key :",key,"|","Values :",value)