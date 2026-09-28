# 8. Write a program to demonstrate basic regular expression pattern matching.

import re

text = "My phone number is 123-456-7890 and my zip code is 90210."

print("--- Basic Regular Expression Matching ---")

# 1. Search for a specific word
# re.search() looks for the first match anywhere in the string

word_match = re.search("phone", text)
if word_match:
    print("Found the word 'phone' at position:", word_match.start())
else:
    print("Word 'phone' not found.")

# 2. Match patterns using special characters (\d means any digit)
# Let's find the 5-digit zip code (\d{5} means exactly 5 digits in a row)

zip_pattern = r"\d{5}"
zip_match = re.search(zip_pattern, text)
if zip_match:
    print("Found a 5-digit zip code:", zip_match.group())

# 3. Find all occurrences of a pattern
# Let's find all individual groups of numbers in the string

numbers_list = re.findall(r"\d+", text) # \d+ means one or more digits together
print("All number groups found in the text:", numbers_list)

# 4. Replace a pattern (Regex Substitution)
# Let's hide the numbers by replacing digits with an 'X'

hidden_text = re.sub(r"\d", "X", text)
print("Text with numbers hidden:", hidden_text)
