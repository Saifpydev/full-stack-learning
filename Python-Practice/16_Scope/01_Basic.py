# Local Scope
# Create a function with a local variable name and print it inside the function

def  show_name():
    name = "Saif"
    print(name)
show_name()    


# Glboal Scope
# Create a global varriable city and access it inside a function

city = "Delhi"
def show_city():
    print(city)
show_city()    


# Local vs Global
# Create a global variable x = 100 and a local variable x = 50 inside a function print both and observe the difference.
x = 100
def show_value():
    x = 50
    print("Local:", x)
show_value()
print("Global:", x)    



# global Keyword
# Create a global variable count = 0.,  Inside a function, use global to change its value to .
# Print the value outside the function


count  = 0
def update_count():
    global count
    count = 10
update_count()
print("Count:", count)    