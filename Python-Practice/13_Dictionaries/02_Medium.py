# Keys() and values ()
# Create a studnets dictionary and print all keys and all values

student = {
    "name": "Ahmad",
    "course": "BCA",
    "age": 21,
    "city": "Dehli"
}

print(student)

# items () print every key and values using items().
# create 
student = {
    "name": "Saif",
    "age": 22,
    "course": "Python"
}
for key, value in student.items(): 
    print(key, ":", value)

#  Update() create a dictionary 
student = {
    "name": "Raja",
    "age": 25,
    "city": "old_city",
    "course": "JAVA"
}

# Update city and course
student["city"]  = "New city"
student["course"] = "Django"
print(student)