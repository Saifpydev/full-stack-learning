studnet = {
    "name": "Saif",
    "age": 25,
    "course": "Python"
}
print(studnet)
print(type(studnet))


# 02 Access Values
studnet = {
    "name": "Saif",
    "age": 25
}
print(studnet["name"])
print(studnet["age"])


# 03 ADD New Key- Value

studnet = {
    "name": "Ahmad",
    "city": "Delhi"
}

studnet["age"] = 25
print(studnet)

# update Value

studnet = {
    "name": "Rahul",
    "age":  "23"
}
studnet["age"] = 26
print(studnet)


# get()  + len ()
studnet = {
    "name": "Kaif",
    "age": 25,
    "state": "Bihar"
}
print(studnet.get("name"))
print(studnet.get("course"))


print(len(studnet))