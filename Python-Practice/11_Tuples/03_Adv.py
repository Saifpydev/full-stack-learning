# Create a tuple containing student records find and print the student with the highest marks


students = (
    ("Saif", 85),
    ("Ali", 74),
    ("Rahul", 91)
)
highest = max(students, key=lambda x: x[1])


print("Student:", highest[0])
print("Marks:", highest[1])

# Create a tuple containing numbers from 1 to 10. Using tuple operations, create
# A tuple of even numbers
# A tuple of odd numbers
# A tuple of squares

numbers = (1, 2, 3, 4, 5, 6, 7,  8, 9, 10)
even = numbers[1::2]
odd = numbers[0::2]
square = tuple(x * x for x in numbers)

print("Even:", even)
print("Odd:", odd)
print("Square:", square)