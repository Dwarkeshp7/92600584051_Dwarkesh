"""(7)
Write a python program to perform following operation : 
Input String : Hello 
Input a character : X 
Input number of times : 3 
Output : HelloXHelloXHello 
"""

txt = input("Enter String :")
char = input("Entet Character :")
times = int(input("Input number of times:"))

result = char.join([txt]*times)

print(result)
