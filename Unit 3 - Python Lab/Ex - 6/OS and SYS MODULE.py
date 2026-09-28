"""6. Write a program to perform file and directory 
operations using os and sys modules. """

import os
import sys

print("--- System Information (sys module) ---")
print("Python Version:", sys.version)
print("Operating System Platform:", sys.platform)

print("\n--- Directory Operations (os module) ---")
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Create a new directory
dir_name = "test_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print("Created directory named:", dir_name)
else:
    print("Directory already exists:", dir_name)

# List all items in the current directory
print("Items in current directory:", os.listdir("."))

print("\n--- File Operations (os module) ---")
# Create and write to a simple file inside our new folder
file_path = os.path.join(dir_name, "sample.txt")
file = open(file_path, "w")
file.write("Hello from the os and sys program!")
file.close()
print("Created file at path:", file_path)

# 6. Check if the file exists
print("Does the file exist?", os.path.exists(file_path))
