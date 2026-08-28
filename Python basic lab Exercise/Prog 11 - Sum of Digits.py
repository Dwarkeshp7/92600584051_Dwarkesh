# (11) Write a Python Program to enter a no. and find sum of its digits. 

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits is : ", sum)