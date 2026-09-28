# Standard Import
import Calculator

print("Module created by : ",Calculator.author)

result_1 = Calculator.add(10, 5)
result_2 = Calculator.subtract(10, 5)

print("Addition Result : ",result_1)
print("Subtraction Result : ",result_2)

# Import Specific Functions

from Calculator import add, subtract

print(add(20, 10))
print(subtract(20, 10))


# Import with an Alias

import Calculator as calc

print(calc.add(8, 2))
