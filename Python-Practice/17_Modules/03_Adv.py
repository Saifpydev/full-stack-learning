# Demonstrate the differebce between local and gloabl scope using the same variable name

x = 100

def show_x():
    x = 50
    print("Local:", x)
show_x()

print("Global:", x)


# Use the global keyword to modify a global balance variable inside a function

balance = 1000

def add_money():
    global balance
    balance += 500

add_money()

print("Balance:", balance)



# Create a counter closure that remembers its count between function calls

def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase

count = counter()

print(count())
print(count())
print(count())

