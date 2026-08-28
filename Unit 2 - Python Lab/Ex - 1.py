"""1. Write a program to demonstrate conditional statements using if if-else and if-elif-else."""

temp = int(input(("Enter Temprature : ")))
age = int(input("Enter Age : "))
score = int(input("Enter Score : "))

if temp > 30:
    print("It's a Hot Today!")

print("--------------------")

if age > 18:
    print("You are Eligible For Vote!")
else:
    print("You're not Eligible For Vote.")

print("--------------------")

if score >= 90:
    print("Grade : A+")
elif score >= 80:
    print("Grade : A")
elif score >= 70:
    print("Grade : B")
elif score >= 60:
    print("Grade : C")
elif score >= 50:
    print("Grade : D")
elif score >= 35:
    print("Grade : E")
else:
    print("Fail.")