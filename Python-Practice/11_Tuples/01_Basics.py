colors = ("Red", "Blue", "Green")
print(colors)
print(type(colors))

# Tuple indexing

colors = ("Red", "Orange", "Green")
print(colors[0])
print(colors[-1])

# Tuple Slicing
number = (10, 20, 30, 40, 50)
print(number[1:4])

# len() + count()
numbers = (10, 20, 10, 30, 10)
print(len(number))
print(numbers.count(10))


# index() + Tuple Unpacking

person = ("Saif", 25, "Delhi")

print(person.index(25))
name, age, city = person
print(name)
print(age)
print(city)
