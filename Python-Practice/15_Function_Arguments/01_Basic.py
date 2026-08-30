# Positional Arguments 
# Create a function introduce () that accept name, age, and city and prints all three values. Call it using positional arguments.

def introduce(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
 
introduce("Saif", 22, "Delhi")
# Note yaha value same order m pass hue hai


# Keyword Arguments
# Create a function student() that accepts name, course, and duration Call it using keyword arguments in a different order.

def student(name, course, duration):
    print("Name:", name)
    print("Course:", course)
    print("Duration:", duration)


student(duration = "6 Months", name = "Saif", course = "Python")


# Create function greet() with a default parameter name = "Guest". Test it both with and without an argument.

def greet(name ="Guest"):
    print("Hello", name)

greet()
greet("Saif")    

# Create a function calculate_bill() that accepts item, price and quantity and returns the total bill amount.

def calculate_bill(item, price, qunatity):
    total = price * qunatity
    print(item, "-", price, "x", qunatity, "=", total)
    return total

bill1 = calculate_bill("Pen", 20, 5)
bill2 = calculate_bill("Notebook", 50, 3)
bill3 = calculate_bill("Pencil", 10, 4)

grand_total = bill1 + bill2 + bill3
print("Grand Total:", grand_total)

