# (14) Write a Python Program to enter a no. and check it is Armstrong or not?

num = int(input("Enter Number : "))

original = num

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + (digit ** 3)
    num = num // 10

if sum == original:
    print("Number is Armstrong !")
else:
    print("Number is Not Armstrong.")