# Local Scope
# Create a function with a local variable name and print it inside the  function

def show_name():
    name = "Kaif"
    print(name)
show_name()

# Note Name function k under local variable hai



# Global Scope
# Create a global variable city and access it inside a function

city = "Delhi"
def show_city():
    print(city)
show_city()

# note city glbal hai islye function ke ander directly access ho sakta hai



# Local vs Global
# Create a global variable x = 100 and a local variable x = 50 inside a function Print both and observe the difference.

x = 100

def show_x():
    x = 50
    print("Local:", x)
    print("Global:", globals)
["x"]

show_x()


# Enclosing Scope
# Create an outer() function with a variable message = "Hello". Define an inner() function inside it and access message from inner()

def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()        
