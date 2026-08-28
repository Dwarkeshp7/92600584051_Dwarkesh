# Write a python program to enter 10 Nos. and find Maximum out of it without using array.

print("===== Enter 10 Numbers =====")

Max = 0

for i in range(1,11):
    Num = int(input("Enter Number : "))

    if Num > Max:
        Max = Num 

print("Maximum Number is : " , Max)
