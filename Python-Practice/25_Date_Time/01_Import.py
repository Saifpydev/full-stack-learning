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



# Calculate Age
# Write a Python program to calculate a person's age from theri birth year.

from datetime import date
birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age = current_year - birth_year
print("Your age is:", age)



# find the Date After 30 Days
# write a Python program to find the date after 30 days from today

from datetime import date, timedelta
today = date.today()

after_30_days = today + timedelta(days=30)

print("Today's date:", today)
print("Date after 30 days:", after_30_days)

