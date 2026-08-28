# (16) Write a Python Program to enter a no. and check it is KrishnaMurthy no. or not?

num = int(input("Enter Number : "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1,digit + 1):
        fact = fact * i

    sum = sum + fact
    num = num // 10

if sum == original:
    print("KrishnaMurthy Number")
else:
    print("Not a KrishnaMurthy Number")