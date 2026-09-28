# 5. Write a program to display current date and time using datetime module.

import datetime

current_data = datetime.datetime.now()

print("Current Date and Time:", current_data)
print("Current Year:", current_data.year)
print("Current Month:", current_data.month)
print("Current Day:", current_data.day)
