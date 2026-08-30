# LEGB 
# Create nested functions with variables having the same name in Global Enclosing and local scopes. Print the variable from different scopes and demonstratge the LEGB rule

x  = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print("Inner:", x)

    print("Outer:", x)
    inner()

print("Global:", x)
outer()        





# global vs local
# create a global variable balance = 100 inside a function, create a local variable with the same name and then create another function that modifies the global balance using global

balance = 100
def show_balance():
    balance = 50
    print("Local balance:", balance)

def update_balance():
    global balance
    balance += 50
show_balance()
update_balance()

print("Global balance:", balance)

