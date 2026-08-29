
# Squares

squares = [x * x for x in range(1,6)]
print(squares)

# Double Numbers

numbers = [1, 2, 3, 4, 5]
double = [x * 2 for x in numbers] 
print(double)

# Even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [x for x in numbers if x % 2 == 0]

print(even)

# Convert string to Uppercase

names = ["Saif", "Ahmad", "prince", "raja"]
upper_names = [name.upper() for name in names]
print(upper_names)


# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8,]
squares = {x: x * x for x in numbers}

print(squares)