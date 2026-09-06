# Write a Python program to read students.csv and print every row.

import csv
with open("27_CSV/02_student.csv", "r") as file:
    reader =  csv.reader(file)
    
    for row in reader:
        print(row)