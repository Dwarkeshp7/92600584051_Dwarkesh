"""(8)
Write a python program to enter a string from keyboard and count number of Vowels and No. 
of consonants.  Also give percentage of both.
"""

txt = input("Enter String :")

vowelscount = 0
consonantscount = 0

vowels = "aeiouAEIOU"

for char in txt:
    if char.isalpha():
        if char in vowels:
            vowelscount = vowelscount + 1
        else:
            consonantscount = consonantscount + 1

print("No of Vowel :",vowelscount,", No of Consonants :",consonantscount)

total = vowelscount + consonantscount

if total > 0:
    vowelperc = (vowelscount / total) * 100
    consoperc = (consonantscount / total) * 100
else:
    vowelperc = 0
    consoperc = 0
    
print("-----Result-----")
print("Total Letters :",total)
print("Vowel Percentage :",vowelperc)
print("Consonant Percentage :",consoperc)
