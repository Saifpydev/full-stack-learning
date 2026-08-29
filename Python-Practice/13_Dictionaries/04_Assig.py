# Find highest Value  find and print student with the highest marks

Marks = {
    "Saif": 99,
    "Raja": 49,
    "Ahmad": 84,
    "Ravi": 76,
    "Kaif": 78,

}

highest = max(Marks.values())
print("Highest Marks:", highest)

for name, marks in Marks.items():
    if marks == highest:
        print("Studnet:", name)



# Create a dictioary containing at least 3 employees, where each employes has Name Age Department Salary 
employes = {
    "emp1": {
        "name": "Saif",
        "age": 25,
        "salary": 100000,
        "department": "IT"
    },
    "emp2": {
        "name": "Ali",
        "age": 26,
        "department": "HR",
        "salary": 80000
    },
    "emp3": {
        "name": "Raja",
        "age": 27, 
        "department": "IT",
        "salary": 80000
    }
}
highest_salary = 0
highest_employee = ""
for employee in employes.values():
    if employee["salary"] > highest_salary:
     highest_salary = employee["salary"]
     highest_employee = employee["name"]

print("Highest Salary:", highest_salary)
print("Employee:", highest_employee)


#  Create a student dictionary containing name, age, course, and city, Print all keys and values.

Student = {
   "name": "Raja",
   "age": 20,
   "course": "BCA",
   "city": "delhi"
}
print(Student)

