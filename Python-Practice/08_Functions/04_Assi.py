# Create a function that takes a numbers and returns its square and cube

def square_cube(num):
    square  = num * num
    cube = num * num * num
    return square, cube

print(square_cube(25))


# Create a function that takes two numbers and returns
# Sum Difference Product Division

def calculate(a, b):
    sum = a + b
    differece = a - b
    product = a * b
    division = a / b

    return sum, differece, product, division
result = calculate(20, 10)

print("Sum: ", result[0])
print("difference: ", result[1])

print("product: ", result[2])
print("division: ", result[3])
