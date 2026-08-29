# Simple Function
def greet():
    print("Hello Python")
greet()    

# Function with Parameter

def greet(name):
    print("Hello", name)
greet("Saif")

# Add two Numbers
def add (a, b):
    print(a + b)
add(10, 20)

# Function with return

def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)
    
# Default Parameter

def greet(name= "User"):
    print("Hello", name)
    greet("Saif") 