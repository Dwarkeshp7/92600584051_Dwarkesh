# Write a python program to enter marks of 3 subjects and find :
# total , percentage , results and class

print("Enter Subjects Marks :")

Sub1 = float(input("Sub1 Marks : "))
Sub2 = float(input("Sub2 Marks : "))
Sub3 = float(input("Sub3 Marks : "))

TotalMarks = Sub1 + Sub2 + Sub3

Percentage = TotalMarks / 3

print("=====Results=====")
print("TotalMarks : " , TotalMarks)
print("Percentage : " , Percentage)

if Sub1 >= 35 and Sub2 >= 35 and Sub3 >= 35:
    print("Pass")

    if Percentage >= 80:
        print("High Class")

    elif Percentage >= 60:
        print("Average Class")

    elif Percentage >= 35:
        print("Low class")

else :
    print("Fail")
