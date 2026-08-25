#  Create & print Set
numbers = {10, 20, 30, 10}
print(numbers)
print(type(numbers))

#   Note Duplicate automatically remove ho jayga

# add()
fruits = {"Apple", "Mango"}
fruits.add("Banana")
print(fruits)

# Update ()

numbers = {10, 20}
numbers.update([30 ,40, 50])
print(numbers)

# remove() vs discard()

numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

numbers.discard(30)
print(numbers)


# len() + Membership

fruits = {"Apple", "Mango", "Banana"}
print(len(fruits))
print("Apple" in fruits)
print("Orange" not in fruits)