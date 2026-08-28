# (13) Write a Python Program to enter a no. and check it is palindrome or not ? 

num = int(input("Enter Number : "))

original = num 
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")