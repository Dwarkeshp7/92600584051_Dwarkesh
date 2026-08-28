"""2. Write a program to check whether a number is positive negative or zero using nested conditions. """

num = int(input("Enter Number : "))

if num >= 0:

    if num > 0:
        print("Positive")
    else:
        print("Zero")

else:

    print("negative")