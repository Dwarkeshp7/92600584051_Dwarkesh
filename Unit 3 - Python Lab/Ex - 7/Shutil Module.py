# 7. Write a program to copy move and delete files using shutil module. 

import os
import shutil

print("--- Step 1: Setting up a test file ---")

# Create an initial file to work with

source_file = "original.txt"
file = open(source_file, "w")
file.write("This is some sample text.")
file.close()
print("Created source file:", source_file)

print("\n--- Step 2: Copying the file ---")

# Copy the original file to a new file named backup.txt

copied_file = "backup.txt"
shutil.copy(source_file, copied_file)
print("Copied", source_file, "to", copied_file)

print("\n--- Step 3: Moving the file ---")

# Create a folder and move the backup file inside it

folder_name = "destination_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Move backup.txt inside destination_folder/

moved_file_path = shutil.move(copied_file, folder_name)
print("Moved", copied_file, "into", folder_name)

print("\n--- Step 4: Deleting the folder and files ---")

# Delete the original file using standard os remove

os.remove(source_file)
print("Deleted original file:", source_file)

# Delete the entire folder and everything inside it using shutil

shutil.rmtree(folder_name)
print("Deleted the entire folder and its contents:", folder_name)
