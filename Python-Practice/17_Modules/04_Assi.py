# Demonstrate the difference between local and global scope using the same variable name

x = 100
def show_value():
    x = 50
    print("Local:", x)

show_value()
print("Global:", x)    



# Use the global keyword to modify a global balance variable inside a function

balance = 1000

def update_balance():
    global balance
    balance += 500

update_balance()

print("Balance:", balance)



# Create a nested function and use nonlocal to modiofy an enclosing variable

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count:", count)

    inner() 
    inner()   
    inner()

outer()

# Create a program demonstrating the complete LEGB rule and explain throught output which value Python selects at each scope..

x = "Global"
def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print("Local:", x)
    inner()
    print("Enclosing:", x)

outer()
print("Global:", x)
        