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

 
