# Convert Python dictonary to JSON String
# convert the flowing python dictionary inot a JSON string using json.dumps()

import json

# Convert Python dictionart to JSON string

data = {
    "name": "Saif",
    "age": 22,
    "city": "Patna"
}
json_string = json.dumps(data)
print(json_string)



# Convert JSON String to Python Dictionary 
# Convert this JSON string into a python dictionary using json.loads()

json_data = '{"name": "Saif", "age": 25}'

python_data = json.loads(json_data)
print(python_data)


# Read Data from a JSON File
# Read the data from studnet.json and print the student's name and course.

import json
with open("26_JSON/02_Student.json", "r") as file:
    student = json.load(file)
    
print("Name:", student["name"])
print("Course:", student["course"])   

student["age"]  = 24
with open("26_JSON/02_Student.json", "w") as file:
    json.dump(student, file, indent =4)
    
print("Age updated successfully!")    
    
    





# Update JSON Date
# Read student.json chnage the student's age from 23 to 24, and save the updated data back to the file..


 
