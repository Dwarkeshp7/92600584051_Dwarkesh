"""(6)
Write a python program to enter two strings and prepare a new string by combining both the 
strings in following manner : 
Input String one : abc 
Input string two : xyz 
output : axbycz 
"""

str1 = input("Enter String One :")
str2 = input("Enter String Two :")

newstr = "".join(i + j for i,j in zip(str1,str2))

print(newstr)
