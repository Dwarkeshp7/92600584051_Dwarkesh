""" (4)
Write a python program to print as following : 
Input : Hi 
Output : HHii
"""

text = input("Enter a String: ")

result = "".join(char * 2 for char in text)

print("Output:", result)
