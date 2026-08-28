# Write a python program to enter three no. and find maximum out of it.

Num1 = int(input("Enter FirstNumber :"))
Num2 = int(input("Enter SecondNumber :"))
Num3 = int(input("Enter ThirdNumber :"))

if Num1 > Num2 and Num1 > Num3:
    print("Num1 is Maximum")

elif Num2 > Num1 and Num2 > Num3:
    print("Num2 is Maximum")

else :
    print("Num3 is Maximum")
