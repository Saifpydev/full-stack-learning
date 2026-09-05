# .Create a generator function numbers() that uses yield to generate:

# 1 2 3 4 5 6
# Then use a for loop to print the values

def numbers():
    for i in range(1, 7):
        yield i 
        
for number in numbers():
    print(number)        
        

# Create a generator that generates even numbers from 2 to 20

def even_numbers():
    for i in range(2, 21, 2):
        yield i 
        
for number in even_numbers():
    print(number)        



# Create a generator for the multiplication table of a number

def multiplication_table(number):
    for i in range(1, 11):
        yield number * i
for value in multiplication_table(5):
    print(value)        
