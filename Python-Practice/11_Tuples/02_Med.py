# Updating using conversion
# Convert this tuple into a list, add "Orange", then convert it back to a tuple. 

colors = ("Red", "Blue", "Green")
colors = list(colors)
colors.append("Orange")
colors = tuple(colors)
print(colors)

# Count & Index  find numbers of times 10 occurs and index of 30

numbers = (10, 20, 10, 30, 10, 40)
numbers.count(10)
numbers.index(30)
print(numbers.count(10))
print(numbers.index(30))


# Check Membership Check whether "Python" and "PHP" are present using in/not in.

language = ("Python", "Java", "C++", "JavaScript")

print("Python" in language)
print("PHP" in language)

print("Python" not in language)
print("PHP" not in language)


# Nested Tuple 
data = (("Saif", 25), ("Ali", 30), ("Rahul", 28))
print(data[0][0])
print(data[0][1])
print(data[2][0])
print(data[2][1])





