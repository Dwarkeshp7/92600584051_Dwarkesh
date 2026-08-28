# Write a python program to enter 10 Nos. and find sum and average of it.

print("===== Enter 10 Numbers =====")

Add = 0
Avg = 0

for i in range(1,11):
    Num = int(input("Enter Number : "))
    Add = Add + Num

Avg = Add / 10

print("Sum is : " , Add)
print("Avg is : " , Avg)
