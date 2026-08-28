"""3. Write a program to generate a multiplication table using a for loop. """

num = int(input("Enter Number for Multiplication Table :"))

for i in range(1,11):
    print(num," ","*"," ",i," ","=",i*num)