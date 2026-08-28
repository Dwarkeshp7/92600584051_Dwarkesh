"""(10)
Write a python program to count the digits in given string and also give sum of digits. If no digits 
available in string print 0. 
Input : Hello123World 
Output : No. of digits : 3 
Sum of digits : 6 
Input : HelloWorld 
Output : 0
"""

text = input("Input : ")

digit_count = 0
digit_sum = 0

for char in text:
    
    if char.isdigit():
        digit_count += 1
        digit_sum += int(char)
        
if digit_count > 0:
    print("Output : No. of digits :",digit_count)
    print("Sum of digits :",digit_sum)
else:
    print("Output : 0")
