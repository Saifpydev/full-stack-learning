# .Current Date & Time

# Write a python program to display the current date and time

from datetime import datetime

# Current Date & Time
now = datetime.now()
print(now)







# Format a Date
# Write a Python program that takes the current date and displays it in the format DD-MM-YYYY. 
 
# Format a Date
print(now.strftime("%d-%m-%Y"))


# Convert String to Date
# Convert the flowing data string into a python datetime object


# Convert String to Data
date_string = "06-09-2026"
date_object = datetime.strptime(date_string, "%d-%m-%Y")
print(date_object)