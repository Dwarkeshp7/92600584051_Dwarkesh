# (3) Write a python program to enter a string and check whether it is palindrome or not ?

string = input("Enter The String :")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
