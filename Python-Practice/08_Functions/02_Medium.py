# Create a function that takes two numbers as parameters and returns their sum

def add(a, b):
    print(a + b)
add(20, 30)    


# Create a function that takes a number and returns its square.

def Square(num):
    return num * num
print(Square(5))

# Create a function that takes a students marks and returns

# "Pass" if marks are 40 or above
# "Fail" otherwise

def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print(check_result(48))
print(check_result(77))


# Create a function that takes name and age as parameters and points

def introduce(name, age):
    print("My name is", name)
    print("My age is", age)

introduce("Saif", 22)


# Create a function that takes three numbers and returns the largest number/

def largest(a, b, c):
    return max(a, b, c)
print(largest(10, 25, 15))