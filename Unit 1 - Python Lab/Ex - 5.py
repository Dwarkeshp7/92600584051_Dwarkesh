"""5. Write a program to create and manipulate lists using indexing slicing and list
comprehensions."""

numbers = [10,20,30,40,50,60,70,80,90,100]
print("List :",numbers)

firstelement = numbers[0]
lastelement = numbers[-1]

print("FirstElement :",firstelement)
print("LastElement  :",lastelement)


numbers[2] = 35
print("Modifying index 2 :",numbers)

sublist = numbers[1:5]
print("Sliced sublist :",sublist)

everysecond = numbers[::2]
print("Sliced with step 2 :",everysecond)

reversedlist = numbers[::-1]
print("Reversed list :" ,reversedlist)

squares = [x**2 for x in numbers]
print("Squares using comprehension:",squares)
