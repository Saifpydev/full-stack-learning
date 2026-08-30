# Create a function using *args that accepts any number of numbers and returns
# sum Maximum Minimum

def calculate_numbers(*args):
    total = sum(args)
    maximum = max(args)
    minimum = min(args)
    return total, maximum, minimum

result = calculate_numbers(10, 25, 5, 40, 18)
print("Sum:", result[0])
print("Maximum:", result[1])
print("Minimum:", result[2])

# Create a function using **kwargs that accepts employee details and prints all key value pair

def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
employee(
    name = "Saif",
    age = 22,
    city = "Delhi",
    salary = 500000
)

