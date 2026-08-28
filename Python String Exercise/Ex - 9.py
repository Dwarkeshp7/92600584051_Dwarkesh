"""(9)
Write a python program to enter a string, character to replace and replacement character.  
Output will be new string. 
Input : Hello ! How are you  ? 
Character to replace : H 
Replacement Character : P 
Output : Pello ! Pow are you ?
"""

txt = input("Enter String :")
char_to_replace = input("Character to replace : ")
replacement_char = input("Replacement Character : ")

result = txt.replace(char_to_replace,replacement_char)

print(result)
