# 9. Write a program to use re module functions such as match search and findall. 

import re

text = "Python is fun. I love Python programming!"

print("--- Comparing match, search, and findall ---")

# 1. re.match() - Looks ONLY at the very beginning of the string
match_result = re.match("Python", text)
print("1. re.match('Python'):", match_result)
if match_result:
    print("   Found at the beginning:", match_result.group())

# Trying re.match with a word in the middle
match_fail = re.match("love", text)
print("   re.match('love'):", match_fail) 
print("   (Returns None because 'love' is not at the start)")


# 2. re.search() - Looks anywhere in the entire string, but returns only the FIRST match
search_result = re.search("Python", text)
print("\n2. re.search('Python'):", search_result)
if search_result:
    print("   Found first occurrence:", search_result.group(), "at index position:", search_result.start())


# 3. re.findall() - Finds EVERY occurrence in the string and returns them as a clean List
findall_result = re.findall("Python", text)
print("\n3. re.findall('Python'):", findall_result)
print("   Total matches found:", len(findall_result))
