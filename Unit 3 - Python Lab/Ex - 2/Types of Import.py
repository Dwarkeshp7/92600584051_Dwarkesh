# 2. Write a program to demonstrate different import mechanisms in Python.

# 1. Standard Module Import (Whole Module)

import math

print("--- 1. Standard Module Import ---")
print("Value of pi: ",math.pi)
print("Square root of 16: ",math.sqrt(16),"\n")


# 2. Module Import with an Alias
import datetime as dt

print("--- 2. Import with an Alias ---")
print("Current local time via 'dt': ",dt.datetime.now(),"\n")

# 3. Specific Attribute Import (from ... import ...)
from os import getcwd, name

print("--- 3. Specific Attribute Import ---")
print("Operating system family: ",name)
print("Current working directory: ",getcwd(),"\n")


# 4. Specific Attribute Import with an Alias

from time import sleep as pause_execution

print("--- 4. Attribute Import with an Alias ---")
print("Pausing execution for 0.5 seconds...")
pause_execution(0.5)
print("Resumed!\n")

# 5. Wildcard Import (from ... import *)
from random import *

print("--- 5. Wildcard Import ---")
# choice() and randint() belong to 'random', but are called without a prefix
my_list = ["Apple", "Banana", "Cherry"]
print("Random choice: ",choice(my_list))
print("Random integer (1-100): ",randint(1, 100),"\n")

# 6. Dynamic Import (Using importlib)

import importlib

print("--- 6. Dynamic Import ---")
module_name = "sys"
dynamic_sys = importlib.import_module(module_name)
print("Dynamically loaded ",module_name,'Python Version: ',dynamic_sys.version)

