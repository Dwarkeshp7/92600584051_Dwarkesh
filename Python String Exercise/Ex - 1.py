#(1) Write a python program to enter your full name and print your initial. 

name = input("Enter your name: ")

nameparts = name.split()

initials = ".".join(part[0].upper() for part in nameparts)

print("Your initials are:",initials)
