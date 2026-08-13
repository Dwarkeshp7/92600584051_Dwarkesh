"""4. Write a program to demonstrate string operations including slicing formatting and
built-in string functions."""

message = "  Hello, Python Programming World!  "
print("Original String:",message)

print("----------------------------------------------")

cleaned_message = message.strip()
print("Cleaned String :",cleaned_message)

print("\nUppercase:", cleaned_message.upper())
print("Lowercase:", cleaned_message.lower())

replaced_text = cleaned_message.replace("Programming", "Coding")
print("Replaced Text:", replaced_text)

print("Count of letter - o:", cleaned_message.count("o"))
print("Position of word - Python:", cleaned_message.find("Python"))
print("----------------------------------------------")

print("First 5 chars:", cleaned_message[0:5])

print("Middle word:", cleaned_message[7:13])

print("From index 14 to end:", cleaned_message[14:])

print("Reversed string:", cleaned_message[::-1])

print("----------------------------------------------")

name = "Dwarkesh"
language = "Python"
version = 3.12

f_string_msg = "Hello",name,"welcome to",language,"version",version
print("f-String Formatting:",f_string_msg)

