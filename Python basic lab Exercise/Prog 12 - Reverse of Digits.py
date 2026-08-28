# (12)  Write a Python Program to enter a no. and find its reverse.

num = int(input("Enter Number : "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse is : ",reverse)