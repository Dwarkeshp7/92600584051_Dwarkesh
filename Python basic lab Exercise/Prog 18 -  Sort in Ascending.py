# (18) Write a Python Program to enter 10 nos. and sort them in ascending order 

num = []

for i in range(10):
    n = int(input("Enter Number : "))
    num.append(n)

num.sort()

print(num)