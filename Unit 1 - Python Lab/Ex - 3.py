"""3. Write a program to perform arithmetic relational and logical operations using Python operators."""

num1 = 26
num2 = 4

bol1 = True
bol2 = False

print("===== ARITHMETIC OPERATIONS =====")

print("Addition         :",num1+num2)
print("Substraction     :",num1-num2)
print("Multiplication   :",num1*num2)
print("Division         :",num1/num2)
print("Modulus          :",num1%num2)
print("Floor Division   :",num1//num2)
print("Exponentiation   :",num1**num2)

print("===== RELATIONAL OPERATIONS =====")

print("Eqaual To        :",num1 == num2)
print("Not Equal To     :",num1 != num2)
print("Greater Than     :",num1 > num2)
print("Less Than        :",num1 < num2)
print("Greater Than or Equal To :",num1 >= num2)
print("Less Than or Equal To    :",num1 <= num2)

print("===== LOGICAL OPERATIONS =====")

print("Logical AND Operator :",(num1 > 10) and (num2 < 5))
print("Logical OR  Operator :",(num1 > 10) or (num2 < 1))
print("Logical NOT Operatot :",not(num1 == num2))
