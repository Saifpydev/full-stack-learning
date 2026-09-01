# Global variable Access
# Create a global variable language = "Python" and access it inside a function without using global

def outer():
    x = 100

    def inner():
        x = 50
        print("Inner:", x)

    print("Outer:", x)
    inner()

outer()

# Global variable update
# Crete a global variable score = 0. Create a function that increases it by using the global keyword

score = 0

def increase_score():
    global score
    score += 10

increase_score()

print("Score:", score)




# Enclosing Scope
# Create an outer() function with x = 100 and an inner () function with x = 50. Print x from both functions and observe the difference.

def outer():
    x = 100

    def inner():
        x = 50
        print("Inner:", x)

    print("Outer:", x)
    inner()    

outer()