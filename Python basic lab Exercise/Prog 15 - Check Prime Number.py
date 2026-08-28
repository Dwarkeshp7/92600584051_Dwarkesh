# (15) Write a Python Program to enter a no. and check it is prime or not?

num = int(input("Enter Number : "))

factorcount = 0

for i in range(1,num + 1):
    if num % i  == 0:
        factorcount = factorcount + 1

if factorcount == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")