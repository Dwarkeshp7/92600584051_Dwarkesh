"""4. Write a program to find the sum of digits of a number using a while loop."""

num = int(input("Enter Number :"))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("The Sum of Digit Is :",sum)