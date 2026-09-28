""" 10.Write a program to extract specific information 
from a text file using regular expressions. """

import re

print("--- Step 1: Creating a Sample Text File ---")
# Create a dummy file with mixed text, emails, and phone numbers
file_name = "company_data.txt"
file = open(file_name, "w")
file.write("Hello, contact our support team at support@example.com or hr@company.org.\n")
file.write("You can also call us at 123-456-7890 or fax at 987-654-3210.")
file.close()
print("Sample file created:", file_name)


print("\n--- Step 2: Reading the File and Extracting Information ---")
# Open and read the file contents
file = open(file_name, "r")
file_content = file.read()
file.close()

# Define regular expression patterns
# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} matches standard email formats
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# \d{3}-\d{3}-\d{4} matches phone numbers like 123-456-7890
phone_pattern = r"\d{3}-\d{3}-\d{4}"

# Extract all matches using re.findall()
emails_found = re.findall(email_pattern, file_content)
phones_found = re.findall(phone_pattern, file_content)

print("Extracted Emails:", emails_found)
print("Extracted Phone Numbers:", phones_found)
